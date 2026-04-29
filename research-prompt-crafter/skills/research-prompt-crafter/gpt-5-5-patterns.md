# GPT-5.5 Prompting Patterns

Patterns optimized for GPT-5.5's deep research and agentic capabilities, based on
OpenAI's official prompt guidance
(developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5).

## Key Characteristics

- **More efficient reasoning**: Reaches strong results with fewer reasoning tokens than 5.4, even at the same effort level
- **Outcome-first execution**: Performs best when given a clear goal + success criteria rather than step-by-step process guidance
- **Stronger, more precise tool use**: Better tool selection and argument accuracy on large tool surfaces and long-running agent workflows
- **Literal instruction following**: Interprets prompts thoroughly — define stopping rules and success criteria explicitly
- **Polished but direct default tone**: Often warmer and more readable with less scaffolding; can feel terse without explicit personality guidance
- **Default reasoning effort is `medium`**: Re-evaluate `low` and `medium` before escalating

## Migrating from 5.4 (or older) prompts

Don't carry every instruction over. Legacy prompts often over-specify the *process*
because earlier models needed more help staying on track. With 5.5, that adds noise
and narrows the model's search space.

| Old 5.4-era pattern | Rework for 5.5 |
|---|---|
| Rigid output contracts with `ALWAYS`/`NEVER` | Success criteria + stopping rules; reserve absolutes for true invariants |
| Hardcoded multi-pass research mode | Retrieval budget — let the model choose path |
| Inject the current date in the prompt | Drop it; 5.5 is aware of current UTC date |
| Describe the output schema in the prompt | Use [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) where supported |
| Reasoning effort `none` as default | Start at `medium` (default) or `low` |

Start migrations from a fresh baseline that captures the product contract, then add
detail only where evals show it changes behavior.

## Recommended Prompt Structure

GPT-5.5 still responds well to XML-style section tags for complex prompts. Keep each
section short. The shape below is a starting point — drop sections that don't change
behavior for your task.

```xml
<role>
You are a [domain] research specialist. Your job is to produce a comprehensive,
well-grounded answer to the goal below.
</role>

<goal>
[Outcome the user wants, in plain language.]
</goal>

<success_criteria>
- [What must be true before the final answer]
- [Required coverage]
- [Evidence rules]
</success_criteria>

<constraints>
- [Scope, time bounds, sources, what to exclude]
- [Allowed and disallowed side effects]
</constraints>

<stopping_rules>
- [When to stop searching / iterating]
- [What to do when evidence is insufficient]
</stopping_rules>

<output>
- [Sections, length, tone]
- [Format: Markdown / JSON / prose]
</output>
```

## Outcome-First Goals and Success Criteria

The single most impactful 5.5 pattern. Describe the destination, not every step.

```xml
<goal>
Resolve the user's research question end to end and produce a decision-grade brief.
</goal>

<success_criteria>
- The core question is answered with a defensible recommendation
- Each material claim is grounded in a cited source
- Trade-offs and contradicting evidence are surfaced, not hidden
- Uncertainty is named where it exists
- Output matches the requested structure and length budget
</success_criteria>
```

Avoid this style unless every step is genuinely required:

```text
First inspect A, then inspect B, then compare every field, then think through
all possible exceptions, then decide which tool to call, then call the tool,
then explain the entire process to the user.
```

## Avoid Unnecessary Absolute Rules

Use `must`, `never`, `always`, and `only` for true invariants — safety, required
output fields, actions that must not happen. For judgment calls (when to search
again, when to ask, when to keep iterating), prefer decision rules instead.

```xml
<decision_rules>
- Search again only when a required fact, owner, date, ID, or source is missing
- Ask the user only when a missing detail would materially change the answer
- Stop when further searching is unlikely to improve the conclusion
</decision_rules>
```

## Stopping Conditions and Retrieval Budgets

Without explicit stopping rules, 5.5's literal instruction following can lead to
over-searching. Give it a budget.

