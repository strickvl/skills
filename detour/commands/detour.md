---
description: Spawn detour in tmux side pane
allowed-tools:
  - Bash
  - Write
argument-hint: "<question>"
---

Before spawning the detour, analyze the question and provide context.

## Your Task

1. **Assess relevance**: Is "$ARGUMENTS" related to what we've been working on in this session?

2. **Write context file**: Create a unique file at `/tmp/detour-context-{unique_id}.md` where `{unique_id}` is the current epoch timestamp (e.g., `1736592000`). Write a brief (3-5 line) summary:
   - If RELATED: Describe what we were doing, mention specific files/components involved
   - If UNRELATED: Note it's a separate exploration, but mention current session focus for background

3. **Spawn the detour**: Run the script with the context file path you just created
   ```bash
   bash .claude/scripts/detour.sh spawn "$ARGUMENTS" /tmp/detour-context-{unique_id}.md
   ```

## Context Template

```markdown
## Session Context

[What we were working on - 1-2 sentences]

**Relevance to question**: [Related/Unrelated/Partially related]

**Key files** (if related): [list 2-4 files, or "N/A"]
```

Now analyze and spawn.
