"""
fq.py
Fetches a LeetCode question by number using the public GraphQL API.
Outputs a clean markdown string to stdout.

Usage:
    python fq.py <lc_number>
    python fq.py 42
"""

import sys
import json
import urllib.request
import urllib.error
import html
import re


GRAPHQL_URL = "https://leetcode.com/graphql"

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://leetcode.com",
    "x-csrftoken": "dummy",
}


def graphql(query: str, variables: dict) -> dict:
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(GRAPHQL_URL, data=payload, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"ERROR: HTTP {e.code} from LeetCode API", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Could not reach LeetCode API: {e}", file=sys.stderr)
        sys.exit(1)


def get_title_slug(lc_number: str) -> tuple[str, str, str]:
    """Get titleSlug, title, difficulty from question number using problemsetQuestionList."""
    query = """
    query problemsetQuestionList($skip: Int, $limit: Int, $filters: QuestionListFilterInput) {
        problemsetQuestionList: questionList(
            categorySlug: ""
            limit: $limit
            skip: $skip
            filters: $filters
        ) {
            questions: data {
                questionFrontendId
                titleSlug
                title
                difficulty
            }
        }
    }
    """
    # Use frontendQuestionId filter — most reliable approach
    data = graphql(query, {
        "skip": 0,
        "limit": 1,
        "filters": {"searchKeywords": lc_number}
    })

    questions = (
        data.get("data", {})
            .get("problemsetQuestionList", {})
            .get("questions", [])
    )

    # Find exact match by frontend ID
    for q in questions:
        if str(q.get("questionFrontendId", "")) == str(lc_number):
            return q["titleSlug"], q["title"], q["difficulty"]

    # If search didn't return exact match, try fetching more results
    # by using a broader search and scanning
    data2 = graphql(query, {
        "skip": max(0, int(lc_number) - 3),
        "limit": 10,
        "filters": {}
    })
    questions2 = (
        data2.get("data", {})
             .get("problemsetQuestionList", {})
             .get("questions", [])
    )
    for q in questions2:
        if str(q.get("questionFrontendId", "")) == str(lc_number):
            return q["titleSlug"], q["title"], q["difficulty"]

    print(f"ERROR: Question #{lc_number} not found in LeetCode.", file=sys.stderr)
    sys.exit(1)


def get_question_details(title_slug: str) -> dict:
    """Fetch full question content by titleSlug."""
    query = """
    query getQuestion($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
            content
            topicTags { name }
            hints
        }
    }
    """
    data = graphql(query, {"titleSlug": title_slug})
    q = data.get("data", {}).get("question")
    if not q:
        print(f"ERROR: No details returned for slug '{title_slug}'", file=sys.stderr)
        sys.exit(1)
    return q


def html_to_markdown(html_content: str) -> str:
    """Convert LeetCode HTML content to readable markdown."""
    text = html_content

    # Code blocks — handle <pre> with nested tags
    text = re.sub(
        r"<pre>(.*?)</pre>",
        lambda m: "\n```\n" + re.sub(r"<[^>]+>", "", m.group(1)).strip() + "\n```\n",
        text, flags=re.DOTALL
    )

    # Bold / italic / inline code
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text, flags=re.DOTALL)
    text = re.sub(r"<b>(.*?)</b>",           r"**\1**", text, flags=re.DOTALL)
    text = re.sub(r"<em>(.*?)</em>",          r"*\1*",   text, flags=re.DOTALL)
    text = re.sub(r"<code>(.*?)</code>",      r"`\1`",   text, flags=re.DOTALL)

    # Paragraphs and line breaks
    text = re.sub(r"<p>(.*?)</p>", r"\1\n", text, flags=re.DOTALL)
    text = re.sub(r"<br\s*/?>", "\n", text)

    # Lists
    text = re.sub(r"<ul>(.*?)</ul>", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"<ol>(.*?)</ol>", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"<li>(.*?)</li>", r"- \1\n", text, flags=re.DOTALL)

    # Superscript
    text = re.sub(r"<sup>(.*?)</sup>", r"^\1", text)

    # Remove remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Decode HTML entities
    text = html.unescape(text)

    # Clean up extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def build_markdown(q: dict, slug: str, date_label: str = "") -> str:
    content_md = html_to_markdown(q.get("content") or "")
    tags = ", ".join(t["name"] for t in q.get("topicTags", [])) or "N/A"
    date_line = f"\n**Date:** {date_label}" if date_label else ""
    lc_url = f"https://leetcode.com/problems/{slug}/"

    md = f"""# {q['title']}

**LeetCode:** #{q['questionFrontendId']}{date_line}
**Difficulty:** {q['difficulty']}
**Topics:** {tags}
**Link:** {lc_url}

## Problem Statement

{content_md}
"""

    hints = q.get("hints", [])
    if hints:
        md += "\n## Hints\n\n"
        for i, hint in enumerate(hints, 1):
            clean = html.unescape(re.sub(r"<[^>]+>", "", hint))
            md += f"{i}. {clean}\n"

    md += "\n## My Approach\n\n### Brute Force\n<!-- explain here -->\n\n### Optimal\n<!-- explain here -->\n"

    return md


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fq.py <lc_number> [date_label]", file=sys.stderr)
        sys.exit(1)

    lc_number  = sys.argv[1]
    date_label = sys.argv[2] if len(sys.argv) > 2 else ""

    slug, title, difficulty = get_title_slug(lc_number)
    details  = get_question_details(slug)
    markdown = build_markdown(details, slug, date_label)

    print(f"TITLE:{title}")
    print(f"DIFFICULTY:{difficulty}")
    print("MARKDOWN_START")
    print(markdown)
