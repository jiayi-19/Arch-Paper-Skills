# asplos-2025-smoothe: SmoothE: Differentiable E-Graph Extraction

Reading notes. Text extracted with pdftotext; word counts are approximate.

## 0. Identity
- Title: SmoothE: Differentiable E-Graph Extraction
- Venue and year: ASPLOS 2025 (Volume 1, Rotterdam). Award: ASPLOS 2025 Best Paper.
- Contribution type: mechanism (an algorithm) with a GPU implementation and a comparative study. It is the extraction step used by e-graph based compilers and hardware synthesis flows, so it is tool-like but written as an algorithm paper.
- Pages: 15 including references and an artifact appendix. About 6,800 words in the body.
- Full text used: https://www.csl.cornell.edu/~yc2632/data/smoothe_asplos2025_final.pdf (first author's site, open). DOI 10.1145/3669940.3707262.

## 1. Skeleton
| Sec | Heading | Role | Words | Figs / tables |
|---|---|---|---|---|
| Abstract | | | 200 | 0 |
| 1 | Introduction | | 730 | 0 |
| 2 | Preliminaries (notation, ILP, heuristic methods, other methods, limits of linear cost models) | background, problem formulation, prior work | 1,540 | Fig 1 (e-graph example), Fig 2 (three extraction solutions) |
| 3 | A Differentiable Approach to E-Graph Extraction (3.1 to 3.5) | design | 2,080 | Fig 3 (probability example) |
| 4 | Implementation and Performance Optimization (4.1 to 4.3) | design (systems) | 710 | Table 1 (dataset statistics) |
| 5 | Evaluation (5.1 Experimental Setup, 5.2 Real-World Datasets, 5.3 Adversarial Datasets, 5.4 Linear Cost Models, 5.5 Non-linear Cost Models, 5.6 Performance Optimizations, 5.7 Performance Portability, 5.8 Effectiveness of Sampling) | methodology and evaluation | 2,300 | Tables 2 to 5, Figs 4 to 9 |
| 6 | Conclusion | | 55 | 0 |
| A | Artifact Appendix | | about 400 | 0 |
No Related Work section: prior methods are treated in Section 2 ('Heuristic Methods', 'Other Extraction Methods', 'Limitations of Linear Cost Models'). No separate Motivation section and no Overview section: Section 3 opens with a four-component roadmap. Totals: 9 figures, 5 tables.

## 2. Abstract
- 11 sentences, about 200 words, in two paragraphs (first paragraph 4 sentences of context and problem, second 7 sentences of approach and evaluation).
- Functions: (1) setting: e-graphs are popular; (2) what they enable; (3) the benefit: extraction of the best expression under a cost model; (4) gap: extraction has an unfavorable scalability-quality trade-off and only supports linear costs; (5) 'we propose SmoothE', a differentiable extraction algorithm for complex cost models and GPUs; (6) mechanism: a probabilistic view where the discrete choice is relaxed to continuous; (7) consequence: supports any differentiable cost and gradient descent; (8) implementation in PyTorch; (9) performance techniques for sparsity and data parallelism; (10) evaluation scope: five applications, three cost models, linear and non-linear; (11) result, qualitative: a favorable trade-off between scalability and quality.
- Numbers: only counts of the evaluation (five applications, three cost models). No performance number. The scope is the whole result sentence: "consistently achieves a favorable trade-off".
- System named in sentence 5, with an apposition that gives its type.

