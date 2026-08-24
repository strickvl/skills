# Research and Verification Protocol

Use this protocol when building or refreshing the catalog. It is deliberately stricter than ordinary recommendation search because a convincing invented bibliography is worse than a short honest one.

## 1. Build a vocabulary map before searching for authorities

Identify:

- the field's own preferred terms;
- historical names for the same issue;
- neighboring disciplines that frame it differently;
- ambiguous terms likely to produce irrelevant results;
- major institutions, journals, conferences, standards bodies, archives, or professional communities.

Use orientation sources to learn search vocabulary, not as automatic final authorities.

## 2. Search in passes

### Pass A: Structural map

Find handbooks, review articles, reference entries, graduate syllabi, standards overviews, or respected field histories that reveal the major questions and schools.

Goal: learn the shape of the field and candidate names.

### Pass B: Foundations and genealogy

Locate the original works, cases, experiments, systems, or events that later sources repeatedly treat as turning points.

Goal: verify what was actually claimed and what problem it answered.

### Pass C: Current synthesis

Find recent review papers, textbooks, handbooks, state-of-the-field essays, official documentation, or systematic evidence reviews.

Goal: avoid describing the field as it looked twenty years ago.

### Pass D: Disagreement and disconfirmation

Search explicitly for critiques, replication failures, negative cases, rival schools, limitations, and boundary conditions.

Goal: prevent a single tradition from masquerading as the whole field.

### Pass E: Practice

Find standards, operational manuals, protocols, reference implementations, mature codebases, case collections, or practitioners with demonstrated experience.

Goal: learn what competent operators actually do, including where practice diverges from theory.

### Pass F: Live debates

Search recent papers, conference programs, standards proposals, official roadmaps, working groups, credible expert exchanges, and newly important cases.

Goal: identify what is moving now, not merely what is fashionable online.

## 3. Verify each surviving catalog item

For each item, verify as many of these as apply:

- exact creator or institutional author;
- exact title;
- publication or release date;
- venue, publisher, standard body, repository, or archive;
- DOI, ISBN, stable catalog record, official documentation page, or repository;
- actual thesis or function;
- why later sources regard it as important;
- whether major revisions or editions changed it.

One authoritative metadata record can establish existence. Characterization usually requires the work itself or multiple reliable discussions.

## 4. Track the access basis

Internally tag each source as one of:

- **FULL:** full text or complete primary material inspected;
- **PRIMARY-SUMMARY:** official abstract, executive summary, documentation, or author-provided synopsis;
- **EXCERPT:** meaningful excerpts inspected;
- **SECONDARY:** reviews, histories, citations, or scholarly discussion only;
- **METADATA:** existence and bibliographic data only.

Do not make detailed claims that exceed the access basis. Tell the user the basis during a deep dive when it affects confidence.

## 5. Apply domain-specific source priorities

### Technical and software fields

Prefer specifications, official documentation, source code, design documents, issue discussions, benchmarks with disclosed methodology, and original papers. Blog posts are useful when written by the people who built or operated the system, but still distinguish experience from general evidence.

### Science and medicine

Prefer original studies, systematic reviews, consensus guidelines, trial registries, and official safety guidance. Note study design, population, effect size, uncertainty, and replication. Do not infer clinical advice from mechanistic plausibility alone.

### History and humanities

Prefer primary materials, critical editions, archival guides, historiographical surveys, and serious reviews. Separate a work's influence from the present scholarly consensus. Identify schools of interpretation and the sources on which they depend.

### Law and policy

Prefer statutes, regulations, cases, official guidance, legislative history, and current jurisdiction-specific commentary. Verify current legal status and dates.

### Management, design, and practice-heavy fields

Triangulate conceptual works with case evidence, failure reports, operational playbooks, and practitioners who have repeatedly done the work. Be suspicious of frameworks supported mainly by memorable diagrams and consultancy repetition.

## 6. Judge inclusion by role, not fame

An item earns a place when it contributes at least one distinct role:

- establishes a foundational question;
- supplies a powerful concept or method;
- synthesizes a fragmented field;
- represents a major competing school;
- provides unusually strong evidence;
- exposes a failure or boundary condition;
- embodies mature practice;
- reframes the field from an adjacent discipline;
- captures a genuinely live transition.

Remove redundant items, even famous ones, when they add no new role.

## 7. Use calibrated labels

Useful labels include:

- historically foundational;
- best doorway;
- current synthesis;
- empirically strong;
- influential but disputed;
- practically useful with weak evidence;
- difficult primary source;
- field standard;
- minority school;
- emerging and uncertain;
- outdated except for genealogy.

Avoid vague praise such as “seminal,” “essential,” or “groundbreaking” unless you explain the exact influence.

## 8. Handle disagreement proportionally

Represent serious schools in proportion to their evidential and disciplinary standing. Do not manufacture a fifty-fifty debate when one view is fringe. Conversely, do not erase a minority school when it identifies real anomalies or dominates a relevant subfield.

For each major disagreement, ask:

1. Are they answering the same question?
2. Do they use the same unit of analysis?
3. Do they disagree about facts, values, mechanisms, definitions, or scope?
4. What observation would update either side?
5. Could both be useful under different conditions?

## 9. Know when the catalog is stable

Stop expanding when new sources mostly duplicate existing roles and no longer change:

- the governing questions;
- the genealogy;
- the set of serious schools;
- the practical options;
- the known failure modes;
- the current uncertainty.

At that point, deeper searching has diminishing returns. Return to the user's problem.
