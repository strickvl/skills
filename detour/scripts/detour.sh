#!/usr/bin/env bash
set -euo pipefail

# Detour spawner - creates tmux side pane with fresh Claude + context

PANE_ID_FILE="/tmp/claude-detour-pane-id"

require_tmux() {
    if [ -z "${TMUX:-}" ]; then
        echo "ERROR: Detour requires tmux" >&2
        exit 1
    fi
}

detect_context_root() {
    if [ -n "${CLAUDE_PROJECT_DIR:-}" ]; then
        echo "$CLAUDE_PROJECT_DIR"
    elif git rev-parse --show-toplevel 2>/dev/null; then
        return 0
    else
        pwd
    fi
}

get_existing_pane_id() {
    if [ -f "$PANE_ID_FILE" ]; then
        local pane_id
        pane_id=$(cat "$PANE_ID_FILE" 2>/dev/null || echo "")
        if [ -n "$pane_id" ]; then
            if tmux display-message -t "$pane_id" -p "#{pane_id}" 2>/dev/null | grep -q "^${pane_id}$"; then
                echo "$pane_id"
                return 0
            fi
        fi
    fi
    return 1
}

save_pane_id() {
    echo "$1" > "$PANE_ID_FILE"
}

create_new_pane() {
    local command="$1"
    local width="${2:-50}"
    local pane_id
    pane_id=$(tmux split-window -h -p "$width" -P -F "#{pane_id}" "$command")
    save_pane_id "$pane_id"
    echo "$pane_id"
}

reuse_pane() {
    local pane_id="$1"
    local command="$2"
    tmux send-keys -t "$pane_id" C-c 2>/dev/null || return 1
    sleep 0.15
    tmux send-keys -t "$pane_id" "clear && $command" Enter
}

create_context_bundle() {
    local question="$1"
    local root="$2"
    local session_context_file="${3:-}"
    # Use mktemp for secure, unique temp file creation
    local bundle_path
    bundle_path="$(mktemp "/tmp/claude-detour-context.XXXXXX.md")"

    # Read session context if provided
    local session_context=""
    if [ -n "$session_context_file" ] && [ -f "$session_context_file" ]; then
        session_context=$(cat "$session_context_file")
    fi

    cat > "$bundle_path" <<BUNDLE
# Detour Context Bundle

**Generated:** $(date -u +"%Y-%m-%d %H:%M:%S UTC")
**Question:** $question
**Root:** $root

$(if [ -n "$session_context" ]; then echo "$session_context"; else echo "## Session Context

_No session context provided - this is a standalone exploration._"; fi)

## Git Status
\`\`\`
$(cd "$root" && git status --porcelain 2>/dev/null || echo "Not a git repo")
\`\`\`

## Recent Commits
\`\`\`
$(cd "$root" && git log -n 5 --oneline 2>/dev/null || echo "No commits")
\`\`\`

## Recent Changes
\`\`\`
$(cd "$root" && git diff --stat 2>/dev/null || echo "No changes")
\`\`\`
BUNDLE

    echo "$bundle_path"
}

send_bootstrap_message() {
    local pane_id="$1"
    local bundle_path="$2"
    local question="$3"

    # Wait for Claude to fully start and be ready for input
    # Claude Code initialization can take 5-7 seconds (loading agents, MCP servers, etc)
    sleep 7.0

    # Read context bundle content
    local context_content
    context_content=$(cat "$bundle_path")

    # Type the prompt with embedded context (agent is already set via --agent flag)
    tmux send-keys -t "$pane_id" "Context:

$context_content

Question: $question"

    # Wait for prompt to fully paste (large context can take a moment)
    sleep 1.5

    # Submit with Enter (as separate command)
    tmux send-keys -t "$pane_id" Enter
}

spawn_detour() {
    local question="$1"
    local session_context_file="${2:-}"
    local width="${3:-50}"

    require_tmux

    local root=$(detect_context_root)
    local bundle_path=$(create_context_bundle "$question" "$root" "$session_context_file")
    
    echo "📍 Context root: $root" >&2
    if [ -n "$session_context_file" ] && [ -f "$session_context_file" ]; then
        echo "📝 Session context: $session_context_file" >&2
    fi
    echo "📦 Bundle: $bundle_path" >&2

    # Shell-escape the root path to handle paths with special characters
    local quoted_root
    quoted_root="$(printf '%q' "$root")"
    local claude_cmd="cd -- $quoted_root && claude --agent detour-investigator"
    local pane_id

    if pane_id=$(get_existing_pane_id); then
        echo "♻️  Reusing pane: $pane_id" >&2
        reuse_pane "$pane_id" "$claude_cmd"
    else
        echo "🆕 Creating pane..." >&2
        pane_id=$(create_new_pane "$claude_cmd" "$width")
    fi

    echo "💬 Injecting prompt..." >&2
    send_bootstrap_message "$pane_id" "$bundle_path" "$question"
    
    echo "✅ Detour spawned in pane $pane_id" >&2
}

# Main
case "${1:-}" in
    spawn)
        shift
        spawn_detour "$@"
        ;;
    *)
        echo "Usage: detour.sh spawn <question> [session_context_file] [width]" >&2
        exit 1
        ;;
esac
