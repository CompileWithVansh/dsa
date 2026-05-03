# DSA Revision Sheet

This repository is for **revision and daily practice**. It contains solutions to DSA problems organized by topic, plus a daily streak folder for LeetCode daily challenges — so I can track progress, maintain GitHub activity, and revisit solutions without reopening LeetCode every time.

## Motive

- Revise solutions topic-wise at any point
- Maintain a daily LeetCode streak with a dedicated folder
- Track progress across all major DSA topics
- Keep solutions clean and accessible in one place

## How It's Structured

```
DSA/
├── arrays/
├── strings/
├── linked-list/
├── stack-queue/
├── trees/
├── graph/
├── dynamic-programming/
├── recursion-backtracking/
├── dailystreak/              ← LeetCode daily challenge solutions
│
├── nq.ps1                    ← script: create a new question folder
├── fq.py                     ← script: fetch question from LeetCode API
└── push.ps1                  ← script: commit and push to GitHub
```

### Topic folders

Each topic folder contains question subfolders named `LC-<number>`:

```
arrays/
└── LC-42/
    ├── bruteforce.java   (or .py)
    ├── optimal.java      (or .py)
    └── Trapping Rain Water.md
```

### Daily Streak folder

Daily challenge solutions go inside `dailystreak/`. Folder names include the date:

```
dailystreak/
└── LC-42(4thMay26)/
    ├── bruteforce.py
    ├── optimal.py
    └── problem.md        ← auto-filled from LeetCode
```

---

## Automation Scripts

This repo includes three scripts to make adding questions fast — no manual folder creation or copy-pasting needed.

### `nq.ps1` — Create a new question

Scaffolds a new question folder with all files in one command.

```powershell
.\nq.ps1
```

It will ask:
1. **LC Number** — e.g. `42`
2. **Language** — `1` for Python, `2` for Java
3. **Topic** — pick a number from the menu (no typing long folder names)

Then it automatically:
- Fetches the full problem statement from LeetCode (via `fq.py`)
- Creates the folder in the right location with the correct naming format
- Writes `bruteforce`, `optimal`, and `problem.md` / `<Title>.md`
- Offers to open the folder in VS Code

### `fq.py` — LeetCode question fetcher

Called internally by `nq.ps1`. Hits the LeetCode GraphQL API and returns the problem statement, examples, constraints, difficulty, and topic tags as markdown.

You don't need to run this directly — `nq.ps1` handles it. But you can use it standalone:

```bash
python fq.py 42
```

Requires Python 3 (no extra packages needed — uses only stdlib).

### `push.ps1` — Push to GitHub

Stages all changes, commits with your message, and pushes in one command.

```powershell
.\push.ps1
```

Or pass the message directly to skip the prompt:

```powershell
.\push.ps1 "LC-42 Trapping Rain Water solved"
```

---

## Topics Covered

- Arrays
- Strings
- Recursion & Backtracking
- Linked List
- Stack & Queue
- Trees
- Graph
- Dynamic Programming
- Daily Streak

## Note on Solutions

Solutions are written in Java or Python depending on the problem. Each folder has both a brute force and an optimal approach, with time and space complexity noted at the top of each file.
