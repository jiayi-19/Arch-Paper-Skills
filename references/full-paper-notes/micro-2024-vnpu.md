# micro-2024-vnpu: Hardware-Assisted Virtualization of Neural Processing Units for Cloud Platforms

Source read: arXiv v3 (13 Sep 2024) of the MICRO 2024 paper. The camera-ready may differ in formatting. Counts are estimates from pdftotext of a two-column layout, with the reference list and figure text removed where possible. The text extraction merges columns in places, so the paragraph counts for the introduction were checked by hand.

## 0. Identity
- Title: Hardware-Assisted Virtualization of Neural Processing Units for Cloud Platforms
- Venue and year: MICRO 2024. Award: Best Paper Runner-up.
- Contribution type: co-design (system abstraction, resource allocator, ISA extension and microarchitecture support), implemented on a production-level NPU simulator with real TPU traces.
- Pages: 16 in the arXiv PDF, about 12 pages of body.
- Authors: Xue, Liu, Nai (Google), Huang (UIUC).
- Full text used: https://arxiv.org/pdf/2408.04104v3

## 1. Skeleton
Roman-numeral sections with lettered subsections; "Section" references use the section sign ("§III-D"). Body prose about 9,500 words including captions.

| Section | Approx words | Figures / tables | Role |
|---|---|---|---|
| Abstract | ~215 | 0 | summary |
| I Introduction | ~1,000 (about 11 paragraphs + 5 bullets) | Fig 1 | problem as three "Lack of ..." gaps, approach, contributions, results |
| II Background and Motivation (A NPU architecture, B characterization of ML inference, C virtualization challenges and opportunities) | ~1,100 | Figs 2-9, Table I | background and measured motivation on real TPUv4 |
| III Design and Implementation (A vNPU abstraction, B allocation and deallocation, C mapping and security, D ISA extension, E architectural support for NeuISA, F system support, G implementation) | ~3,500 | Figs 10-18, Table II | overview (objectives and roadmap) + design |
| IV Discussion | ~290 | Fig 19-20 spill over | scope and limits (placed before the evaluation) |
| V Evaluation (A setup, B performance, C utilization, D benefit breakdown of harvesting, E varying MEs and VEs, F varying memory bandwidth, plus an LLM case study) | ~1,500 | Figs 19-27, Table III | methodology + results |
| VI Related Work | ~550 | 0 | related work, four bold run-in paragraphs |
| VII Conclusion | ~60 | 0 | conclusion |

Totals: 27 figures, 3 tables. Design is the largest section. Discussion sits between Design and Evaluation, which is unusual.

## 2. Abstract
- 9 sentences, about 215 words, one paragraph.
- Functions: (1) setting, clouds deploy NPUs for ML inference; (2) insight or approach in the abstract, "a natural approach is to virtualize NPUs"; (3) problem, "However, virtualizing NPUs ... is not easy"; (4) the gap in two named parts, no system abstraction and no architectural and ISA support for fine-grained dynamic operator scheduling; (5) system named, "We present Neu10, a holistic NPU virtualization framework"; (6) scope, across the entire software and hardware stack; (7) mechanism, three numbered components (vNPU abstraction, resource allocator, ISA extension) in one long sentence; (8) method, implemented on a production-level NPU simulator; (9) result, three numbers.
- Numbers: throughput up to 1.4x, tail latency up to 4.6x, NPU utilization 1.2x on average, "compared to state-of-the-art NPU sharing approaches". Scope: "up to" for two, "on average" for one; baseline named only as a class.
- System named in sentence 5 after setting, approach, problem and gap.
- Quote (Abstract): "virtualizing NPUs for modern cloud platforms is not easy"