## 3. Introduction
- 4 prose paragraphs, a 4-item contribution list, and a one-paragraph roadmap, about 730 words in total.
- P1: setting. Term rewriting, the phase ordering problem, equality saturation, the e-graph, tools (egg, egglog), and a bracketed list of application areas. No claims about the problem yet. Ends listing applications, which signals broad relevance.
- P2: "Extracting a high-quality solution from an e-graph is challenging" (NP-hard in general, large graphs). Ends with the two limitations as a numbered, bold-led list: (1) Unfavorable scalability-quality trade-off (ILP does not scale, heuristics give poor results, CPU only); (2) Inadequate support of realistic cost models (linear only, no learned costs).
- P3: "To address these challenges, we propose SmoothE". Describes the idea in sentences: binary e-node decisions become selection probabilities; gradient descent; parallel on GPUs; sampling to get a valid discrete solution. The key insight appears here, the first place in the body.
- P4: "SmoothE distinguishes itself from existing extraction methods in several key aspects. First, ... Second, ... Third, ..." mapping one to one to the two limitations plus ease of integration.
- Contribution list (4 items): (1) mechanism: first differentiable approach, relaxes the discrete problem to a probabilistic one; (2) components and techniques: PyTorch implementation, sparsity and vectorization, seed batching; (3) result: a comprehensive comparative study on five real datasets; similar quality to ILP with second-scale GPU time (qualitative); (4) capability: handles non-linear and learned costs while keeping quality. No numbers in the list.
- Roadmap paragraph: "The rest of the paper is organized as follows: Section 2 ..." closes the introduction.
- Problem posing: a hard combinatorial problem with two limits, stated as a numbered list of limitations of existing methods, not as one gap sentence.
- Key insight: not labeled as such. It is the sentence that turns binary decisions into probabilities. The abstract states it more cleanly than the introduction does.
- Prior work: credited by naming methods ('Most existing work uses ILP', 'heuristic algorithms like greedy and iterative methods'), dismissed by trade-off, with citations. Named systems appear in Section 2 where each gets a failure example (Figure 2 shows the common-subexpression failure of the heuristic).
- Results preview: none with numbers. A qualitative contribution bullet is the only preview. (The 8x to 37x speed-up appears only in Section 5.4.)

## 4. Motivation and background
- No separate motivation section. Section 2 'Preliminaries' does background, formal problem statement, and the case against existing methods.
- Evidence: analytical with an example. Figures 1 and 2 build one small e-graph (sec^2 alpha + tan alpha) and show three extraction solutions with costs 32, 27 and 19, where the greedy heuristic gives 27 because it misses a shared subexpression and the optimum is 19. Costs are written on the nodes, so the reader can add them up. Limits of ILP are stated without a number in Section 2 ('hours'); the strongest evidence appears only in Section 5.
- Closing sentences: each Preliminary subsection ends on a limitation sentence (ILP "does not scale well on large e-graphs"; heuristics "overestimate costs by ignoring the reuse of common subexpressions"). Two real systems (E-syn, ROVER) are used in the last subsection to motivate non-linear costs.
- Tie to design: Section 2's three completeness and acyclicity constraints are the exact list Section 3 relaxes, one per subsection (3.3 completeness, 3.4 acyclicity). Notation introduced in Section 2 is reused throughout.

## 5. Overview of the design
- No Overview section. Section 3 opens with a roadmap paragraph: break the discrete problem into four components (variables, objective, completeness constraints, acyclicity constraint) and transform each; then 3.5 ties them into optimization and sampling.
- There is no whole-system figure. Figures 2 and 3 are the same small e-graph with costs and then with probabilities; Figure 3 plays the role of a running example for the probability computation.
- Key insight is handled by the structure itself: each subsection starts with the discrete form (from Section 2) and ends with its differentiable form.

## 6. Design sections
- Pattern for 3.1 to 3.4: the discrete component, the relaxed form (with equation numbers), then the difficulty (for example 'computing phi exactly is exponential, so use loopy belief propagation'), then the choice made and alternatives (three correlation assumptions: independent, fully correlated, hybrid). 3.5 closes with the optimizer plus sampling schedule and stopping rules.
- Worked example: Figure 3 with a few conditional probabilities and a hand-computed objective (f(p) = 19 + 13 cp1 - 5 cp1 cp4), which shows the minimum equals the optimal solution in Figure 2.
- A short theorem and proof for the acyclicity trick (borrowed NOTEARS) is included inline, with the sentence "To explain the core idea of NOTEARS, we include the following theorem and a brief proof".
- Section 4 (systems): 4.1 vectorization and sparsity, 4.2 seed batching, 4.3 matrix exponential optimization (SCC decomposition, batched approximation). Each trick states the bottleneck first, then the fix. It includes an approximation formula that trades exactness for speed.
- Components named consistently: e-node, e-class, cp (conditional probability), p (probability), NOTEARS term, seed, completeness constraints, acyclicity constraint.
- Details deferred: baselines, hyper-parameter grid search (done on one random e-graph per dataset), MLP training recipe are in Section 5.

