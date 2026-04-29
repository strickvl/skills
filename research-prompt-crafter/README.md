# Research Prompt Crafter

Craft high-quality prompts for deep research models — the kind where you send a prompt and wait 5-20+ minutes for a comprehensive response.

## What It Does

Walks you through a structured workflow to turn rough ideas into optimized research prompts for:

- **GPT-5.5** — with outcome-first goals, success criteria, retrieval budgets, verification loops, and reasoning effort guidance
- **Claude Opus 4.7** — with adaptive thinking, new effort levels (`xhigh`/`max`), explicit scope, and competing hypotheses patterns
- **Gemini 3 Pro** — with instruction placement, self-critique, and grounding rules
- **DeepSeek** — using generic cross-model patterns

The skill gathers your brain dump, clarifies ambiguities, proposes a structure, and generates a final prompt with model-specific optimizations.

## Installation

### Claude Code (marketplace plugin)

```bash
# First, add the marketplace (one-time setup):
/plugin marketplace add strickvl/skills

# Then install the plugin:
/plugin install research-prompt-crafter@strickvl-skills
```

Or install manually:

```bash
mkdir -p ~/.claude/skills/research-prompt-crafter
cp skills/research-prompt-crafter/* ~/.claude/skills/research-prompt-crafter/
```

### claude.ai Skills

To add this as a skill in claude.ai:

1. Clone this repo (or download the `research-prompt-crafter/` folder)
2. Zip up the `skills/research-prompt-crafter/` directory contents (SKILL.md + the pattern files)
3. Go to [claude.ai/customize/skills](https://claude.ai/customize/skills)
4. Upload the zip file

## Usage

The skill triggers when you ask Claude to help craft a research prompt:

- "Help me write a prompt for deep research"
- "Craft a research prompt for GPT-5.5"
- "I need a prompt for Gemini"
- "Write a prompt that will take a while to run"

## Files

```
research-prompt-crafter/
├── .claude-plugin/
│   └── plugin.json                        # Plugin metadata
├── skills/
│   └── research-prompt-crafter/
│       ├── SKILL.md                       # Skill definition & workflow
│       ├── gpt-5-5-patterns.md            # GPT-5.5 (from OpenAI prompt guidance)
│       ├── claude-4-7-patterns.md         # Claude Opus 4.7 (from Anthropic best practices)
│       └── gemini-3-patterns.md           # Gemini 3 Pro
└── README.md
```

## Workflow

1. **Confirm target model** — loads the right patterns file
2. **Gather brain dump** — accepts messy, unstructured input
3. **Clarify ambiguities** — resolves contradictions and vague terms
4. **Propose structure** — outlines the prompt before writing it
5. **Generate final prompt** — applies model-specific patterns
6. **Save output** — writes to `design/` or repo root as `{topic}-{model}-prompt.md`
