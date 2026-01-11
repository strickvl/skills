# Claude Code Skills & Agents

A collection of reusable skills and sub-agents for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

**Use at your own risk.** These are personal productivity tools that may require specific setups or configurations.

## Available Skills

| Skill | Description | Requirements |
|-------|-------------|--------------|
| [detour](./detour/) | Spawn isolated exploration in a tmux side pane | tmux |

## Installation

Each skill has its own installation instructions. Generally, you'll copy files to your `~/.claude/` directory:

```bash
# Example: Install detour skill
cp -r detour/commands/* ~/.claude/commands/
cp -r detour/scripts/* ~/.claude/scripts/
cp -r detour/agents/* ~/.claude/agents/
```

## Structure

Skills in this repo follow this structure:

```
skill-name/
├── README.md           # Skill documentation
├── commands/           # Slash commands (*.md)
├── scripts/            # Bash scripts
├── agents/             # Sub-agent definitions
└── skills/             # Skill definitions (if any)
```

## Contributing

Feel free to fork and adapt for your own use. PRs welcome for improvements.

## License

MIT
