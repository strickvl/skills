# Claude Code Skills & Agents

A collection of reusable skills and sub-agents for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

**Use at your own risk.** These are personal productivity tools that may require specific setups or configurations.

## Available Skills

| Skill | Description | Requirements |
|-------|-------------|--------------|
| [detour](./detour/) | Spawn isolated exploration in a tmux side pane | tmux |
| [clean-research-report](./clean-research-report/) | Strip citation artifacts from ChatGPT deep research markdown exports | Python 3.12+, uv |
| [research-prompt-crafter](./research-prompt-crafter/) | Craft optimized prompts for deep research models (GPT-5.4, Claude 4.6, Gemini 3) | — |
| [going-to-the-library](./going-to-the-library/) | Map a field like a research librarian — browse curated shelves, then apply what you borrowed to your problem | Web search recommended |

## Installation

### Claude Code plugin (for skills with `.claude-plugin/`)

Skills that include a `.claude-plugin/plugin.json` can be installed as plugins from this marketplace:

```bash
# First, add this repo as a marketplace (one-time setup):
/plugin marketplace add strickvl/skills

# Then install any plugin:
/plugin install research-prompt-crafter@strickvl-skills
```

### Manual install (copy to `~/.claude/`)

Each skill has its own installation instructions in its README. Generally:

```bash
# Example: Install detour skill
cp -r detour/commands/* ~/.claude/commands/
cp -r detour/scripts/* ~/.claude/scripts/
cp -r detour/agents/* ~/.claude/agents/
```

### claude.ai Skills

To use a skill in claude.ai (web):

1. Clone this repo or download the skill folder
2. Zip up the contents of the skill's `skills/<skill-name>/` directory
3. Go to [claude.ai/customize/skills](https://claude.ai/customize/skills)
4. Upload the zip file

## Structure

Skills use one of three Claude Code extension mechanisms:

**Plugins** (installable via `/plugin install`):
```
skill-name/
├── .claude-plugin/
│   └── plugin.json     # Plugin metadata (name, description, author)
├── skills/
│   └── skill-name/
│       └── SKILL.md    # Skill definition + reference files
└── README.md
```

**Auto-triggered skills** (installed to `~/.claude/skills/`):
```
skill-name/
├── README.md           # Human documentation
├── SKILL.md            # Skill definition (name + description frontmatter)
└── scripts/            # Executable code
```

**Slash commands** (installed to `~/.claude/commands/`, `scripts/`, `agents/`):
```
skill-name/
├── README.md           # Human documentation
├── commands/           # Slash commands (*.md)
├── scripts/            # Bash/Python scripts
└── agents/             # Sub-agent definitions
```

## Contributing

Feel free to fork and adapt for your own use. PRs welcome for improvements.

## License

MIT
