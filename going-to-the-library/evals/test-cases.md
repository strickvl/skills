# Evaluation Cases

These are lightweight manual evals for improving the skill.

## Must trigger

### 1. Explicit phrase

**Prompt:**
> Let's go to the library on domain-driven design. I'm trying to decide whether its concepts would help structure a Python platform for long-running AI agents.

**Expected:**
- Treats DDD as a field with questions and schools, not as a list of books.
- Keeps the Python agent-platform problem visible.
- Separates Evans's historical importance from the best modern doorway.
- Includes practical implementation sources and credible criticism.
- Ends with an interactive route rather than prematurely prescribing an architecture.

### 2. Implicit field-mapping request

**Prompt:**
> Before I design an evaluation system, map the literature and practice around inter-rater reliability, disagreement, and adjudication. I want the classic foundations, current synthesis, and approaches that disagree with one another.

**Expected:**
- Activates without the phrase “go to the library.”
- Includes methodological foundations, modern syntheses, competing views, practical protocols, and limitations.
- Does not treat consensus as automatically desirable.

### 3. Orientation only

**Prompt:**
> Let's go to the library on media archaeology.

**Expected:**
- Proceeds without blocking on a missing workbench problem.
- Labels the visit orientation-only.
- Clarifies boundaries with adjacent fields.
- Offers a route and later opening to connect it to a concrete problem.

### 4. Current technical debate

**Prompt:**
> Let's go to the library on durable execution for coding agents, with special attention to what is actively changing now.

**Expected:**
- Uses current research and dates the live-debate shelf.
- Includes specifications, systems, documentation, papers, and operating experience rather than books alone.
- Clearly separates transcript replay, harness resume, and external-state restoration when evidence supports those distinctions.

## Must not trigger, or should collapse to a direct answer

### 5. Simple lookup

**Prompt:**
> Who coined the term “bounded context”?

**Expected:**
- Gives a direct, sourced answer.
- Does not build a library floor plan unless the user asks for broader orientation.

### 6. Ordinary recommendation

**Prompt:**
> Recommend one accessible book about databases for a Python developer.

**Expected:**
- Gives a recommendation directly.
- Does not create eight shelves unless the user asks for a field map.

## Robustness cases

### 7. Obscure or possibly invented field

**Prompt:**
> Let's go to the library on chrono-semantic orchestration.

**Expected:**
- Verifies whether the term is established.
- Does not invent a literature.
- If it is a coined or ambiguous phrase, identifies nearby real fields and explains the mapping.

### 8. Canon trap

**Prompt:**
> Let's go to the library on scientific management. Just give me the classics.

**Expected:**
- Includes classics but distinguishes influence from present validity.
- Includes labor, empirical, and implementation critiques.
- Avoids treating the traditional managerial canon as the whole field.

### 9. Return test

**Prompt sequence:**
1. Go to the library on causal inference for product experiments because I need to decide how to evaluate an agent feature.
2. Pull the strongest modern synthesis.
3. Compare potential-outcomes and causal-graph approaches.
4. Return to the workbench.

**Expected:**
- Maintains a non-redundant borrowing ledger.
- The final answer changes the evaluation design rather than merely recapping readings.
- Labels which recommendations come from sources and which are synthesis.

## Scoring rubric

Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Triggering | Wrong behavior | Partly appropriate | Correctly triggers or declines |
| Field structure | Flat list | Some grouping | Questions, genealogy, and schools are clear |
| Source integrity | Invented or unsupported | Mostly sound | Verified and access-calibrated |
| Curation | Dump | Mixed | Every item has a distinct role |
| Disagreement | Missing or false balance | Partial | Strong, proportional comparison |
| Practical knowledge | Missing | Token inclusion | Mature practice and failure evidence included |
| Currency | Stale or undated | Some current material | Live debates are genuinely current and dated |
| Interactivity | No usable choices | Generic follow-up | Clear browsing operations and route |
| State | Forgets prior exploration | Partial continuity | Ledger and problem persist cleanly |
| Transfer | Summary only | Some application | Concrete workbench output materially improved |

A strong run scores at least 17/20 and must receive 2 for source integrity and transfer.
