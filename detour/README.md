# Detour

Spawn isolated Claude explorations in a tmux side pane without polluting your main conversation context.

## What It Does

When you're deep in a coding session and want to explore a tangential question, `/detour` spawns a fresh Claude instance in a side pane. This gives you:

- **Visual separation**: Side pane so you can see both conversations
- **Context isolation**: Exploration doesn't pollute main session history
- **Multi-turn conversation**: Full interactive Claude in the side pane
- **Session context**: Main Claude summarizes what you were working on for the detour

## Requirements

- **tmux**: Must be running inside a tmux session
- **Claude Code**: Installed and available as `claude` command

## Installation

```bash
# From the skills repo root:
mkdir -p ~/.claude/{commands,scripts,agents}
cp detour/commands/detour.md ~/.claude/commands/
cp detour/scripts/detour.sh ~/.claude/scripts/
cp detour/agents/detour-investigator.md ~/.claude/agents/

# Make script executable
chmod +x ~/.claude/scripts/detour.sh
```

## Usage

```
/detour <your question>
```

Examples:
```
/detour how does authentication work in this codebase?
/detour what's the difference between these two approaches?
/detour can you explain how the pipeline executor works?
```

## How It Works

1. **You run `/detour <question>`** in your main Claude session
2. **Main Claude analyzes** whether the question relates to current work
3. **Writes session context** to a temp file (what you were doing, relevant files)
4. **Spawns a tmux side pane** with a fresh Claude instance using `--agent detour-investigator`
5. **Injects the prompt** with context bundle (session context + git info)
6. **Detour Claude investigates** in read-only exploration mode

The detour agent is configured for exploration:
- Read-only by default (Bash, Read, Grep, Glob tools)
- Uses `haiku` model for faster responses
- Structured output format for findings

## Files

| File | Purpose |
|------|---------|
| `commands/detour.md` | Slash command - analyzes relevance, writes context, spawns pane |
| `scripts/detour.sh` | Bash spawner - creates pane, injects prompt with context |
| `agents/detour-investigator.md` | Sub-agent used in spawned pane - structured exploration |

## Configuration

In `scripts/detour.sh`:
- `sleep 7.0` - Claude startup wait time (increase if prompt appears before Claude is ready)
- `sleep 1.5` - Prompt paste buffer (increase for very large context bundles)
- `width="${3:-50}"` - Side pane width percentage

## Troubleshooting

**Prompt not submitting?**
- Increase the sleep times in `detour.sh`
- Check that tmux pane is receiving input (`tmux list-panes`)

**Pane not spawning?**
- Ensure you're inside a tmux session (`echo $TMUX` should show path)
- Check script is executable: `chmod +x ~/.claude/scripts/detour.sh`

**Context not loading?**
- Two temp files are created:
  - **Session context file** (`/tmp/detour-context-*.md`): Written by the slash command with session summary
  - **Context bundle** (`/tmp/claude-detour-context.*.md`): Created by the script, includes git info
- Check both files were created and contain expected content

## Privacy Note

Detour writes temporary markdown files to `/tmp` containing:
- Your question
- The detected project root path
- Optional session summary (what you were working on)
- `git status` output (filenames of changed files)
- Recent commits (`git log -n 5 --oneline`)
- `git diff --stat` output (filenames and change sizes)

These files remain on disk until manually deleted or system cleanup. If you're working in a sensitive or private repository, review or delete these files after use:

```bash
# View detour temp files
ls -la /tmp/detour-context-*.md /tmp/claude-detour-context.*.md 2>/dev/null

# Delete all detour temp files
rm -f /tmp/detour-context-*.md /tmp/claude-detour-context.*.md
```

## Acknowledgments

The idea of using tmux to spawn side panes for Claude explorations was inspired by [David Siegel's claude-canvas](https://github.com/dvdsgl/claude-canvas) project.