## 7. Evaluation
- Not organized by research question. Organized by experiment: setup, datasets (real and adversarial), linear cost, non-linear cost, performance optimization ablations, portability, sampling effectiveness.
- First result (5.4): Table 2, five realistic datasets. Metric: cost increase over an oracle (CPLEX run for 10 hours) as worst and average, plus runtime, with failures counted in red. ILP solvers have a 15-minute limit.
- Claim bounding: baselines are three ILP solvers (CPLEX, SCIP, CBC), egg's heuristic and an improved heuristic. Datasets come from prior work (three public). SmoothE results report the maximum difference over three runs.
- Reporting that does not flatter: SmoothE is not best on flexc (CPLEX is at 0.0%, SmoothE at 0.7% worst, 0.2% average); on the NP-hard adversarial datasets all ILP solvers find the optimum in under a minute, SmoothE is 21.9% to 22.9% worse on average and is claimed only to beat the heuristics there. The text states both. Non-linear experiments use a synthetic MLP and say that real non-linear models from prior work are not open source.
- Summary sentence for the main result: SmoothE gives similar solution quality to ILP with much faster GPU execution (8x to 37x speed-up) and beats both heuristics.
- Ablations: Figure 6 (CPU, +GPU, +MatExp; each about 10x), Figure 7 (seed count: cost and variance fall as seeds grow, latency grows sub-linearly until 64 seeds), Figure 8 (runtime breakdown), Table 5 (lower-end GPU), Figure 9 (sampling loss versus relaxed loss).
- Negative results: four cases fail on the smaller GPU because memory per seed exceeds capacity; stated directly.

## 8. Sentence and paragraph habits
- Average sentence length about 26 words in the design sections, 20 to 22 in evaluation. Paragraphs 100 to 180 words.
- 'We' about 120 times; present tense for method, present for results. Phrases like 'Next, we will provide a more formal statement' are used as transitions.
- Bold run-in headings for method subparts ('Heuristic Methods.', 'Seed Batching.', 'Anytime Results.', 'Results on Real-World Datasets.', 'Ablation Study.').
- Semicolons about 24; em dashes about 19 (many in figure and table captions as a separator); parentheses for definitions and for 'i.e.'.
- Hedging is low: 'we find', 'it is expected', 'typically'.
- Numbers: percentages are normalized to an oracle; ranges ('8x to 37x'); standard deviation as plus-minus in tables.
- Sentence patterns:
  1. "Extracting a high-quality ___ is challenging due to ___ and ___."
  2. "While a number of ___ have been proposed, existing approaches still have significant limitations: (1) ___: ___ (2) ___: ___"
  3. "To address these challenges, we propose ___, a ___. More specifically, we ___ by transforming ___ into ___."
  4. "___ distinguishes itself from existing ___ in several key aspects. First, ___. Second, ___. Third, ___."
  5. "We present ___, the first ___ approach to ___, which relaxes ___ into ___, enabling ___."
  6. "We break down the original ___ into four key components: 1) ___ 2) ___ 3) ___ 4) ___, and transform each separately."
  7. "In summary, ___ offers similar solution quality to ___ with much faster ___, significantly surpassing ___."
  8. "This experiment showcases that ___ is capable of ___ other than ___."

## 9. Figures and tables
- First figure (Figure 1): a three-panel e-graph with two rewrites (sec^2 alpha + tan alpha), with the caption defining every symbol. It comes first because the entire audience (architecture venue) must learn what an e-graph is. Figure 2 reuses it to show three extractions with costs.
- Caption style: very descriptive, long, defining notation (for example the Table 1 caption defines every column). Takeaways are rarely in captions; they appear in the text.
- Carrying figures: Figure 2 (32, 27 and 19 costs side by side), Figure 4 (anytime curves against CPLEX), Figure 6 (stacked speed-up bars for CPU, GPU, MatExp on a log axis).
- Tables: Table 2 has two statistics per solver per dataset (time with failure counts, and worst and average cost increase). Heavy but consistent, and Table 3 gives the per-graph breakdown behind Table 2.

## 10. Why it reads as strong, and what does not transfer
Three moves to copy:
1. A tiny numeric example reused three times (Figures 1 to 3): the reader sums costs of 32, 27, 19 and sees both the heuristic's failure and the relaxation's correctness. The same example proves the formulation at the end of 3.3.
2. An introduction whose two numbered limitations (scalability-quality; cost-model realism) are answered by three 'First, Second, Third' distinguishing points and four contributions, so each limit maps to a feature.
3. Honest evaluation framing: oracle defined as a 10-hour CPLEX run, a hard 15-minute ILP limit, failures counted and shown in red, adversarial datasets where ILP wins, and a stated limit that real non-linear models were not available.

Not to copy: the abstract and introduction carry no number at all, so the headline result (8x to 37x faster at similar quality) is missing from the first two pages; also the lack of a related-work section depends on prior methods fitting into the preliminaries.
