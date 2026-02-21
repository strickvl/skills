#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# ///
"""
clean_report.py — strips ChatGPT deep research citation artifacts from markdown exports.

Removes:
  - Citation tokens: citeturnXsearchY, fileciteturnXfileY, etc.
  - Private-use Unicode delimiters: \\ue200, \\ue201, \\ue202
  - entity[] annotation tags

Usage:
  python clean_report.py input.md                  # writes input_clean.md
  python clean_report.py input.md output.md        # explicit output path
  python clean_report.py input.md --inplace        # overwrite in place
"""

import re
import sys
from pathlib import Path


def clean(text: str) -> str:
    # Remove cite tokens (with optional Unicode wrappers \ue200-\ue202)
    text = re.sub(r'[ \t]*(file)?cite[\ue200\ue201\ue202a-z0-9]*(\ue202[^\ue201]*\ue201)?', '', text)
    # Remove any remaining private-use Unicode chars
    text = re.sub(r'[\ue200\ue201\ue202]+', '', text)
    # Remove entity[] annotation tags
    text = re.sub(r'entity\[.*?\]', '', text)
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

    if inplace:
        output_path = input_path
    elif len(paths) >= 2:
        output_path = Path(paths[1])
    else:
        output_path = input_path.with_stem(input_path.stem + '_clean')

    text = input_path.read_text(encoding='utf-8')
    cleaned = clean(text)
    output_path.write_text(cleaned, encoding='utf-8')
    print(f"Cleaned: {input_path} → {output_path}")


if __name__ == '__main__':
    main()
