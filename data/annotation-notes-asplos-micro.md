# ASPLOS and MICRO development annotations

This batch covers the complete Abstract and complete Introduction of all six ASPLOS and all six MICRO development sources in the recorded manifest: 24 complete sections, 138 source paragraphs, and 560 sentences. Every sentence has an inspected functional primary label. All sections stop at the next major section; named Introduction material, contribution bullets, and roadmaps are included. Page numbers below refer to one-based PDF file pages.

| Recorded primary source | Abstract paragraphs / sentences | Introduction paragraphs / sentences | Introduction PDF pages |
| --- | ---: | ---: | --- |
| [DianNao, ASPLOS 2014](https://www.cs.princeton.edu/courses/archive/spring16/cos598F/p269-chen.pdf) | 3 / 9 | 10 / 27 | 1–2 |
| [Automatically Characterizing Large Scale Program Behavior, ASPLOS 2002](https://cseweb.ucsd.edu/~calder/papers/ASPLOS-02-SimPoint.pdf) | 2 / 9 | 6 / 27 | 1–2 |
| [Paragon, ASPLOS 2013](https://people.csail.mit.edu/delimitrou/papers/2013.asplos.paragon.pdf) | 3 / 12 | 9 / 51 | 1–2 |
| [GhostRider, ASPLOS 2015](https://www.cs.umd.edu/~mwh/papers/ghostrider15.pdf) | 1 / 7 | 12 / 49 | 1–2 |
| [Centauri, ASPLOS 2024](https://jf-d.github.io/files/Centauri.pdf) | 2 / 9 | 11 / 47 | 1–3 |
| [TensorIR, ASPLOS 2023 development source](https://arxiv.org/pdf/2207.04296) | 1 / 7 | 11 / 36 | 1–2 |
| [Utility-Based Cache Partitioning, MICRO 2006](https://users.ece.northwestern.edu/~rjoseph/eecs453/papers/quereshi-micro2006.pdf) | 2 / 8 | 6 / 30 | 1–2 |
| [CACTI 6.0, MICRO 2007](https://www2.cs.utah.edu/~rajeev/pubs/micro07a.pdf) | 1 / 9 | 6 / 33 | 1–2 |
| [McPAT, MICRO 2009](https://raw.githubusercontent.com/HewlettPackard/mcpat/master/Documents/micro09.pdf) | 2 / 8 | 6 / 28 | 1–2 |
| [Decoupled Vector Runahead, MICRO 2023](https://www.cl.cam.ac.uk/~tmj32/papers/docs/naithani23-micro.pdf) | 1 / 6 | 4 / 18 | 1–2 |
| [NoCap, MICRO 2024](https://people.csail.mit.edu/devadas/pubs/micro24_nocap.pdf) | 3 / 11 | 19 / 53 | 1–2 |
| [Avatar, MICRO 2024](https://www.cs.cmu.edu/~18742/papers/Park2024.pdf) | 3 / 14 | 14 / 52 | 1–2 |

## Annotation and reconstruction method

A model agent read the full source sections, selected actual source paragraphs, inspected every sentence's main rhetorical function, and visually checked rendered PDF pages for paragraph indentation, column continuations, section boundaries, and first-figure layout. The agent applied the repository's `architecture-moves.v1` protocol. No human annotation or independent expert adjudication is claimed.

Sentence boundaries were initially suggested by a small script that protects abbreviations and decimal points. The agent inspected the resulting sentence lists and assigned primary labels from the sentence's function in the argument. Repeated roadmap labels reflect their explicit section-navigation function; they are not keyword-derived classifications of arbitrary sentences. The actual fragment selections, label assignments, and source repairs remain reviewable in task-private scripts.

Source reading order required explicit repair. DianNao's Abstract continuation appears above its Abstract opening in the flow extraction, and its first contribution bullet is separated from the other two by a column break. SimPoint, Paragon, GhostRider, CACTI, McPAT, DVR, and Avatar contain interrupted column or page continuations. Centauri's Introduction continues around a figure and table and onto PDF page 3. NoCap's provided flow text interleaves the two columns line by line; its reconstruction instead uses direct per-page, per-column `pdftotext` crops. The visual audit also separated DianNao's opening design-goal paragraph from its following application-selection paragraph.

Only whitespace, typographic ligatures, line-wrap hyphenation, clearly lost compound hyphens, and separated word fragments were normalized. Grammatical infelicities and technical claims were retained. Author information, captions, figure/table content, footnotes and their numeric markers, running matter, copyright material, and indexing metadata were excluded from section prose. Contribution bullets form individual paragraphs. Run-in topic headings are recorded as subsection context where applicable. TensorIR's recorded source is arXiv:2207.04296v2, dated 27 October 2022; a different publication layout was not substituted.

Each private JSON includes source-verification provenance, the corrected private source-text path, the reconstruction script path, exclusions, and an exact normalized transcription audit. All 560 sentences match their corrected reconstructed source. This audit checks consistency of transcription against the retained reconstruction; it is not independent evidence that the model's paragraph decisions or functional labels are correct. Corrected full text, original extracts, exact captions, and rendered source pages remain in task scratch and are not redistributed in this repository.

## Interpretation and uncertainty

The difficult distinctions are rhetorical: a capability statement can function as a delivered-object claim or operational description; an enabling design argument can resemble a qualitative benefit; a motivating measurement can resemble a final result. The annotations distinguish these using the main clause and the surrounding argument. Explicit research-object claims generally receive `contribution`, concrete operations receive `mechanism`, motivating empirical properties receive `observation`, and evaluated benefits receive `result`. A few sentences retain a distinct scope qualifier as a secondary label. Per-paper cleaning notes record these judgment boundaries.

All twelve first figures were inspected, with their exact captions retained privately alongside page, panel-count, width, and figure-kind metadata. Motivating code listings in GhostRider and DVR are recorded as `other`, rather than forced into a plot or hardware-diagram category. Caption typography for mathematical variables in NoCap is limited by text extraction and is noted in its private record. These classifications describe the inspected papers and do not establish conference-wide writing rules.

This is a development set for studying generic computer-architecture paper functions. It is neither a representative venue sample nor human ground truth. The annotation does not validate, rerun, or endorse the papers' technical results.