## 3. Introduction
- About 11 paragraphs and 5 bullets, about 1,000 words.
- P1: setting, ML services and NPUs (ends with the TPU as an example).
- P2: "A common approach to using NPUs in cloud platforms is to assign an entire NPU chip to a single ML application instance"; underutilization shown with a prior study; ends "the one-size-fits-all approach is much less attractive".
- P3: "To address the utilization challenge..., it is desirable to virtualize hardware devices... Unfortunately, modern cloud platforms have very limited virtualization ..." This sets up three bold run-in problems.
- P4 to P6: three bold run-in paragraphs, the challenges: "Lack of system abstraction support for NPUs.", "Lack of architectural support for NPU virtualization.", "Lack of ISA support for virtualized NPUs." Each opens with the bold label, states what exists, why it fails, and ends with a "We need..." sentence ("We need to rethink the NPU ISA design to facilitate dynamic resource scheduling for virtualized NPUs.").
- P7: "Ideally, we wish to virtualize NPUs to enable flexible and fine-grained resource sharing... We present Neu10, a hardware-assisted system virtualization framework for NPUs."
- P8 to P10: bold run-in "Our contributions." paragraph then the vNPU abstraction, the allocation and mapping, and the ISA extension (µTOps) as running prose, each answering one of the three gaps in the same order.
- P11: result preview: "We implement Neu10 with a production-level NPU simulator" with real TPU traces, then the three numbers and the 0.04% die-area overhead.
- Contributions: 5 bullets, each with a section pointer. (1) a study of DNN inference on real NPU hardware and virtualization challenges (finding, §II); (2) vNPU abstraction (component, §III-A); (3) allocation scheme and vNPU-to-pNPU mappings (mechanism, §III-B and C); (4) ISA and architecture extension (mechanism, §III-D and E); (5) evaluation with real traces (result, §V). No numbers in the bullets; numbers are in P11 above. Bullets carry section sign pointers.
- Problem posed as three missing things, matched one-to-one by three contributions.
- Key insight first appears as the observation that ME and VE control flows can be decoupled; in the intro it is told as a design fact ("Neu10 extends the VLIW-style ISA by reorganizing VLIW instructions into independent micro-Tensor operators"). The explicit sentence ("Our key observation is that the execution of different MEs and VEs in a tensor operator is usually separable.") is in II-C.
- Prior work dismissed in the three gap paragraphs: GPU and FPGA virtualization "cannot be directly applied to NPUs, as they target different architectures"; PREMA-like time sharing "sacrifice isolation or suffer from high preemption overhead"; V10 "still based on the time-sharing mechanism".
- Fig 1 is the first figure (NPU board architecture) and sits at the end of page 1/2 of the intro, with a footnote on pay-as-you-go.

## 4. Motivation and background
- Section II "Background and Motivation": A is architecture (Fig 1); B is a measured characterization on a real TPUv4 board of 11 DNN models: the number of MEs and VEs demanded over time (Fig 2, 3), the intensity ratio (Fig 4), utilization (Fig 5), a VE underuse example (Fig 6), HBM bandwidth (Fig 7). Bold run-in headings: "Diverse demands on MEs/VEs.", "Low NPU resource utilization."
- C "NPU Virtualization: Challenges and Opportunities" gives four bold run-in items: new abstraction required, dynamic resource scheduling (harvesting), ISA limitations (Figs 8-9), architectural support for parallelizing ME/VE operations. Each item ends with a need statement, "we need to ...".
- Observations end in a sentence that states the consequence ("collocating DNN workloads on the same NPU core helps cloud platforms utilize both resources"), not a box.
- Tie to design: the four challenge items map to III-A (abstraction), III-B and C (allocation, mapping), III-D and E (NeuISA and hardware), with §-pointers inside the text ("see §III-B").
- Quote (II-C): "Our key observation is that the execution of different MEs and VEs in a tensor operator is usually separable."

## 5. Overview of the design
- No Overview heading. Section III opens with three design objectives as bullets (allocation flexibility, NPU utilization, performance isolation), each one sentence giving a reason, then one roadmap sentence with six section pointers ("We first present a new vNPU abstraction (§III-A). Based on this, we enable flexible vNPU resource allocation (§III-B) and vNPU-to-pNPU mappings (§III-C)...").
- Length: about 150 words. The figure that serves as the overview is Fig 11, the system architecture of Neu10, inside III-A. It shows guest VM, hypervisor, vNPU manager, hypercalls, PCIe virtual function, and the NPU's µTOp scheduler with numbered steps 1-3 that the text walks in the vNPU lifecycle paragraph.
- Walks the figure by numbered steps (1 hypercall, 2 vNPU context setup, 3 command buffer).
- Key insight: the observation that ME and VE control flows are separable was set up in II-C and turns into the µTOp design in III-D.

## 6. Design sections
- Subsection pattern: state a goal (as bold run-in labels such as "vNPU abstraction.", "vNPU lifecycle.", "ME/VE allocation.", "Memory allocation.", "vNPU mapping schemes.", "vNPU security isolation."), give the mechanism, give an analytical model (Amdahl-style Equations 1-4 for the ME/VE ratio), then a cost-effectiveness check against measured data (Fig 12).
- The ISA section (III-D) introduces NeuISA with µTOp types (ME µTOp, VE µTOp), µTOp groups for fused operators, control flow instructions (Fig 14), program structure (Fig 15), compiler support and overhead (<1%, Fig 16).
- Worked examples: Fig 8 splits a tiled MatMul+ReLU into independent ME and VE streams; Fig 9 shows why a VLIW program cannot use more or fewer MEs; Fig 18 gives a cycle-level example of ME and VE harvesting between two vNPUs.
- Names stay stable: vNPU, pNPU, ME, VE, µTOp, NeuISA, harvesting, spatial-isolated and temporal-sharing modes; baselines are PMT, V10, Neu10-NH, Neu10.
- Movement between components: the vNPU config goes from the guest driver to the hypervisor to the vNPU manager to the NPU context; the µTOp scheduler fetches ready µTOps per vNPU context.
- Left out or deferred: side channels ("We leave side-channel mitigation to future work"), multi-chip virtualization, cluster-level placement ("orthogonal to our work"); the Discussion section handles engineering effort and generation compatibility.
- Figure types: architecture block diagrams, ISA and program-structure listings, a worked timeline example, scatter of configurations (Fig 12).