```xml
<retrieval_budget>
Start with one broad search using short, discriminative keywords. If the top
results contain enough citable support for the core request, answer from those
results instead of searching again.

Make another retrieval call only when:
- The top results do not answer the core question
- A required fact, parameter, owner, date, ID, or source is missing
- The user asked for exhaustive coverage, a comparison, or a comprehensive list
- A specific document, URL, or record must be read
- The answer would otherwise contain an important unsupported factual claim

Do not search again to improve phrasing, add nonessential examples, or support
wording that can safely be made more generic.
</retrieval_budget>
```

For research that synthesizes across many documents, set a coverage budget too:
"cover at minimum N distinct sources" or "stop after diminishing returns on three
consecutive searches."

## Citation and Grounding Rules

5.5 has strong citation discipline when instructed explicitly. Absence of evidence
shouldn't automatically become a factual "no."

```xml
<citation_rules>
- Cite only sources retrieved in the current workflow
- Never fabricate citations, URLs, IDs, or quote spans
- Attach citations to specific claims, not only at the end
- Base factual claims only on provided context or tool outputs
- Surface conflicting sources explicitly with attribution to each
- Narrow the answer or acknowledge insufficient evidence rather than guessing
- Label inferences distinctly from established facts
</citation_rules>
```

## Creative Drafting Guardrails

When the research output includes generative or persuasive prose (executive
summaries, leadership briefs, talk tracks, narrative framing), separate
source-backed claims from creative wording so the model doesn't invent specifics
to make the draft sound stronger.

```xml
<creative_guardrails>
- Use retrieved or provided facts for concrete product, customer, metric,
  date, or capability claims, and cite them
- Do not invent specific names, first-party data, metrics, outcomes, or
  capabilities to strengthen the draft
- If support is thin, write a useful generic draft with placeholders or
  clearly labeled assumptions rather than unsupported specifics
</creative_guardrails>
```

## Verification Loop

5.5 still benefits from an explicit self-check before finalizing.

```xml
<verification>
Before finalizing your response, confirm:
1. Correctness — does the output meet every success criterion?
2. Grounding — are factual claims backed by cited evidence?
3. Formatting — does the output match the requested structure?
4. Completeness — has the goal been fully addressed, or are blockers named?
</verification>
```

## Reasoning Effort Guidance

5.5 supports `reasoning.effort`: `none`, `low`, `medium` (default), `high`, `xhigh`.

Treat reasoning effort as a *last-mile* knob. Better outcomes usually come from
clearer success criteria, stopping rules, and verification — not from raising effort.

| Effort | When to use |
|---|---|
| `none` | Latency-critical tasks with no real reasoning need: simple lookups, classification, voice turns |
| `low` | Most execution tasks; works well for many production workflows |
| `medium` | **Default**. Balanced point for tool use, planning, and synthesis |
| `high` | Complex agentic tasks where evals show measurable lift and latency is acceptable |
| `xhigh` | Hardest async tasks or evals testing the bounds of model intelligence |

Higher effort is not automatically better. With weak stopping criteria or
open-ended tool access, higher effort can cause overthinking and over-searching.
Increase effort only when evals show a measurable quality gain.

## Output Verbosity

GPT-5.5's default style is concise and direct. Use `text.verbosity` (`low`,
`medium`, `high`) deliberately rather than relying on prompt scaffolding to
expand or contract length. On 5.5, `low` produces proportionally more concise
responses than `low` did on 5.4.

For research outputs you usually want longer prose, so use `medium` or `high`
verbosity and constrain length explicitly:

```xml
<output>
- Target ~2,500-4,000 words
- Lead with a 2-3 paragraph executive summary
- Use prose paragraphs for analysis; use bullets only for genuinely discrete items
- Include section headers
</output>
```

## Formatting

Let formatting serve comprehension. Use plain paragraphs as the default. Reach
for headers, bold, and bullets when the content needs comparison, ranking, or
scanability.

```xml
<formatting>
- Use plain paragraphs as the default for explanation and synthesis
- Use headers for navigable sections
- Reserve bullets for genuinely discrete items, not for prose-shaped content
- Keep lists flat (single level); use sub-sections for hierarchy
- Use `1.` `2.` `3.` style numbering, not `1)`
</formatting>
```

