# Gemini 3 Pro Prompting Patterns

Patterns optimized for Gemini 3 Pro's advanced reasoning capabilities.

## Key Characteristics

- **Direct and precise**: Responds best to clear, well-structured prompts
- **Structure-sensitive**: Benefits from consistent delimiters (XML or Markdown)
- **Context-position aware**: Place instructions AFTER long context blocks
- **Thinking-capable**: Can be prompted to plan/self-critique before answering

## Recommended Prompt Structure

Gemini 3 works well with either XML or Markdown structure. Choose one and be consistent:

**XML Style:**
```xml
<role>
You are a [domain] research specialist.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Background information, documents, data]
</context>

<task>
[Specific research request]
</task>
```

**Markdown Style:**
```markdown
# Identity
You are a senior [domain] analyst.

# Constraints
- [Constraint 1]
- [Constraint 2]

# Output format
[Structure specification]
```

## Critical: Instruction Placement

For long-context research tasks:

1. **Context first**: Put all documents, data, background at the beginning
2. **Instructions last**: Place your specific questions/tasks at the END
3. **Anchor phrase**: Use "Based on the information above..." to bridge

```xml
<context>
[Long document or multiple sources here]
</context>

Based on the information above:

<task>
[Your research question here]
</task>
```

## Reasoning Enhancement

Gemini 3 can plan and self-critique. For complex research, prompt this explicitly:

```xml
<reasoning_approach>
Before providing the final answer:
1. Parse the research question into distinct sub-questions
2. Check if the provided information is sufficient
3. Create a structured outline of your analysis
4. After drafting, review for completeness and accuracy
</reasoning_approach>
```

**Self-critique pattern:**
```xml
<self_critique>
Before returning your final response, review your analysis:
1. Did I address all parts of the question?
2. Are my claims supported by the provided context?
3. Have I noted areas of uncertainty appropriately?
</self_critique>
```

## Grounding Instructions

For research requiring strict adherence to provided sources:

```xml
<grounding_rules>
You are limited to the information provided in the context. In your analysis:
- Rely ONLY on facts directly mentioned in the provided material
- Do not use external knowledge to fill gaps
- If information is not explicitly stated, say "not available in provided sources"
- Quote or paraphrase specific passages when making claims
</grounding_rules>
```

## Verbosity Control

Gemini 3 defaults to efficient responses. For research depth:

```xml
<output_depth>
Provide comprehensive analysis with:
- Thorough coverage of each aspect
- Supporting evidence for claims
- Multiple perspectives where relevant
- Clear logical progression
Do not prioritize brevity over completeness.
</output_depth>
```

## Output Format Specification

Be explicit about structure:

```xml
<output_format>
Structure your response as follows:
1. **Executive Summary**: [2-3 paragraph overview]
2. **Detailed Analysis**: [Main content organized by theme]
3. **Key Findings**: [Bulleted list of main conclusions]
4. **Limitations**: [What the analysis cannot determine]
</output_format>
```

## Example Deep Research Prompt

```xml
<role>
You are an expert research analyst. Your role is to provide thorough, 
well-reasoned analysis based on careful examination of available information.
</role>

<constraints>
- Base analysis on provided context and sound reasoning
- Note explicitly when making inferences vs. stating facts
- Acknowledge uncertainty and limitations
- Structure response for clarity and readability
</constraints>

<context>
[Insert background documents, data, or source material here]
</context>

Based on the information above:

<task>
Analyze [specific research question].

Address the following:
1. [Sub-question 1]
2. [Sub-question 2]
3. [Sub-question 3]
</task>

<reasoning_approach>
Before answering:
1. Identify the key themes relevant to this question
2. Note any gaps or ambiguities in the provided information
3. Structure your analysis logically
</reasoning_approach>

<output_format>
1. Executive Summary (2-3 paragraphs)
2. Analysis by Theme
   - [Theme 1]
   - [Theme 2]
   - [Theme 3]
3. Synthesis and Conclusions
4. Limitations and Uncertainties

Provide comprehensive coverage. Current date: [DATE]
</output_format>
```

## Temperature Note

For Gemini 3, keep temperature at default (1.0). Lowering temperature can cause unexpected behavior including looping or degraded reasoning on complex tasks.

## Things to Avoid

- Placing instructions before long context (put them after)
- Inconsistent delimiter styles (pick XML or Markdown, not both)
- Vague output specifications
- Over-reliance on "don't" instructions (say what TO do instead)
