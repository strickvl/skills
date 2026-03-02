---
name: clean-research-report
description: >-
  Strips citation artifacts and hidden Unicode characters from ChatGPT deep
  research exports (.md or .docx). Use when the user has a .md or .docx file
  from ChatGPT deep research that contains leftover citation tokens (citeturnX,
  fileciteturnX), entity[] tags, garbled Unicode characters, or a trailing
  references dump. Also triggers when user mentions "clean report", "remove
  citations", "fix deep research export", or provides a .docx deep research
  file.
---

# clean-research-report

Cleans ChatGPT deep research exports. Accepts both `.md` and `.docx` files.

For `.docx` input, the script converts to GitHub-flavored markdown via `pandoc` first (must be installed), then applies the full cleaning pipeline. The `.docx` format is **preferred** because ChatGPT's markdown export strips reference hyperlinks while the Word export preserves them as inline links.

## What it removes

- Citation tokens: `citeturn0search0`, `fileciteturn14file18`, chained variants
- Private-use Unicode delimiters: `\ue200`, `\ue201`, `\ue202` (hidden in text)
- Entity annotation tags: `entity["company","Google","internet company"]`
- Trailing references/bibliography section (the URL dump after the last horizontal rule)
- Resulting double spaces and trailing whitespace

## What it preserves

- Inline citation hyperlinks like `[\[1\]](URL)` in the body text (these are the actual useful source links)

## Usage

```bash
# From a .docx file (preferred) — converts + cleans → report_clean.md
uv run {baseDir}/scripts/clean_report.py report.docx

# From a .md file — writes input_clean.md alongside the original
uv run {baseDir}/scripts/clean_report.py input.md

# Explicit output path (works with both .md and .docx)
uv run {baseDir}/scripts/clean_report.py input.docx output.md

# Overwrite .md in place (not available for .docx — never overwrites the original)
uv run {baseDir}/scripts/clean_report.py input.md --inplace
```

### Prerequisites

- **pandoc** is required for `.docx` conversion: `brew install pandoc` (macOS) or see https://pandoc.org/installing.html

## Workflow

1. Identify the file the user wants cleaned (`.md` or `.docx`)
2. Run: `uv run {baseDir}/scripts/clean_report.py <input> [output | --inplace]`
3. Report where the cleaned `.md` file was written
