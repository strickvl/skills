# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

A collection of reusable skills and sub-agents for Claude Code. Skills here extend Claude Code's capabilities through slash commands, bash scripts, and specialized sub-agents.

## Architecture

Skills follow a three-component pattern that maps to Claude Code's extension system:

```
skill-name/
├── commands/*.md    → Slash commands (copied to ~/.claude/commands/)
├── scripts/*.sh     → Bash executables (copied to ~/.claude/scripts/)
└── agents/*.md      → Sub-agent definitions (copied to ~/.claude/agents/)
```

**Flow for the `detour` skill:**
1. User runs `/detour <question>` → triggers `commands/detour.md`
2. Command writes session context to `/tmp/detour-context-*.md`
3. Command invokes `scripts/detour.sh` with the context file path
4. Script spawns a tmux side pane running `claude --agent detour-investigator`
5. Script injects the prompt + context bundle into the spawned pane

## Installation (for users)

Skills are installed by copying files to the user's `~/.claude/` directory. Each skill's README has specific instructions.

## Key Implementation Details

**Detour timing parameters** (`scripts/detour.sh`):
- `sleep 7.0` after spawning Claude (wait for full initialization)
- `sleep 1.5` after pasting prompt (buffer for large context)
- These may need adjustment based on system performance

**Detour agent configuration** (`agents/detour-investigator.md`):
- Uses `haiku` model for speed
- Limited to read-only tools: Read, Grep, Glob, Bash
- Outputs structured format: Findings → Recommendation → Risks → Files → Follow-ups

**Temp files created by detour:**
- Session context: `/tmp/detour-context-{timestamp}-{pid}.md`
- Context bundle: `/tmp/claude-detour-context.XXXXXX.md`
