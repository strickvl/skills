# Claude Opus 4.7 Prompting Patterns

Patterns optimized for Claude Opus 4.7's deep reasoning and long-horizon agentic
capabilities, based on Anthropic's official prompting best practices
(platform.claude.com/docs).

## Key Characteristics

- **Long-horizon reasoning**: Maintains orientation across extended sessions and multi-context-window workflows
- **Adaptive thinking**: Dynamically decides when and how much to think (replaces manual `budget_tokens`)
- **Literal instruction following**: Even more literal than 4.6 — won't silently generalize one instruction to other items
- **Response length calibrated to complexity**: Shorter answers on simple lookups, naturally longer on open-ended analysis
- **More direct, opinionated tone**: Less validation-forward and fewer emoji than 4.6 — re-evaluate style prompts
- **Strict respect for `effort`**: Low/medium effort genuinely means less work — risk of under-thinking on complex tasks at low effort
- **Fewer tools / fewer subagents by default**: Reasons more before reaching for tools; steerable through prompting

## Migrating from 4.6 (or earlier) prompts

Most 4.6 prompts work without changes. The patterns below are the ones most often
worth re-tuning.

| Old 4.6-era pattern | Rework for 4.7 |
|---|---|
| Heavy "MUST be comprehensive" scaffolding for depth | 4.7 calibrates length to task complexity — keep depth requests but soften the rhetoric |
| Default effort `medium` | Use `high` minimum for intelligence-sensitive research; consider `xhigh` for hard tasks |
| Implicit scope ("apply this style") | State scope explicitly ("apply this to every section, not just the first") |
| Aggressive "ALWAYS use \[tool\]" wording | 4.7 may overtrigger on imperatives — use normal phrasing |
| Forced status updates ("after every 3 tool calls, summarize") | 4.7 emits good user-facing updates on its own — remove scaffolding |
| Older filtering language ("only report important issues") | 4.7 follows filtering literally — say "report all findings, filter downstream" if you want coverage |

## Recommended Prompt Structure

XML tags continue to work well for complex research prompts.

```xml
<role>
You are a [domain] research specialist providing thorough, evidence-based analysis.
</role>

<task>
[Clear research question or objective]
</task>

<scope>
[Boundaries: what to include, what to exclude, time period, etc.]
</scope>

<approach>
[Methodology, perspectives to consider, hypothesis tracking]
</approach>

<output_format>
[Structure, length, tone]
</output_format>
```

## Effort Levels (Updated for 4.7)

Claude Opus 4.7 introduces new effort levels and respects them more strictly than 4.6.
Treat effort as the primary lever for the intelligence/cost trade-off.

| Effort | When to use |
|---|---|
| `low` | Short, scoped tasks where intelligence isn't critical and latency matters. **Risks under-thinking on complex problems.** |
| `medium` | Cost-sensitive workloads where you can trade some intelligence for fewer tokens |
| `high` | **Recommended minimum for intelligence-sensitive use cases**, including most research |
| `xhigh` (new) | Best setting for most coding and agentic use cases; strong fit for hard research |
| `max` (new) | Hardest, intelligence-demanding tasks. Can deliver gains, but may show diminishing returns and is sometimes prone to overthinking. Test it. |

For deep research:

- Start at `high` for most prompts.
- Move to `xhigh` for long-horizon synthesis or when the eval shows lift.
- Reserve `max` for the hardest problems and validate against your evals.
- If running at `max` or `xhigh`, set a generous `max_tokens` (e.g. 64k) so the model has room to think and act.

If you observe shallow reasoning on a complex task, raise effort first — don't try to
prompt around it. If you must keep effort low for latency, add targeted reasoning
guidance:

```text
This task involves multi-step reasoning. Think carefully through the problem before responding.
```

## Literal Instruction Following

4.7 reads prompts more literally than 4.6 and will not silently generalize from one
instance to others. State scope explicitly.

```xml
<scope>
- Apply the formatting guidance to every section, not just the first
- Cite every factual claim, not only contested ones
- Explore each competing hypothesis equally — do not stop after the first plausible answer
</scope>
```

If your prompt has a list of items and you want one rule applied to all of them, say
"all of them." 4.7 won't fill that in for you.

## Response Length and Verbosity

4.7 calibrates response length to perceived task complexity, so for open-ended research
it will tend to produce longer answers than 4.6 without prompting. You can still tune:

```xml
<output_format>
- Lead with a 2-3 paragraph executive summary
- Target ~3,000-5,000 words for the full analysis
- Use prose paragraphs for synthesis; bullets only for genuinely discrete items
- Reserve markdown headings for navigable sections
</output_format>
```

If responses are too verbose, *show* what concise looks like rather than just telling
the model "be concise" — positive examples outperform negative instructions.

## Adaptive Thinking

Adaptive thinking remains the recommended configuration. Use it to let the model
calibrate reasoning depth per turn.

```python
client.messages.create(
    model="claude-opus-4-7",
    max_tokens=64000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},  # or "xhigh" / "max"
    messages=[{"role": "user", "content": "..."}],
)
```

Guide the model to reflect after retrieving information:

```xml
<thinking_guidance>
After gathering information, reflect on its quality and decide on optimal next steps
before proceeding. Use your reasoning to plan and iterate based on new evidence,
then take the best next action.
</thinking_guidance>
```

If the model thinks more often than you'd like (common with large or complex system
prompts), steer it explicitly:

```text
Thinking adds latency and should only be used when it will meaningfully improve answer quality — typically for problems that require multi-step reasoning. When in doubt, respond directly.
```

## Tool Use and Subagents

4.7 uses tools and spawns subagents less aggressively than 4.6 by default. This usually
improves results, but if you specifically *want* more tool use or fan-out, either:

