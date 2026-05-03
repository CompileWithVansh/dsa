"""
fetch_question.py
Fetches a LeetCode question by number using the public GraphQL API.
Outputs a clean markdown string to stdout.

Usage:
    python fetch_question.py <lc_number>
    python fetch_question.py 42
"""

import sys
import json
import urllib.request
import urllib.error
import html
import re


def fetch_question(lc_number: str) -> dict:
    url = "https://leetcode.com/graphql"

    query = """
    query getQuestion($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            title
            difficulty
            content
            exampleTestcases
            topicTags { name }
            hints
        }
    }
    """

    # First get the title slug from the question number
    slug_query = """
    query problemsetQuestionList($skip: Int, $limit: Int) {
        problemsetQuestionList: questionList(
            categorySlug: ""
            limit: $limit
            skip: $skip
            filters: {}
        ) {
            questions: data {
                questionId
                titleSlug
                title
                difficulty
            }
        }
    }
    """

    # Search by question ID using the daily/title approach
    # Use the questionId -> titleSlug lookup
    lookup_query = """
    query {
        allQuestionsCount { difficulty count }
    }
    """

    # Direct approach: use the question title slug via search
    search_query = """
    query problemSearch($query: String!) {
        problemsetQuestionList: questionList(
            categorySlug: ""
            limit: 5
            skip: 0
            filters: { searchKeywords: $query }
        ) {
            questions: data {
                questionId
                titleSlug
                title
                difficulty
            }
        }
    }
    """

    payload = json.dumps({
        "query": search_query,
        "variables": {"query": lc_number}
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://leetcode.com"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"ERROR: Could not reach LeetCode API: {e}", file=sys.stderr)
        sys.exit(1)

    questions = data.get("data", {}).get("problemsetQuestionList", {}).get("questions", [])

    # Find exact match by questionId
    match = None
    for q in questions:
        if q["questionId"] == str(lc_number):
            match = q
            break

    if not match:
        print(f"ERROR: Question #{lc_number} not found.", file=sys.stderr)
        sys.exit(1)

    title_slug = match["titleSlug"]

    # Now fetch full question details
    detail_payload = json.dumps({
        "query": query,
        "variables": {"titleSlug": title_slug}
    }).encode("utf-8")

    req2 = urllib.request.Request(
        url,
        data=detail_payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": f"https://leetcode.com/problems/{title_slug}/"
        }
    )

    try:
        with urllib.request.urlopen(req2, timeout=10) as resp:
            detail = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"ERROR: Could not fetch question details: {e}", file=sys.stderr)
        sys.exit(1)

    q = detail.get("data", {}).get("question", {})
    if not q:
        print(f"ERROR: No details returned for #{lc_number}", file=sys.stderr)
        sys.exit(1)

    return {
        "id":         q.get("questionId", lc_number),
        "title":      q.get("title", "Unknown"),
        "difficulty": q.get("difficulty", ""),
        "content":    q.get("content", ""),
        "tags":       [t["name"] for t in q.get("topicTags", [])],
        "hints":      q.get("hints", []),
        "slug":       title_slug
    }


def html_to_markdown(html_content: str) -> str:
    """Convert LeetCode HTML content to readable markdown."""
    text = html_content

    # Code blocks
    text = re.sub(r"<pre>(.*?)</pre>", lambda m: "\n```\n" + m.group(1) + "\n```\n", text, flags=re.DOTALL)

    # Bold
    text = re.sub(r"<strong>(.*?)</strong>", r"**\1**", text, flags=re.DOTALL)
    text = re.sub(r"<b>(.*?)</b>", r"**\1**", text, flags=re.DOTALL)

    # Italic
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.DOTALL)

    # Inline code
    text = re.sub(r"<code>(.*?)</code>", r"`\1`", text, flags=re.DOTALL)

    # Paragraphs and line breaks
    text = re.sub(r"<p>(.*?)</p>", r"\1\n", text, flags=re.DOTALL)
    text = re.sub(r"<br\s*/?>", "\n", text)

    # Lists
    text = re.sub(r"<ul>(.*?)</ul>", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"<li>(.*?)</li>", r"- \1", text, flags=re.DOTALL)

    # Superscript
    text = re.sub(r"<sup>(.*?)</sup>", r"^\1", text)

    # Remove remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Decode HTML entities
    text = html.unescape(text)

    # Clean up extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def build_markdown(q: dict, date_label: str = "") -> str:
    content_md = html_to_markdown(q["content"])
    tags = ", ".join(q["tags"]) if q["tags"] else "N/A"
    date_line = f"\n**Date:** {date_label}" if date_label else ""
    lc_url = f"https://leetcode.com/problems/{q['slug']}/"

    md = f"""# {q['title']}

**LeetCode:** #{q['id']}{date_line}
**Difficulty:** {q['difficulty']}
**Topics:** {tags}
**Link:** {lc_url}

## Problem Statement

{content_md}
"""

    if q["hints"]:
        md += "\n## Hints\n\n"
        for i, hint in enumerate(q["hints"], 1):
            md += f"{i}. {html.unescape(re.sub(r'<[^>]+>', '', hint))}\n"

    md += "\n## My Approach\n\n### Brute Force\n<!-- explain here -->\n\n### Optimal\n<!-- explain here -->\n"

    return md


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_question.py <lc_number> [date_label]", file=sys.stderr)
        sys.exit(1)

    lc_number  = sys.argv[1]
    date_label = sys.argv[2] if len(sys.argv) > 2 else ""

    question = fetch_question(lc_number)
    markdown = build_markdown(question, date_label)

    # Print title and difficulty back to PowerShell on first two lines
    # so PS can use them (title|difficulty|markdown...)
    print(f"TITLE:{question['title']}")
    print(f"DIFFICULTY:{question['difficulty']}")
    print("MARKDOWN_START")
    print(markdown)
