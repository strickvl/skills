# Clean Research Report

Strip citation artifacts and hidden Unicode characters from ChatGPT deep research markdown exports.

## What It Does

When you export a ChatGPT deep research report as markdown, the file often contains leftover citation tokens, private-use Unicode delimiters, and entity annotation tags that clutter the text. This skill auto-triggers when Claude detects you're working with such a file and cleans it up.

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
mkdir -p ~/.claude/skills/clean-research-report/scripts
cp clean-research-report/SKILL.md ~/.claude/skills/clean-research-report/
cp clean-research-report/scripts/clean_report.py ~/.claude/skills/clean-research-report/scripts/

# Make script executable
chmod +x ~/.claude/skills/clean-research-report/scripts/clean_report.py
```

## Usage

The skill triggers automatically when Claude detects you're working with a ChatGPT deep research markdown export. You can also ask directly:

- "Clean this research report"
- "Remove the citation artifacts from this file"
- "Fix this deep research export"

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition — auto-triggers on relevant user requests |
| `scripts/clean_report.py` | Python script — regex-based cleaning of citation artifacts |

## How It Works

The script applies a pipeline of regex substitutions:

1. Strips `cite`/`filecite` tokens, including variants wrapped in Unicode private-use characters
2. Removes any remaining `\ue200`–`\ue202` characters
3. Removes `entity[...]` annotation tags
4. Collapses double spaces that the removals leave behind
5. Trims trailing whitespace from each line
