# Sentence and paragraph annotation protocol v1

Scope: complete Abstract and complete Introduction of each development paper's
recorded PDF version. Exclude author block, headings, captions, footnotes, page headers,
reference list and figures. Include contribution bullets as separate paragraphs.
If an Introduction contains named subsections before Background, include them and
record the subsection. Mark any incomplete extraction honestly; incomplete sections
must not contribute to complete-section length statistics.

Sentence primary labels (one each):
- context: setting or broad technical fact needed by this argument.
- problem: bottleneck, unmet goal or research question.
- prior_work: a specific existing technique or baseline and what it does.
- limitation: why existing technique, representation or assumption is insufficient.
- observation: a specific empirical/technical property motivating a design, not a claimed final benefit.
- insight: inference from the observation that makes a new design choice possible.
- mechanism: concrete proposed algorithm, structure, representation or operation.
- methodology: how an experiment, implementation, comparison or validation is performed.
- result: a reported observed/modelled quantitative or qualitative outcome.
- contribution: explicit claim of delivered research object/finding, often a contribution bullet.
- scope: explicit assumption, qualification, excluded regime, cost or limitation governing the claim.
- roadmap: navigation to later paper sections.
Use secondary labels only if a distinct second function matters; do not use secondary
to hide uncertain primary labeling. Prefer the main clause's role; report ambiguity.
"We present X" with no explanation -> contribution; with operational detail -> mechanism.
A measured motivation phenomenon -> observation; a final evaluated benefit -> result.
Distinguish design rationale from measured benefit. Record ambiguous boundaries in notes.

Paragraph roles (one each): setting, gap, prior_work, insight, approach, evidence,
contributions, scope, roadmap, mixed. Paragraph follows visual/rhetorical source breaks;
merge a PDF column continuation, not semantically distinct paragraphs. Contribution
bullets count separately and are marked in the cleaning notes.

Private annotation JSON: paper_id; annotation_version='architecture-moves.v1';
cleaning_notes list; sections [{name:'abstract'/'introduction',complete:bool,
paragraphs:[{pdf_page_start:1,pdf_page_end:1,subsection:'',role:'gap',
summary:'Original short paraphrase of the paragraph function',
sentences:[{text:'exact cleaned source sentence',primary:'limitation',secondary:[]}]}]}].
The paragraph text is the joined sentence text; do not duplicate full paragraphs.
Keep exact source words; normalize whitespace, ligatures and line-wrap hyphens only.
A short standalone clause after a colon or semicolon remains in the source sentence.
Abbreviations, decimals, Fig./Sec./et al. and citations do not automatically end sentences.
Standalone contribution-list fragments and colon-ended lead-ins count as source units in sentence statistics; these are rhetorical segments, not a claim of grammatical sentence perfection. Store all raw source text only in task scratch, not the public repository. Public
annotations contain roles, offsets, lengths, source locators, and paraphrases, not
redistributed paragraphs. Existing short exemplar quotes stay separate.

Annotators are model agents, not human raters. Record the actual annotation method.
Training/dev labels are not ground truth or conference-wide writing rules. A second
review of a small sample measures agreement, not correctness of every annotation.
