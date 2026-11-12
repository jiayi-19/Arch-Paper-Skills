# hpca-2025-dynamollm: DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency

Source read: arXiv v1 text (2 Aug 2024 posting; the HPCA 2025 camera-ready may differ in small ways). Word counts are estimates from pdftotext of a two-column layout; figure and table text is excluded where I could.

## 0. Identity
- Title: DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency
- Venue and year: HPCA 2025. Award: Best Paper.
- Contribution type: system or framework (energy management for LLM inference clusters), with a characterization section that motivates it.
- Pages: 14 in the arXiv PDF (about 11.3 pages of body, then references).
- Authors: Stojkovic, Zhang, Goiri, Torrellas, Choukse (UIUC and Microsoft Azure Research).
- Full text used: https://arxiv.org/pdf/2408.00741v1

## 1. Skeleton
Roman-numeral sections, no numbered subsubsections. Body prose about 7,800 words.

| Section | Approx words | Figures / tables | Role |
|---|---|---|---|
| Abstract | 184 | 0 | summary |
| I Introduction | ~850 (7 paragraphs + 3 bullets) | 0 / 0 | problem, insight, system, preview |
| II Background | ~430 | 0 / 0 | background (LLM phases, metrics, parallelism, datacenter power) |
| III Opportunities for Energy Efficiency | ~1,900 | Figs 1-3 / Tables I-V | motivation (measured characterization), A heterogeneous profiles, B dynamic workloads, C reconfiguration overheads |
| IV DynamoLLM: An Energy Management Framework | ~2,900 | Figs 4-5 / Table VI | overview ("Architecture" paragraph) + design A-E (configuring instances, hierarchical control, reduced overheads, predictive scheduling, implementation) |
| V Evaluation | ~1,300 | Figs 6-16 / 0 | methodology (A) + results B-F |
| VI Related Work | ~330 | 0 | related work, two run-in paragraphs |
| VII Conclusion | ~90 | 0 | conclusion |

Totals: 16 figures, 6 tables. Section III is the longest motivation section relative to the paper and holds the first figure. Evaluation is relatively short (about 17% of the body).

## 2. Abstract
- 8 sentences, 184 words (a single paragraph).
- Sentence functions in order: (1) setting, LLMs are a pivotal workload; (2) setting, inference clusters with strict SLOs; (3) problem, power-hungry GPUs cause energy and carbon; (4) insight, "Fortunately, we find" an opportunity in heterogeneity and fluctuation; (5) gap or challenge, "However", a large search space of configurations (instances, parallelism, frequency); (6) approach, "To address these challenges, we propose DynamoLLM, the first energy-management framework"; (7) mechanism, it automatically and dynamically reconfigures the cluster under SLOs; (8) result, "We show that at a service-level..." with three numbers.
- Numbers: 53% energy, 38% operational carbon, 61% customer cost. The scope is one phrase, "at a service-level" and "while meeting the latency SLOs". The baseline is not named in the abstract. The "at a service-level" scope is vague; the baseline is revealed only in the evaluation (SinglePool).
- System named in sentence 6, after problem, insight and gap. Six sentences of buildup before the name.
- Quote (Abstract): "DynamoLLM, the first energy-management framework for LLM inference environments."

## 3. Introduction
- 7 prose paragraphs plus a lead-in line and 3 bullets; about 850 words (including bullets).
- P1: setting, opens "The exponential growth in the adoption of generative large language models"; ends with infrastructure cost (sophisticated software, expensive hardware), which sets up the "efforts so far" paragraph.
- P2: prior work credited and then limited. Opens "To meet these ever increasing computing demands, researchers proposed various software and hardware techniques"; ends by saying energy is paramount. The turn is a single "However, one aspect that has been largely overlooked is the energy consumption". Prior work is credited in one sentence and dismissed by omission, not by criticism.
- P3: "To address this gap, this paper starts by characterizing..." Says the characterization shows a different set of challenges from traditional datacenter energy management, then names the three sources of variation as a numbered inline list (1) request length, (2) model, (3) SLO.
- P4: concrete explanation of the three sources with causal statements (large input compute-bound, so frequency-sensitive; few input and many output tokens memory-bound). Ends "This requires a dynamic approach to resource management", which sets up the system paragraph.
- P5: "To pave the way towards energy-efficient and sustainable LLM inference clusters, this paper introduces DynamoLLM, the first energy-management framework". Names three knobs (instances, parallelism, GPU frequency).
- P6: how heterogeneity is handled (pools), how pools change (merge, split), hierarchy of controllers, overhead reduction. Ends with the sentence that the system "maintains high levels of efficiency and service quality".
- P7: result preview, two sentences. One sentence on the evaluation setup (large GPU cluster, production-level traces from a major cloud provider) and the same three numbers as the abstract.
- Contribution list: lead-in "The contributions of this paper are as follows:" and 3 bullets. Item 1 is a finding or analysis ("An analysis of the opportunities..."); item 2 is a system ("Design and implementation of DynamoLLM"); item 3 is a result type but with no number ("An evaluation... on a large-scale platform using production-level traces"). Numbers are not in the list; they are in P7 just before it.
- How the problem is posed: energy is overlooked; LLM inference has three kinds of variation, so any fixed configuration goes stale. The key insight (exploit heterogeneity and fluctuation, reconfigure dynamically) first appears in the abstract and is repeated in P3 and P4.
- No "challenges" device in the introduction. The challenge appears in the abstract ("large search-space") and as the three "Insight" boxes in Section III. The introduction is organized by what is observed, not by what is hard.
- Prior-work handling: credit, then a single "overlooked" gap; related work (Section VI) separates "cluster and power management", "energy-efficient workloads" and "efficient LLM inference serving", each ending with how DynamoLLM differs.
- No figure in the introduction.

