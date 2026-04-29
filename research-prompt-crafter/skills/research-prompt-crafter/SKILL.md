---
name: research-prompt-crafter
description: >-
  Craft high-quality prompts for deep research models (GPT-5.5, Gemini 3 Pro,
  Claude 4.6 Opus, DeepSeek). Use when user wants to create a prompt for a research
  task that will run on a "thinking" model taking 5-20+ minutes. Triggers: "help me
  write a prompt", "craft a research prompt", "I need a prompt for deep research",
  "prompt for GPT-5.5", "prompt for Gemini", "write a prompt that will take a while
  to run", or any request to create prompts for long-running AI research tasks.
---

# Research Prompt Crafter

Create prompts optimized for deep research models—the kind where you send a prompt and wait 5-20+ minutes for a comprehensive response. Getting the prompt right matters when compute time is significant.

## Environment Detection

**Claude Code**: Use `Ask User Question` tool for iterative refinement. Save output as `.md` file.
**Claude Desktop / claude.ai**: Use conversation for refinement. Save output as markdown artifact.

## Workflow

```
- [ ] Step 1: Confirm target model
- [ ] Step 2: Gather brain dump
- [ ] Step 3: Clarify ambiguities (iterative)
- [ ] Step 4: Propose structure & confirm
- [ ] Step 5: Generate final prompt
- [ ] Step 6: Save output
```

### Step 1: Confirm Target Model

Ask the user which model the prompt will run on:

- **GPT-5.5** → See [gpt-5-5-patterns.md](gpt-5-5-patterns.md)
- **Gemini 3 Pro** → See [gemini-3-patterns.md](gemini-3-patterns.md)
- **Claude 4.6 Opus** → See [claude-4-6-patterns.md](claude-4-6-patterns.md)
- **Generic (multi-model)** → Use common patterns that work across models
- **DeepSeek** → Use generic patterns (specific guide pending)

Load the relevant reference file before proceeding.

### Step 2: Gather Brain Dump

Ask the user to provide their rough/unstructured input. Prompt for:

- **Topic/question**: What research question or topic?
- **Scope**: How broad or narrow? Any boundaries?
- **Depth**: Surface overview or exhaustive deep-dive?
- **Output format**: Report structure, length expectations, sections needed?
- **Audience**: Who will read this? Technical level?
- **Sources/constraints**: Preferred sources? Things to avoid? Time bounds?
- **Success criteria**: What makes a good answer?

Accept messy input—that's the point. User shouldn't need to structure this themselves.

### Step 3: Clarify Ambiguities (Iterative)

Review the brain dump for:

1. **Contradictions**: Conflicting requirements (e.g., "brief but comprehensive")
2. **Vague terms**: Undefined scope words ("recent", "major", "key")
3. **Missing constraints**: Unstated assumptions about length, format, depth
4. **Implicit requirements**: Things user probably wants but didn't say

Use `Ask User Question` (Claude Code) or direct questions to resolve each issue. Ask 1-3 focused questions per round. Continue until requirements are clear.

Example clarifications:
- "You mentioned 'recent developments'—what time range? Last 6 months? Year? 5 years?"
- "You want both breadth and depth—if forced to choose, which matters more?"
- "Should the output include citations/sources, or just synthesized findings?"

### Step 4: Propose Structure & Confirm

Based on gathered requirements, propose:

1. **Prompt structure**: What sections/blocks the prompt will have
2. **Key instructions**: Main behavioral directives for the model
3. **Output specification**: What the model should produce
4. **Constraints**: What to avoid, length limits, format rules

Present this as a brief outline and ask for confirmation or adjustments. This catches misunderstandings before writing the full prompt.

### Step 5: Generate Final Prompt

Apply model-specific patterns from the reference files:

**Common elements across models:**
- Clear role/persona (if needed)
- Explicit task description
- Constraints and boundaries
- Output format specification
- Quality criteria

**Use XML structure** for complex prompts—all three major models handle XML well:

```xml
<role>...</role>
<context>...</context>
<task>...</task>
<constraints>...</constraints>
<output_format>...</output_format>
```

**Include current date** at the top of the prompt for time-sensitive research, *except for GPT-5.5*, which is already aware of the current UTC date — adding it just adds noise (only inject a date there for non-UTC, business, or "as-of" anchoring).

### Step 6: Save Output

**Filename format**: `{topic-slug}-{model}-prompt.md`  
Examples: `ai-regulation-gpt55-prompt.md`, `market-analysis-gemini3-prompt.md`

**Claude Code locations** (check in order):
1. `design/` folder if it exists
2. Repository root otherwise

**Claude Desktop**: Create as markdown artifact.

## Quality Checklist

Before finalizing, verify:

- [ ] Task is unambiguous—model won't need to guess intent
- [ ] Scope is explicit—clear boundaries on what to include/exclude
- [ ] Output format is specified—structure, length, sections
- [ ] Constraints are stated—what NOT to do
- [ ] Success criteria defined—what makes a good response
- [ ] Model-specific patterns applied from reference file

## Anti-Patterns to Avoid

- **Vague scope**: "Tell me about X" without boundaries
- **Contradictory instructions**: "Be brief but cover everything"
- **Missing format spec**: No guidance on structure/length
- **Assumed context**: Referencing things the model won't know
- **Over-instruction**: So many rules the model gets confused
