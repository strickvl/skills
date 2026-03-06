# Claude 4.6 Opus Prompting Patterns

Patterns optimized for Claude 4.6 Opus's deep reasoning capabilities, based on
Anthropic's official prompting best practices (platform.claude.com/docs).

## Key Characteristics

- **Precise instruction following**: Does exactly what you ask — be explicit
- **Context-aware**: Exceptional at tracking state across long contexts
- **Adaptive thinking**: Dynamically decides when and how much to think (replaces manual budget_tokens)
- **More concise by default**: Even more direct than Claude 4.5 — request depth explicitly
- **Strong subagent orchestration**: Can delegate subtasks to specialized agents
- **Long-horizon reasoning**: Maintains orientation across extended sessions and multiple context windows

## Critical Principle: Be Explicit About Depth

Claude 4.6 is more concise than previous models. For research tasks, you MUST explicitly
request comprehensive output. Without it, you'll get efficient but shallow answers.

**Less effective:** "Research X"
**More effective:** "Research X comprehensively. Include as many relevant details as possible. Go beyond the basics to provide a fully-featured, thorough analysis."

```xml
<approach>
Provide comprehensive analysis. Where information supports multiple
interpretations, explore each. Anticipate follow-up questions and
address them proactively. Do not prioritize brevity over thoroughness.
</approach>
```

## Recommended Prompt Structure

XML tags work well for complex research prompts. Claude 4.6 parses them unambiguously:

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
[How to conduct the analysis: methodology, perspectives to consider]
</approach>

<output_format>
[Structure, length, sections]
</output_format>
```

## Adaptive Thinking and Effort

Claude 4.6 uses adaptive thinking — it dynamically decides when and how deeply to reason.
The `effort` parameter controls this:

- **low**: Latency-sensitive, simpler queries
- **medium**: General use — good default for most research
- **high**: Complex multi-step reasoning, deep research synthesis
- **max**: Hardest problems — large-scale analysis, extended autonomous work

For deep research prompts, guide the thinking behavior:

```xml
<reasoning_instructions>
This is a complex research question requiring deep analysis. Take time to:
1. Break down the question into component parts
2. Consider multiple perspectives and interpretations
3. Develop competing hypotheses and track confidence levels
4. Identify key uncertainties and how they affect conclusions
5. Structure your analysis before presenting findings
</reasoning_instructions>
```

You can also steer thinking with explicit instructions:

```xml
<thinking_guidance>
After gathering information, carefully reflect on its quality and determine
optimal next steps before proceeding. Use your reasoning to plan and iterate
based on new information, then take the best next action.
</thinking_guidance>
```

## Context and Motivation

Providing context improves performance significantly. Explain WHY you need something:

**Less effective:** "Never use bullet points"
**More effective:** "Present analysis in flowing prose paragraphs. This research will be incorporated into a formal report where bullet points would disrupt readability."

## Verbosity and Depth Control

Claude 4.6 tends toward efficiency. For research tasks, explicitly request depth:

```xml
<depth_instructions>
Provide comprehensive, detailed analysis. Do not prioritize brevity.
- Cover all relevant aspects thoroughly
- Include supporting reasoning for conclusions
- Explore nuances and edge cases
- Address potential counterarguments or alternative interpretations
- Go beyond surface-level to provide fully-featured coverage
</depth_instructions>
```

## Long Context Handling

When providing large documents or multi-source inputs (20K+ tokens):

1. **Put long documents at the top** of the prompt, above your query and instructions
2. **Place instructions at the end** — this can improve response quality by up to 30%
3. **Use document tags** for multi-source research:

```xml
<documents>
  <document index="1">
    <source>source_name.pdf</source>
    <document_content>
      [content here]
    </document_content>
  </document>
</documents>

Based on the information above:

<task>
[Your research question here]
</task>
```

4. **Ground responses in quotes**: Ask Claude to quote relevant parts before synthesizing

## Structured Research Approach

For complex research, use a structured approach with competing hypotheses:

```xml
<research_approach>
Search for this information in a structured way:
- Develop several competing hypotheses as you gather data
- Track your confidence levels to improve calibration
- Regularly self-critique your approach and plan
- Break down complex sub-questions systematically
- Synthesize across sources rather than summarizing each independently
</research_approach>
```

## Self-Verification

Claude 4.6 benefits from explicit self-check instructions:

```xml
<verification>
Before finalizing your response:
1. Did I address all parts of the question?
2. Are my claims supported by the provided context?
3. Have I noted areas of uncertainty appropriately?
4. Does the output match the requested format and depth?
Before you finish, verify your answer against the success criteria stated in the task.
</verification>
```

## Handling Uncertainty

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

## Output Format Control

Be specific about structure. Claude 4.6 responds well to format specifications:

```xml
<output_format>
Structure your response as:

1. **Executive Summary** (2-3 paragraphs)
   - Key findings
   - Main conclusions
   - Critical uncertainties

2. **Detailed Analysis**
   - Organize by theme, not by source
   - Use prose paragraphs for analysis
   - Include specific evidence for claims

3. **Synthesis**
   - How findings connect
   - Implications and significance

4. **Limitations**
   - What this analysis cannot determine
   - Areas requiring further research

Write in clear, flowing prose. Reserve bullet points for genuinely discrete
items. Target comprehensive coverage over arbitrary length limits.
</output_format>
```

## Example Deep Research Prompt

```xml
<role>
You are an expert research analyst. Provide thorough, well-reasoned analysis
that examines questions from multiple angles and acknowledges complexity.
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
</scope>

<approach>
- Examine multiple perspectives, including contrarian views
- Develop competing hypotheses and track confidence levels
- Distinguish between established consensus and ongoing debate
- Support conclusions with explicit reasoning
- Identify key uncertainties and their implications
- Be comprehensive — do not prioritize brevity over thoroughness
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

<depth_instructions>
Provide comprehensive, detailed analysis. Go beyond surface-level overview.
Include as many relevant details as possible. Do not sacrifice depth for brevity.
</depth_instructions>
```

## Things to Avoid

- Assuming Claude will "go above and beyond" without being asked — request it explicitly
- Vague instructions that require interpretation
- Conflicting constraints (resolve contradictions in the prompt)
- Over-complicated nested instructions that obscure the core task
- Aggressive tool-use language from older prompts ("CRITICAL: ALWAYS use...") — Claude 4.6 may overtrigger
- Using prefilled assistant turns (deprecated in Claude 4.6)
- Expecting verbose output without explicitly requesting depth