## 4. Motivation and background
- Background (II) is separate and short: prefill/decode, TTFT/TBT/throughput, TP/PP, datacenter energy. Ends with a one-sentence gap: LLM inference is a growing share of datacenter load and needs a comprehensive framework.
- Motivation is its own section, III "Opportunities for Energy Efficiency", measured on an NVIDIA DGX H100 with vLLM and on Azure production traces. Evidence: heat-map tables of energy in Wh by tensor parallelism and GPU frequency (Tables I-III), a request-length distribution (Fig 1), a week-long load (Fig 2), a measured overhead breakdown (Table V, Fig 3).
- Structure: A "Heterogeneous Energy-Performance Profiles" (request lengths, load, model, SLO as run-in bold headings), B "Dynamic LLM Inference Workloads", C "Reconfiguration Overheads".
- Each major subsection ends with a bold "Insight #N" paragraph of two sentences: the first states the observation, the second states what the system must do. Three insights total.
- Mapping to design: the four design principles at the start of Section IV map to the insights (energy-optimized and SLO-aware; per-request-type pools; dynamic reconfiguration; minimized overhead). Forward references appear inline ("In DynamoLLM, we will propose techniques to...", "In DynamoLLM, we will show how to minimize the re-sharding overheads"). The mapping is not stated as a table; it is by repeated wording.
- Quote (III): "Insight #1 LLM workloads are highly heterogeneous in their energy-performance profiles."

## 5. Overview of the design
- No separate Overview section or subsection. The section opens with one paragraph that states four key principles (First... Second... Third... Finally), then an "Architecture" run-in paragraph that walks Figure 4.
- Fig 4 shows a hierarchy: Cluster Manager, Pool Managers, Instance Managers, with profile and predictor boxes. Length of the overview text: about 250 words.
- Text walks the figure with numbered components in the order cluster manager (1), pool manager (2), instance manager (3), each in one sentence saying what it receives and what knob it controls.
- Key insight handling: it was already stated in Section III, so the overview only restates it as principles.
- Forward references are by subsection letter implicitly (IV-A configuring instances, IV-B hierarchy), not by explicit "Section IV-B" pointers.

## 6. Design sections
- Subsection pattern: what the controller decides (MILP formulation, Equation 1), why it is too slow for fine-grained use ("~100s of ms"), the hierarchy that approximates it, what overhead each knob pays and how it is reduced, then how mispredictions are handled.
- Run-in bold headings do the work of subsubsections ("Scale-out/in", "Shard-up/down", "Scale-up/down", "Handling fragmentation", "Accounting for the overheads", "Reducing downtime").
- Worked example: Figure 5 re-sharding TP4 to TP2 and TP8 in prose, with a time unit T (1/8 of weights, 50 ms) and Table VI of all transitions in units of T.
- Component names are stable: Cluster Manager, Pool Manager, Instance Manager, SinglePool/MultiPool/ScaleInst/ScaleShard/ScaleFreq as the baselines that are also ablations. Pool names are request-type codes (SS, SM, ..., LL).
- Movement between components: constraints flow downward, "each controller operates under the conditions imposed by the upper level, computes its dedicated knob, and forwards further constraints to ..."; time scales shorten downward (30 min, 5 min, 5 s).
- Left out or deferred: details of predictor models cite prior work; implementation (IV-E) closes the section in one paragraph.
- Figure types: architecture block diagram, re-sharding diagram, algorithm described in prose (graph matching), one equation.