## 7. Evaluation
- Section V opens with a numbered list of four claims in one paragraph ("(1) Neu10 provides performance isolation with up to 4.6x reduction in tail latency... (2) It improves NPU utilization by 1.2x... ..."), each with a subsection pointer. This is an organization by claim, not by research question.
- First result: tail latency (Fig 19, 95th percentile normalized to PMT), which is also the headline number.
- Bounding: baselines described in a bullet list (PMT, V10, Neu10-NH, Neu10) with a one-line mechanism for each; workload pairs grouped by contention level (low, medium, high); each workload on a vNPU with 2 MEs and 2 VEs; batch size 32 except two models at 8.
- Ablation: Neu10-NH (spatial isolation without harvesting) versus Neu10 isolates the harvesting benefit; subsection D traces per-operator speedups (Fig 23) and tabulates harvesting overhead (Table III, 3.12% average).
- Negative or weak: for high-contention pairs "harvesting causes performance degradation for some operators", and "In a few cases (e.g., ENet+MRCN and RNRS+RtNt), harvesting increases the burden on memory bandwidth". The paper says the overall speedup outweighs the slowdowns.
- Added sensitivity: varying MEs and VEs (Fig 25), HBM bandwidth (Fig 26), and a case study collocating LLaMA-13B (Fig 27).
- Bold run-in headings per metric: Tail Latency, Average Latency, Throughput.

## 8. Sentence and paragraph habits
- Average sentence length: about 26-29 words (script: roughly 29, includes some column-merge noise; hand sample about 25).
- Paragraph length: 6-10 sentences; many paragraphs start with a bold run-in label.
- Person and tense: present; "we" about 98 and "our" about 13; "Neu10" is the subject of most design sentences.
- Topic sentences: stated; paragraphs end in a "need" statement or consequence.
- Lists: numbered (1)(2)(3) inside sentences (abstract, intro, eval opening); bullets for objectives, baselines, contributions.
- Parentheticals about 140 (many "e.g." and section pointers); semicolons about 6; em dashes none; en dashes about 3.
- Hedging: low; "may", "can", "typically" used for technical possibility.
- Numbers: "up to 1.4x", "on average"; area overhead stated twice (intro, III-G).
- Eight patterns:
  1. "Lack of ___ support for ___." (bold run-in problem heading)
  2. "However, ___ cannot ___ since ___. We need ___." (limit then need)
  3. "Ideally, we wish to ___ to enable ___. We present ___, a ___ framework for ___." (naming)
  4. "Our key observation is that ___ is usually ___." (insight)
  5. "We first present ___ (§X). Based on this, we enable ___ (§Y) and ___ (§Z)." (roadmap)
  6. "To simplify ___, we ___; this is impossible with ___, as they ___." (contrast with prior design)
  7. "Our evaluation shows that: (1) ___ ; (2) ___ ; (3) ___ (§V-B)." (eval roadmap)
  8. "In a few cases (e.g., ___), ___ may slightly impact ___. However, ___ still achieves ___." (limited weak result)

## 9. Figures and tables
- First figure (Fig 1): schematic of an NPU board (chips, cores, matrix and vector engines, HBM), with no results. It comes first because the paper's vocabulary (ME, VE, core, board) must be set before the motivating measurements. Fig 2 (the first measured figure) is a set of per-workload time series of the number of MEs and VEs demanded (BERT, Transformer, NCF, DLRM, ResNet, Mask-RCNN), which makes "diverse demand" visible.
- Captions: descriptive; some state what the reader should see (Fig 6 "Example of VE underutilization in an ME-intensive operator"); Fig 23 caption explains the axes and what curves above and below 1 mean.
- Figures that carry the argument: Fig 11 (system architecture) and Fig 18 (harvesting example). Fig 5 (utilization of ME and VE per model) carries the problem.
- Table design: Table I lists models by category with abbreviations and footprint; Table II hardware configuration; Table III harvesting overhead per workload with a "<0.01%" convention explained in the caption.

## 10. Why it reads as strong, and what does not transfer
Three writing moves to copy:
1. Three bold run-in problems named "Lack of X support" in the intro (P4-P6), answered by three contributions in the same order (P8-P10), then by the three numbered claims in the evaluation opening (V). One triple, carried through the paper.
2. A "need" sentence closing each gap paragraph ("We need to rethink the NPU ISA design...") that turns the gap into a requirement the design satisfies.
3. A roadmap sentence at the start of the design with section pointers, and section pointers in the contribution bullets, so every claim in the intro points to where it is delivered.
Particular to this paper: the NPU-specific vocabulary (ME, VE, VLIW, µTOp) and the virtualization threats (side channels, security isolation); not transferable.
