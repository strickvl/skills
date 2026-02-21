# Claude Code Skills & Agents

A collection of reusable skills and sub-agents for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

**Use at your own risk.** These are personal productivity tools that may require specific setups or configurations.

## Available Skills

| Skill | Description | Requirements |
|-------|-------------|--------------|
| [detour](./detour/) | Spawn isolated exploration in a tmux side pane | tmux |
| [clean-research-report](./clean-research-report/) | Strip citation artifacts from ChatGPT deep research markdown exports | Python 3.12+, uv |

## Installation

Each skill has its own installation instructions. Generally, you'll copy files to your `~/.claude/` directory:

```bash
# Example: Install detour skill
cp -r detour/commands/* ~/.claude/commands/
cp -r detour/scripts/* ~/.claude/scripts/
cp -r detour/agents/* ~/.claude/agents/
```

## Structure

Skills use one of two Claude Code extension mechanisms:

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
