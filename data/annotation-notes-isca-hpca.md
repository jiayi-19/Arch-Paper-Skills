# ISCA and HPCA development-set annotation notes

The twelve recorded source PDFs below were read for their complete Abstract and Introduction, including contribution lists, introductory subsections, and roadmaps. All 24 sections are marked complete. The private records contain 140 paragraphs and 541 sentence or source-fragment units. These are model annotations under `architecture-moves.v1`, not human ground truth or claims about conference-wide writing conventions.

## Coverage and recorded sources

Page numbers refer to physical PDF pages, starting at one. Counts include contribution bullets as separate paragraphs. The sentence counts include short list-introduction and code-availability fragments; section-pointer parentheticals remain attached to their preceding sentences.

| Paper and recorded PDF | Abstract paragraphs / units | Introduction paragraphs / units | Abstract / Introduction PDF pages | Introduction endpoint |
| --- | ---: | ---: | --- | --- |
| [Constable](https://arxiv.org/pdf/2406.18786) | 3 / 11 | 18 / 41 | 1 / 1–2 | All seven contribution bullets, before Background |
| [Mind the Gap](https://raw.githubusercontent.com/hqjenny/hqjenny.github.io/master/papers/2024ISCA/2024ISCA_Orojensis.pdf) | 3 / 11 | 12 / 37 | 1 / 1–2 | Final positioning paragraph, before Motivation |
| [Adaptive Insertion Policies](https://www.cs.cmu.edu/afs/cs/academic/class/15740-f18/www/papers/isca07-qureshi-dip.pdf) | 2 / 10 | 6 / 34 | 2 / 2–3 | Final measured-benefit paragraph, before Motivation |
| [Wattch](https://mrmgroup.cs.princeton.edu/papers/isca2000.pdf) | 3 / 10 | 12 / 55 | 1 / 1–2 | Subsections 1.1 and 1.2 plus full roadmap, before power-modeling methodology |
| [Eyeriss](https://d1qx31qr3h6wln.cloudfront.net/publications/ISCA_2016_Eyeriss.pdf) | 2 / 10 | 9 / 26 | 1 / 1–2 | Four contribution bullets, before Spatial Architecture |
| [DRAM disturbance errors](https://www.istc-cc.cmu.edu/publications/papers/2014/kim-isca14.pdf) | 1 / 12 | 9 / 38 | 1 / 1–2 | Four contribution bullets, before DRAM Background |
| [Perceptron branch prediction](https://www.cs.utexas.edu/~lin/papers/hpca01.pdf) | 2 / 8 | 10 / 30 | 1 / 1–2 | Final contribution bullet, before Related Work |
| [Runahead execution](https://people.inf.ethz.ch/omutlu/pub/mutlu_hpca03.pdf) | 1 / 9 | 6 / 25 | 1 / 1–2 | Complete evaluation paragraph, before Related work |
| [Stretch](https://homepages.inf.ed.ac.uk/bgrot/pubs/STRETCH_HPCA19.pdf) | 2 / 9 | 12 / 30 | 1 / 1–2 | Four contribution bullets, before Aggressive Workload Colocation |
| [PIM pathfinding](https://arxiv.org/pdf/2308.00846) | 1 / 7 | 4 / 23 | 1 / 1–2 | Final research-directions sentence, before UPMEM-PIM Architecture |
| [TALCO](https://sumit-walia.github.io/assets/paper/TALCO.pdf) | 1 / 15 | 9 / 45 | 1 / 1–2 | Five numbered contributions and full roadmap, before Background |
| [DynamoLLM](https://arxiv.org/pdf/2408.00741) | 1 / 8 | 11 / 37 | 1 / 1–2 | Three contribution bullets, before Background |

DIP's supplied PDF includes a ResearchGate cover page. Wattch's physical pages 1–2 are printed pages 83–84. DynamoLLM uses the downloaded arXiv v1 dated 1 August 2024; its association with HPCA 2025 follows the development manifest and does not imply identity with a later camera-ready paper. PIM pathfinding uses the recorded arXiv v3 dated 7 March 2024. Constable uses the recorded arXiv v1 dated 26 June 2024.

## Annotation and cleaning method

The annotator read the source text before assigning functions. A private preparation script extracted page-positioned lines with `pdftotext -bbox-layout`; indentation, line spacing, and list markers identified candidate paragraph boundaries. The model inspected these boundaries and corrected column continuations, hanging indents, numbered contributions, displaced trademarks, footnote markers, and run-in headings. Sentence splitting protected abbreviations, decimals, citations, and section references. Scripts assembled manually specified judgments and checked that every retained source unit received exactly one primary label. No keyword-based label assignment was used. Each private record also identifies the PDF, original manifest extraction, page-positioned blocks, corrected pre-labeling source-flow text, relevant page images, and an exact-substring assembly audit. All 541 units match their corrected source flow; this verifies text assembly, not independent annotation correctness.

Wattch's character map produced unreadable text. Both original pages were rendered at 2400-pixel height, OCRed with Tesseract 4.1.1, and the entire recovered Abstract and Introduction were visually checked against the page images. Its grammatical irregularities were retained. The PDF page images also resolved Runahead's displaced trademark text, the small-probability inequality in Rowhammer, and a dropped letter in Constable's tool-release paragraph. All raw/OCR text and cleaned source sentences remain in task scratch, outside the public repository.

Exact source wording is preserved with whitespace, ligature, and line-wrap normalization. Source geometry, rather than semantic topic changes, determines paragraph boundaries. Thus long mixed paragraphs remain mixed, and a contribution list's introductory clause can remain a short standalone unit. The opening industry quotation in PIM pathfinding remains associated with its attribution. TALCO's Abstract code-availability statement is retained as a delivered-artifact unit.

## Judgment boundaries and first figures

One primary function follows the main clause. Operational proposals are mechanisms; naming a research object without operational detail is a contribution. Quantitative properties that motivate a design are observations; evaluated end benefits are results. Explicit costs and applicability constraints can be scope even inside a results discussion. Contribution-list placement is represented by paragraph role and, where useful, a secondary contribution label rather than overriding the sentence's substantive function. Individual private cleaning notes record paper-specific ambiguities.

The original first figure of every paper was visually inspected. Their provisional primary kinds are five motivation plots, three conceptual figures, two mechanism diagrams, and two system overviews. All occupy a single column in the recorded PDFs. Eyeriss and PIM pathfinding contain linked overview/detail regions without formal panel letters; their counts treat these as two visual regions. Rowhammer explicitly labels two panels; Wattch labels three usage scenarios; DynamoLLM places two service plots within Figure 1. Series and individual bars are not separate panels. Mind the Gap's analytical gap illustration and TALCO's tradeoff plot could reasonably receive neighboring conceptual or results-oriented classifications; private metadata states these judgment boundaries. These descriptions are evidence from this development set, not mandatory templates.