## Long-Context Handling

5.5 retains 5.4's strength on long-context analysis.

```xml
<long_context>
- Produce an internal outline of key themes before synthesizing
- Re-state the core question and constraints before answering
- Anchor claims to specific reasoning or sources
- Quote or paraphrase when the answer hinges on specific details
- For multi-document inputs, synthesize across documents rather than summarizing each
</long_context>
```

## Date Handling

5.5 is aware of the current date in UTC. Do **not** inject the date into the
prompt by default. Add explicit date or timezone context only when the
application needs:

- A business-specific timezone
- A policy-effective date
- A user-local date or non-UTC reference point
- A historical "as of" date for time-bounded research

## Phase Parameter (Tool-Heavy Workflows)

If the research workflow includes tool calls and you manually replay assistant
output items into the next request (rather than using `previous_response_id`),
preserve each item's `phase` value and pass it back unchanged. This matters most
when responses include preambles, repeated tool calls, or a final answer after
intermediate updates.

```text
If manually replaying assistant items:
- Preserve assistant `phase` values exactly
- Use `phase: "commentary"` for intermediate user-visible updates
- Use `phase: "final_answer"` for the completed answer
- Do not add `phase` to user messages
```

For most one-shot deep-research prompts (no tool replay), this section can be
omitted from the prompt itself.

## Personality (Optional)

Most deep research prompts don't need a personality block — the model's default
direct, polished tone works well for analytical output. Add a short personality
block only if the audience or product surface needs explicit warmth, point of
view, or a particular register.

```xml
<personality>
You are a steady, candid analyst. Be direct without being curt. State a clear
recommendation when you have enough context, name important trade-offs, and
acknowledge uncertainty without becoming evasive.
</personality>
```

## Example Deep Research Prompt

```xml
<role>
You are an expert research analyst specializing in [domain]. You produce
decision-grade briefs grounded in evidence and careful reasoning.
</role>

<goal>
Research and analyze [specific question/topic] and produce a brief that helps
[audience] decide [decision].
</goal>

<success_criteria>
- The core question is answered with a defensible recommendation
- All material claims are grounded in cited sources
- Trade-offs and contradicting evidence are surfaced, not hidden
- Uncertainty and gaps are named explicitly
- Output matches the requested structure and length
</success_criteria>

<constraints>
- Focus on [time period / scope]
- Exclude [out-of-scope topics]
- Prioritize [authoritative sources / primary research / etc.]
</constraints>

<retrieval_budget>
Start with one broad search using discriminative keywords. Search again only
when a required fact, source, or specific document is missing, or when the
answer would otherwise contain an important unsupported claim. Do not search
to polish phrasing or add nonessential examples.
</retrieval_budget>

<citation_rules>
- Cite only sources retrieved in this workflow
- Never fabricate citations, URLs, IDs, or quotes
- Attach citations to specific claims, not only at the end
- Label inferences distinctly from established facts
- Surface conflicting sources explicitly
</citation_rules>

<verification>
Before finalizing, confirm:
1. Every success criterion is met
2. Factual claims are backed by cited evidence
3. Output matches the requested format
4. Gaps and uncertainties are named
</verification>

<output>
Structure your response as:
1. Executive Summary (2-3 paragraphs, lead with the recommendation)
2. [Section 1 title]
3. [Section 2 title]
4. [Section 3 title]
5. Key Uncertainties and Limitations
6. Conclusions

Format: Markdown with section headers.
Use prose paragraphs for analysis. Reserve bullets for genuinely discrete items.
Target ~2,500-4,000 words.
</output>
```

## Things to Avoid

- Vague goals that require guessing at intent ("tell me about X")
- Contradictory constraints ("brief but comprehensive")
- Process-heavy step-by-step instructions when only the outcome matters
- Blanket `ALWAYS`/`NEVER` rules for judgment calls — reserve absolutes for invariants
- Injecting the current date when the model already knows it
- Describing output schemas in the prompt instead of using Structured Outputs
- Jumping to `xhigh` reasoning effort before optimizing the prompt itself
- Skipping a retrieval budget on search-heavy tasks (causes over-searching)
