# Going to the Library

Map a specialized subject like a rigorous research librarian: browse its foundational works, modern syntheses, competing schools, practical authorities, critiques, and live debates — then carry the useful ideas back into your real problem.

<img width="589" height="478" alt="CleanShot 2026-08-24 at 09 45 40" src="https://github.com/user-attachments/assets/3cc06caa-87a4-40d3-9a87-9ab9952d35f4" />

(Credit to [Chris Kercher on X](https://x.com/ChrisKercher_/status/2091619783271686372) for the original idea)

## What It Does

Say "let's go to the library on X" and Claude builds a curated, verified map of the field organized around its governing questions (not a dump of famous names). You then browse interactively — expand a shelf, pull a single work, compare two schools, assemble a reading stack — and finish with a "return to the workbench" memo that applies what you borrowed to the problem that sent you to the library in the first place.

Key properties:

- **Curated, not exhaustive**: a standard visit is 12–20 sources arranged on 6–8 themed shelves, each built around one guiding question.
- **Verified**: every named source is checked to exist before it's presented; when web access is unavailable, the result is labeled as provisional and memory-based rather than passed off as a bibliography.
- **Honest about disagreement**: competing schools are presented in their strongest form, and criticism/failure evidence gets its own shelf.
- **Ends at your problem**: the visit closes with a transfer memo — what changed, what to adopt/reject/test, and the next concrete move.

## Layout

- `SKILL.md` — the skill definition and full workflow
- `references/research-protocol.md` — the source-verification protocol for unfamiliar or contested subjects
- `references/interaction-templates.md` — templates for browsing operations (pull, compare, stack, ledger)
- `agents/openai.yaml` — interface metadata for OpenAI-compatible Agent Skills hosts
- `evals/test-cases.md` — evaluation scenarios

## Requirements

- Web or scholarly-search access is strongly recommended (and required for a genuinely current "live debates" shelf).

## Installation

```bash
# From the skills repo root:
mkdir -p ~/.claude/skills/going-to-the-library
cp going-to-the-library/SKILL.md ~/.claude/skills/going-to-the-library/
cp -r going-to-the-library/references ~/.claude/skills/going-to-the-library/
```

## Usage

The skill triggers on phrases like:

- "Let's go to the library on Bayesian experimental design"
- "Give me a structured map of the field of organizational memory"
- "I need orientation in supply-chain resilience before I design this system"

Once the floor plan appears, browse with natural language or the optional verbs: `tour`, `shelf <n>`, `pull <work>`, `compare A and B`, `stack <goal>`, `counter-shelf`, `periodicals`, `receipt`, and `return` (to bring it all back to your problem).

## License

MIT
