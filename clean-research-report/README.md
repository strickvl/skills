# Clean Research Report

Strip citation artifacts and hidden Unicode characters from ChatGPT deep research markdown exports.

## What It Does

When you export a ChatGPT deep research report as markdown, the file often contains leftover citation tokens, private-use Unicode delimiters, and entity annotation tags that clutter the text. This skill removes them cleanly.

### What it removes

- **Citation tokens**: `citeturn0search0`, `fileciteturn14file18`, chained variants
- **Private-use Unicode delimiters**: `\ue200`, `\ue201`, `\ue202` (invisible in most editors but break copy-paste)
- **Entity annotation tags**: `entity["company","Google","internet company"]`
- **Resulting double spaces** and trailing whitespace

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (for running the script)

## Installation

```bash
# From the skills repo root:
mkdir -p ~/.claude/{commands,scripts}
cp clean-research-report/commands/clean-research-report.md ~/.claude/commands/
cp clean-research-report/scripts/clean_report.py ~/.claude/scripts/

# Make script executable
chmod +x ~/.claude/scripts/clean_report.py
```

## Usage

```
/clean-research-report path/to/report.md
```

### Modes

```bash
# Default: writes report_clean.md alongside the original
/clean-research-report report.md

# Explicit output path
/clean-research-report report.md cleaned_output.md

# Overwrite in place
/clean-research-report report.md --inplace
```

## Files

| File | Purpose |
|------|---------|
| `commands/clean-research-report.md` | Slash command — identifies the file and runs the script |
| `scripts/clean_report.py` | Python script — regex-based cleaning of citation artifacts |

## How It Works

The script applies a pipeline of regex substitutions:

1. Strips `cite`/`filecite` tokens, including variants wrapped in Unicode private-use characters
2. Removes any remaining `\ue200`–`\ue202` characters
3. Removes `entity[...]` annotation tags
4. Collapses double spaces that the removals leave behind
5. Trims trailing whitespace from each line
