---
description: >-
  Strip citation artifacts and hidden Unicode characters from ChatGPT deep
  research markdown exports. Use when you have a .md file exported from ChatGPT
  deep research that contains leftover citation tokens (citeturnX,
  fileciteturnX), entity[] tags, or garbled Unicode characters that clutter the
  reading experience.
allowed-tools:
  - Bash
  - Read
argument-hint: "<path-to-markdown-file> [output-path | --inplace]"
---

# clean-research-report

Clean a ChatGPT deep research markdown export by removing citation artifacts.

## What it removes

- Citation tokens: `citeturn0search0`, `fileciteturn14file18`, chained variants
- Private-use Unicode delimiters: `\ue200`, `\ue201`, `\ue202` (hidden in text)
- Entity annotation tags: `entity["company","Google","internet company"]`
- Resulting double spaces and trailing whitespace

## Your Task

1. **Identify the input file**: The user wants to clean `$ARGUMENTS`.
   - If no argument provided, ask the user which file to clean.
   - Verify the file exists before proceeding.

2. **Run the cleaning script**:
   ```bash
   uv run "$HOME/.claude/scripts/clean_report.py" $ARGUMENTS
   ```

3. **Report results**: Tell the user where the cleaned file was written and summarize what was removed (if anything notable).

## Default behavior

- No output path specified: writes `<input>_clean.md` alongside the original
- Explicit output path: `uv run ~/.claude/scripts/clean_report.py input.md output.md`
- Overwrite in place: `uv run ~/.claude/scripts/clean_report.py input.md --inplace`