1. Raise effort (`high` or `xhigh` substantially increase tool use), or
2. Describe the desired pattern explicitly:

```xml
<tool_usage>
Use the [search tool] when a required fact, source, or specific document is missing
from your existing context. Spawn parallel subagents when fanning out across
independent items (e.g. reading multiple files, researching unrelated sub-questions).
Do not spawn a subagent for work you can complete directly in a single response.
</tool_usage>
```

## Long-Context Handling

When providing large documents or multi-source inputs (20K+ tokens):

1. **Put long documents at the top** of the prompt, above the query and instructions.
2. **Place instructions and the question at the end** — can improve quality by up to ~30%.
3. **Use `<document>` tags** for multi-source research:

```xml
<documents>
  <document index="1">
    <source>source_name.pdf</source>
    <document_content>
      [content]
    </document_content>
  </document>
</documents>

<task>
[Your research question]
</task>
```

4. **Ground responses in quotes** — ask the model to extract relevant quotes before synthesizing.

## Structured Research Approach

For complex research, prompt the model to track hypotheses and confidence:

```xml
<research_approach>
Search and synthesize in a structured way:
- Develop several competing hypotheses as you gather data
- Track your confidence levels to improve calibration
- Self-critique your approach and plan as evidence accumulates
- Break complex sub-questions down systematically
- Synthesize across sources rather than summarizing each independently
</research_approach>
```

## Self-Verification

```xml
<verification>
Before finalizing your response:
1. Did I address all parts of the question?
2. Are my claims supported by the provided context or cited sources?
3. Have I noted areas of uncertainty appropriately?
4. Does the output match the requested format and depth?
</verification>
```

## Uncertainty Handling

```xml
<uncertainty_handling>
- Distinguish clearly between established facts and inferences
- Note confidence levels where relevant
- Identify gaps in available information
- Don't fabricate specifics when uncertain — acknowledge limitations
- Use hedged language appropriately: "likely", "suggests", "based on available information"
- When sources conflict, state the conflict explicitly with attribution
</uncertainty_handling>
```

## Tone

4.7's default voice is more direct and opinionated than 4.6, with less validation-
forward phrasing and fewer emoji. For most analytical research output this is a good
fit. If you need a warmer or more conversational register, request it explicitly:

```xml
<tone>
Use a warm, collaborative tone. Acknowledge the user's framing before answering. Be candid but constructive when challenging assumptions.
</tone>
```

## Output Format Control

```xml
<output_format>
Structure your response as:

1. **Executive Summary** (2-3 paragraphs)
2. **Detailed Analysis** — organized by theme, not by source
3. **Synthesis** — how findings connect; implications
4. **Limitations** — what this analysis cannot determine

Write in clear, flowing prose. Reserve bullet points for genuinely discrete items.
Target comprehensive coverage over arbitrary length limits.
</output_format>
```

For format steering, prefer telling the model what to do rather than what *not* to do
("Write in flowing prose paragraphs" beats "Don't use markdown"). Matching your
prompt's own style to the desired output style also helps — markdown-heavy prompts
tend to produce markdown-heavy responses.

## Prefilled Responses

Prefilled assistant messages on the last turn are deprecated for Claude 4.6 and 4.7.
For research prompts this rarely matters, but if your old prompt used prefill to:

- **Force JSON/YAML output** → use [Structured Outputs](https://docs.claude.com/en/build-with-claude/structured-outputs) or ask the model to emit a specific schema
- **Skip preambles** → instruct directly: "Respond directly without preamble"
- **Continue an interrupted response** → put the continuation cue in a user turn

## Example Deep Research Prompt

```xml
<role>
You are an expert research analyst. Provide thorough, well-reasoned analysis that
examines questions from multiple angles and acknowledges complexity.
</role>

<task>
Research and analyze: [specific question]

This analysis should address:
1. [Key aspect 1]
2. [Key aspect 2]
3. [Key aspect 3]
</task>

<scope>
- Time period: [specify]
- Focus areas: [specify]
- Exclude: [what's out of scope]
- Apply this scope to every section, not just the first
</scope>

<approach>
- Examine multiple perspectives, including contrarian views
- Develop competing hypotheses and track confidence levels
- Distinguish between established consensus and ongoing debate
- Support every conclusion with explicit reasoning
- Identify key uncertainties and their implications
- Self-critique your findings before finalizing
</approach>

<output_format>
1. Executive Summary (3-4 paragraphs covering key findings)
2. Background and Context
3. Analysis
   - [Theme 1]
   - [Theme 2]
   - [Theme 3]
4. Synthesis and Implications
5. Uncertainties and Limitations
6. Conclusions

Use flowing prose paragraphs. Reserve lists for genuinely discrete items.
Current date: [DATE]
</output_format>

<verification>
Before finalizing, confirm:
1. All parts of the question are addressed
2. Factual claims are grounded in cited evidence or stated reasoning
3. Uncertainties are named, not hidden
4. Output matches the requested format
</verification>
```

Recommended runtime config: `effort: "high"` (or `xhigh` for hard problems),
`thinking: {type: "adaptive"}`, generous `max_tokens` (e.g. 64k).

## Things to Avoid

- Implicit scope — state explicitly which sections, items, or claims a rule applies to
- Aggressive imperative wording ("CRITICAL: ALWAYS use…") — 4.7 may overtrigger
- Forced periodic status updates — 4.7 paces user-facing updates well on its own
- Pushing for `low`/`medium` effort on intelligence-sensitive research and then prompting around shallow reasoning — raise effort instead
- Heavy "be comprehensive" scaffolding — 4.7 calibrates depth to task complexity, so keep depth requests but trim the volume of rhetoric
- Prefilled assistant turns on the last message (deprecated)
- Conflicting constraints (resolve contradictions in the prompt)
