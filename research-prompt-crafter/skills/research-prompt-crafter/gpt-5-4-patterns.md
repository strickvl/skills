# GPT-5.4 Prompting Patterns

Patterns optimized for GPT-5.4's deep research and agentic capabilities, based on
OpenAI's official prompt guidance (developers.openai.com/api/docs/guides/prompt-guidance).

## Key Characteristics

- **Strong personality/tone adherence**: Less drift over long answers than previous models
- **Agentic robustness**: Sticks with multi-step work, retries, and completes loops end-to-end
- **Evidence-rich synthesis**: Excels at long-context and multi-document workflows
- **Instruction adherence**: Thrives with modular, skill-based prompts and explicit contracts
- **Batched tool calling**: Can call tools in parallel while maintaining accuracy
- **Conservative by default**: Performs well at `none` reasoning effort for execution tasks

## Recommended Prompt Structure

Use XML-style tags for clear section separation. GPT-5.4 responds especially well to
**output contracts** — explicit specifications of what sections to produce, in what order,
with what format.

```xml
<role>
You are a [domain] research specialist. Your job is to deeply and thoroughly
research and provide comprehensive, well-structured answers grounded in
reliable reasoning.
</role>

<task>
[Clear statement of what to research/analyze]
</task>

<constraints>
[Explicit boundaries and rules]
</constraints>

<output_contract>
Produce exactly the following sections, in this order:
1. [Section name] — [format and length guidance]
2. [Section name] — [format and length guidance]
...
Do not repeat the user's request. Do not add unrequested sections.
Required format: [Markdown / JSON / prose]
</output_contract>
```

## Output Contracts

GPT-5.4's single most impactful pattern. Define an explicit contract for what the model
should produce:

```xml
<output_contract>
- Produce exactly the requested sections in the requested order
- Apply length limits only to the specified sections
- Required format: Markdown with section headers
- Do not repeat the user's request back
- Preserve all evidence and reasoning — do not sacrifice substance for brevity
</output_contract>
```

## Completeness Contract

For research tasks, tell the model to treat the task as incomplete until everything is
covered. This prevents premature stopping:

```xml
<completeness_contract>
- Treat this task as incomplete until all requested items are covered
- Maintain an internal checklist of required deliverables
- For lists or batches: determine expected scope, track processed items, confirm coverage
- Mark blocked items explicitly, stating what is missing
- Do not stop at the first plausible answer
</completeness_contract>
```

## Verification Loop

GPT-5.4 benefits from an explicit self-check step before finalizing:

```xml
<verification>
Before finalizing your response, check:
1. Correctness — does the output satisfy every requirement?
2. Grounding — are factual claims backed by provided context or tool outputs?
3. Formatting — does the output match the requested schema?
4. Completeness — have all requested items been covered?
</verification>
```

## Research Mode (3-Pass Approach)

For deep research tasks, GPT-5.4 performs best with a disciplined multi-pass approach:

```xml
<research_mode>
Use a 3-pass research approach:
1. PLAN: List 3-6 sub-questions that must be answered
2. RETRIEVE: Research each sub-question; follow 1-2 second-order leads per question
3. SYNTHESIZE: Resolve contradictions, write the final answer with citations

Stop only when further searching is unlikely to change your conclusions.
</research_mode>
```

## Citation and Grounding Rules

GPT-5.4 has strong citation discipline when instructed explicitly:

```xml
<citation_rules>
- Only cite sources retrieved in the current workflow
- Never fabricate citations, URLs, IDs, or quote spans
- Attach citations to specific claims, not only at the end
- Base claims only on provided context or tool outputs
- State conflicts explicitly with attribution to each source
- Narrow answers or acknowledge when context is insufficient
- Label inferences — do not present them as established facts
</citation_rules>
```

## Empty Result Recovery

Prevent the model from giving up too early on lookups:

```xml
<empty_result_recovery>
If a lookup returns empty, partial, or overly narrow results:
- Do not immediately conclude no results exist
- Try 1-2 fallback strategies (alternate wording, broader filters, prerequisite lookups)
- Only then report absence, stating what was attempted
</empty_result_recovery>
```

## Reasoning Effort Guidance

GPT-5.4 supports a `reasoning_effort` parameter. Treat it as a **last-mile knob**, not
the primary quality lever. Better prompts, clear output contracts, and verification loops
should come first.

