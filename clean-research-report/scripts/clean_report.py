#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# ///
"""
clean_report.py — strips ChatGPT deep research citation artifacts from exports.

Accepts .md or .docx files. For .docx, converts to markdown via pandoc first,
then applies the same cleaning pipeline.

Removes:
  - Citation tokens: citeturnXsearchY, fileciteturnXfileY, etc.
  - Private-use Unicode delimiters: \\ue200, \\ue201, \\ue202
  - entity[] annotation tags
  - Trailing references/bibliography section (URL dump after final horizontal rule)

Usage:
  python clean_report.py input.md                  # writes input_clean.md
  python clean_report.py report.docx               # converts + cleans → report_clean.md
  python clean_report.py input.md output.md        # explicit output path
  python clean_report.py input.md --inplace        # overwrite in place
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

DOCX_SUFFIXES = {'.docx', '.doc'}


def convert_docx_to_md(docx_path: Path) -> str:
    """Convert a .docx file to GitHub-flavored markdown via pandoc."""
    pandoc = shutil.which('pandoc')
    if not pandoc:
        print(
            "Error: pandoc is required to convert .docx files but was not found.\n"
            "Install it: brew install pandoc  (macOS) or see https://pandoc.org/installing.html",
            file=sys.stderr,
        )
        sys.exit(1)

    result = subprocess.run(
        [pandoc, str(docx_path), '-f', 'docx', '-t', 'gfm', '--wrap=none'],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Error: pandoc conversion failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)

    return result.stdout


def strip_trailing_references(text: str) -> str:
    """Remove the bibliography/references dump that appears after the last horizontal rule.

    ChatGPT deep research exports (especially from .docx → pandoc) append a section
    like:
        ---
        [\\[1\\]](URL) ... URL
        <URL>
        [\\[2\\]](URL) ...

    This function finds the last horizontal rule and checks whether everything after it
    is reference lines. If so, it strips from the rule onward.
    """
    lines = text.split('\n')

    # Find the last horizontal rule (3+ dashes/asterisks/underscores, possibly with spaces)
    last_hr_idx = None
    for i in range(len(lines) - 1, -1, -1):
        stripped = lines[i].strip()
        if re.match(r'^[-*_]{3,}[-*_ ]*$', stripped) and stripped:
            last_hr_idx = i
            break

    if last_hr_idx is None:
        return text

    # Check if everything after the HR is reference-like content
    # Reference lines match: [\[N\]](URL), <URL>, bare URLs, or blank lines
    ref_pattern = re.compile(
        r'^\s*$'                           # blank line
        r'|^\s*(\\\[)?\[\\?\[\d+\\?\]\]'   # [\[N\]](...)  or \[\[N\]\](...)
        r'|^\s*<https?://[^>]+>\s*$'        # <URL> autolink
        r'|^\s*https?://\S+\s*$'            # bare URL
    )

    after_hr = lines[last_hr_idx + 1:]
    if all(ref_pattern.match(line) for line in after_hr):
        # Strip the HR and everything after it, plus any trailing blank lines before it
        trimmed = lines[:last_hr_idx]
        while trimmed and trimmed[-1].strip() == '':
            trimmed.pop()
        return '\n'.join(trimmed) + '\n'

    return text


def clean(text: str) -> str:
    # Remove cite tokens (with optional Unicode wrappers \ue200-\ue202)
    # Character class includes A-Z and hyphen to catch line-ref suffixes like L1-L1
    text = re.sub(r'[ \t]*(file)?cite[\ue200\ue201\ue202a-zA-Z0-9\-]*(\ue202[^\ue201]*\ue201)?', '', text)
    # Remove any remaining private-use Unicode chars
    text = re.sub(r'[\ue200\ue201\ue202]+', '', text)
    # Remove entity[] annotation tags
    text = re.sub(r'entity\[.*?\]', '', text)
    # Strip trailing references/bibliography section
    text = strip_trailing_references(text)
    # Collapse inline double spaces (not at line starts)
    text = re.sub(r'(?<=[^\n])  +', ' ', text)
    # Remove trailing whitespace from lines
    text = re.sub(r'[ \t]+\n', '\n', text)
    return text


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ('-h', '--help'):
        print(__doc__)
        sys.exit(0)

    inplace = '--inplace' in args
    paths = [a for a in args if not a.startswith('--')]

    if len(paths) == 0:
        print("Error: no input file specified.", file=sys.stderr)
        sys.exit(1)

    input_path = Path(paths[0])
    if not input_path.exists():
        print(f"Error: file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    is_docx = input_path.suffix.lower() in DOCX_SUFFIXES

    # Read or convert input to markdown text
    if is_docx:
        text = convert_docx_to_md(input_path)
    else:
        text = input_path.read_text(encoding='utf-8')

    cleaned = clean(text)

    # Determine output path (.docx always outputs as .md, never overwrites the .docx)
    if is_docx:
        if len(paths) >= 2:
            output_path = Path(paths[1])
        else:
            output_path = input_path.with_stem(input_path.stem + '_clean').with_suffix('.md')
    elif inplace:
        output_path = input_path
    elif len(paths) >= 2:
        output_path = Path(paths[1])
    else:
        output_path = input_path.with_stem(input_path.stem + '_clean')

    output_path.write_text(cleaned, encoding='utf-8')
    print(f"Cleaned: {input_path} → {output_path}")


if __name__ == '__main__':
    main()
