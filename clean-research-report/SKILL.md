---
name: clean-research-report
description: >-
  Strips citation artifacts and hidden Unicode characters from ChatGPT deep
  research markdown exports. Use when the user has a .md file from ChatGPT deep
  research that contains leftover citation tokens (citeturnX, fileciteturnX),
  entity[] tags, or garbled Unicode characters that clutter the reading
  experience. Also triggers when user mentions "clean report", "remove
  citations", or "fix deep research export".
---

# clean-research-report

Removes ChatGPT deep research citation artifacts from markdown files.

## What it removes

- Citation tokens: `citeturn0search0`, `fileciteturn14file18`, chained variants
- Private-use Unicode delimiters: `\ue200`, `\ue201`, `\ue202` (hidden in text)
- Entity annotation tags: `entity["company","Google","internet company"]`
- Resulting double spaces and trailing whitespace

## Usage

Run the script against any markdown file:

```bash
# Default: writes input_clean.md alongside the original
uv run {baseDir}/scripts/clean_report.py input.md

# Explicit output path
uv run {baseDir}/scripts/clean_report.py input.md output.md

# Overwrite in place
uv run {baseDir}/scripts/clean_report.py input.md --inplace
```

## Workflow

1. Identify the markdown file the user wants cleaned
2. Run: `uv run {baseDir}/scripts/clean_report.py <input> [output | --inplace]`
3. Report where the cleaned file was written