Recommended starting points:
- **`none`**: Execution-heavy tasks — field extraction, triage, short structured transforms
- **`low`**: Latency-sensitive tasks where small thinking helps, especially with complex instructions
- **`medium`/`high`**: Research-heavy tasks — long-context synthesis, multi-document review, strategy
- **`xhigh`**: Avoid as default; only if evals show clear benefit for long agentic reasoning

**Before increasing reasoning effort**, first add: output contract, completeness contract,
verification loop, and tool persistence rules.

Migration notes:
- From GPT-5.2: Match current reasoning effort first, then tune
- From GPT-4.1 / GPT-4o: Start with `none`, increase only if evals regress

## Handling Ambiguity

```xml
<missing_context>
If required context is missing, do NOT guess.
- Prefer lookup tools when missing context is retrievable
- Ask clarifying questions only when information is not retrievable
- Label assumptions explicitly if proceeding without full context
- Choose reversible actions when operating with missing context
</missing_context>
```

## Long-Context Handling

GPT-5.4 excels at long-context analysis, especially with compaction for extended sessions:

```xml
<long_context>
- Produce an internal outline of key themes before synthesizing
- Re-state the core question/constraints before answering
- Anchor claims to specific reasoning or sources
- When the answer depends on specific details, quote or paraphrase them
- For multi-document inputs, synthesize across documents rather than summarizing each
</long_context>
```

## Default Follow-Through Policy

GPT-5.4 can be instructed to act autonomously on low-risk steps:

```xml
<follow_through>
If the user's intent is clear and the next step is reversible and low-risk, proceed
without asking. Only request permission for:
- Irreversible actions
- External side effects (sending, purchasing, deleting, production writes)
- Missing sensitive information or choices that materially change outcomes
</follow_through>
```

## Output Formatting

```xml
<formatting_rules>
- Use clear section headers for organization
- Include executive summary at top for long responses
- Never use nested bullets — keep lists flat (single level)
- Use separate lists or sections for hierarchy
- For numbered lists, use "1. 2. 3." style (period), never "1)"
- Use prose paragraphs for analysis and synthesis
- Include citations/references where applicable
</formatting_rules>
```

## Example Deep Research Prompt

```xml
<role>
You are an expert research analyst specializing in [domain]. Your role is to
provide comprehensive, well-reasoned analysis grounded in evidence and
careful reasoning.
</role>

<task>
Research and analyze [specific question/topic].

Key areas to cover:
1. [Area 1]
2. [Area 2]
3. [Area 3]
</task>

<constraints>
- Focus on [time period/scope]
- Exclude [out-of-scope topics]
- Prioritize [quality criteria]
- Note uncertainty where it exists
</constraints>

<research_mode>
Use a 3-pass approach:
1. PLAN: List 3-6 sub-questions to answer
2. RETRIEVE: Research each sub-question, follow 1-2 second-order leads
3. SYNTHESIZE: Resolve contradictions, write final answer with citations
Stop only when further searching is unlikely to change conclusions.
</research_mode>

<citation_rules>
- Only cite sources retrieved in the current workflow
- Never fabricate citations, URLs, IDs, or quote spans
- Attach citations to specific claims, not only at end of answer
- Label inferences distinctly from established facts
</citation_rules>

<completeness_contract>
Treat this task as incomplete until all requested areas are covered.
Mark any blocked items explicitly.
</completeness_contract>

<verification>
Before finalizing, check:
1. Does output satisfy every requirement?
2. Are factual claims backed by provided context?
3. Does output match the requested format?
4. Have all requested items been covered?
</verification>

<output_contract>
Structure your response as:
1. Executive Summary (2-3 paragraphs)
2. [Section 1 title]
3. [Section 2 title]
4. [Section 3 title]
5. Key Uncertainties and Limitations
6. Conclusions

Required format: Markdown with section headers.
Use flowing prose for analysis. Reserve bullet points for genuinely discrete items.
Target comprehensive coverage over arbitrary length limits.
</output_contract>

<date>
Current date: [DATE]
</date>
```

## Things to Avoid

- Vague instructions that require guessing ("tell me about X")
- Contradictory constraints ("brief but comprehensive")
- Over-complicated nested instructions
- Assumed shared context the model doesn't have
- Jumping to `xhigh` reasoning effort before optimizing the prompt itself
- Skipping the completeness contract on batch/list tasks (causes premature stopping)