## 7. Evaluation
- Not organized by research questions. Organized by experiment: A setup, B cluster-level (energy, latency, power, frequency changes, sharding changes), C sensitivity (predictor accuracy, load, number of pools), D long cluster-level (1-day), E large-scale simulation (1-week, two services), F cost and carbon.
- First result: Fig 6, energy of six systems on 1-hour open-source Conversation trace with 12 H100 servers.
- Claim bounding: baseline named per claim (SinglePool vs DynamoLLM), the model (Llama2-70B), trace (1 hour, 1 day, 1 week), and level (cluster, simulator). The abstract's 53% mixes results over a week of traces; the headline numbers are service-level.
- Ablation: the baselines are cumulative knobs: MultiPool, then ScaleInst, ScaleShard, ScaleFreq each alone, then all together. Energy: MultiPool +20%, ScaleInst 4.1%, ScaleShard 7%, ScaleFreq 19%, DynamoLLM 35%.
- Weak or negative results stated in line: MultiPool raises energy 20%; P50 latency rises 11.4% and 7.6% while P99 falls 5.3% and 11.1%; savings shrink as load rises (51%, 40%, 23.4%); user cost saving from energy is "only $4.4/hour" next to $1362.7/hour from fewer GPUs; 40% predictor error costs 13% energy.
- Bold run-in headings per metric: Energy, Latency, Power, Frequency changes, Sharding changes.

## 8. Sentence and paragraph habits
- Sentence length: about 25 words in sampled prose (script: 25.7 on body prose, rough).
- Paragraph length: 5-9 sentences in the intro and design, shorter in evaluation.
- Person and tense: present tense, "we" about 49 times in 7,800 words; the subject is more often "DynamoLLM" or "the system". Future tense used for forward references ("In DynamoLLM, we will propose techniques").
- Topic sentences: stated first; paragraphs often close with a consequence sentence.
- Bold run-in headings: very heavy in III, IV and V.
- Lists: numbered inline lists "(1)... (2)... (3)..." inside sentences; bullets only for contributions.
- Parentheticals: about 119 in the body (many "e.g."). Semicolons: about 5. Dashes: essentially none (no em dash; two en dashes in ranges).
- Hedging: low. "can", "may" only 15 times for modal hedges; claims are plain ("This approach guarantees the energy optimal configuration.").
- Numbers: stated as percentages with the baseline attached in the same sentence in evaluation; in abstract and intro stated without baseline.
- Eight sentence patterns:
  1. "However, one aspect that has been largely overlooked is ___." (gap)
  2. "To address this gap, this paper starts by characterizing ___." (turn to the study)
  3. "Insight #N ___. To achieve ___, ___ need to be ___." (takeaway box)
  4. "Such ___ cause a ___ that is ___ at a given point to quickly become sub-optimal. This requires ___." (problem to need)
  5. "To pave the way towards ___, this paper introduces ___, the first ___ for ___." (naming the system)
  6. "In ___, we will propose techniques to ___ while minimizing ___." (forward reference inside motivation)
  7. "___ reduces ___ by X% and Y%, while it increases ___ by Z%." (result with the cost stated next to it)
  8. "As the ___ increases, the savings of ___ reduce, because ___." (negative result with a reason)

## 9. Figures and tables
- First figure (Fig 1, in Section III, not the introduction): stacked bars of the weekday distribution of the nine request types for Coding and Conversation. It comes first because the whole system rests on the claim that requests differ and the mix drifts. Before it, Table I (energy heat map) is the first evidence object.
- Caption style: descriptive ("Distribution of requests based on input and output lengths categorized into three groups"). Table captions say what is varied and how SLO violations are shown (gray empty boxes). Few captions state a takeaway.
- Figures that carry the argument: Fig 4 (hierarchy of controllers, per-request-type pools) and Fig 6 (six systems, energy per request type). Tables I-III as heat maps give the whole search space in a glance; empty gray cells show SLO violations.
- Table design: rows are request type or model, columns are TP x frequency; color per row marks the lowest energy. Also a request-length threshold table (IV) and an overhead breakdown (V) with totals.

## 10. Why it reads as strong, and what does not transfer
Three writing moves to copy:
1. A numbered inline list of the sources of variation in the intro (P3), reused as the section structure of III-A and as the three insights and four principles (Intro P3; Sec III; start of Sec IV). One list, reused, so the reader recognizes the structure.
2. Every characterization subsection ends in a two-sentence bold Insight: observation, then what the system must do (Section III, Insights #1-#3). This makes the motivation a chain of requirements.
3. The evaluation names the cost next to each win (Section V-B latency paragraph, V-C load sensitivity, V-F cost paragraph), so that the headline numbers look conservative.
Particular to this paper: the heat-map tables of energy by TP and frequency and the carbon-intensity accounting; these depend on measured GPU energy and do not carry to a design-automation paper.
