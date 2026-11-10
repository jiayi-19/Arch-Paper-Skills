# Computer Architecture writing corpus

Initial curated edition: 24 papers, six each from HPCA, ASPLOS, ISCA, and MICRO. Original publication years range from 2000 to 2025. Selection is purposeful rather than statistical; notable means a teaching selection, not a quantified fame ranking. Recognition was checked against official conference or society sources on 2026-11-10.

Each record contains one short exact excerpt, its one-based PDF page and section, the inspected reading scope, source/version notes, an original writing analysis, and a transfer caveat. Abstract/introduction plus selected technical/evaluation passages were read; this is not a full sentence-level annotation of 24 complete papers.

The machine-readable [corpus](corpus.json) stores each quote once. Retrieve a full card on demand:

```bash
python3 scripts/find_exemplars.py --list --limit 100
python3 scripts/find_exemplars.py --id isca2016-eyeriss
python3 scripts/find_exemplars.py --move "validation" --limit 3
python3 scripts/find_exemplars.py --recognition best_paper_candidate --limit 5
```

## Recognition and use

Best paper: 6. Formal candidate/nominee or designated Best Paper Session: 5. Test of Time or named Influential Paper Award: 9. Notable teaching selections: 4. These describe the selected records, not conference-wide distributions.

`test_of_time` is a retrieval category; for ISCA and ASPLOS the exact named recognition is an Influential Paper Award. Publication and award years are recorded separately. A Best Paper Session entry is labeled as that source supports; it is not silently treated as a winner.

## Route by writing need

| Writing need | Useful exemplars |
|---|---|
| Define a remaining cost after strong prior work | Constable, Decoupled Vector Runahead |
| Make a model decision-relevant and validate its abstraction | Mind the Gap, Wattch, CACTI 6.0, McPAT |
| Expose a misleading proxy or fixed assumption | UCP, Adaptive Insertion Policies, Perceptron |
| Separate resource scale, mechanism, and accounting | Eyeriss, DianNao, NoCap |
| Characterization and observed population | RowHammer, PIM Pathfinding |
| Explain semantic limits or speculative recovery | TALCO, Runahead, Avatar, GhostRider |
| Couple a representation change to search/decisions | Centauri, TensorIR, Paragon |
| State system tradeoffs and operating regimes | Stretch, DynamoLLM |
| Validate a cheaper evaluation route against independent behavior | SimPoint, Wattch |

## Papers

### HPCA

| Paper / ID | Recognition | Writing function |
|---|---|---|
| [DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency](https://arxiv.org/pdf/2408.00741) (2025)<br>`hpca-2025-dynamollm` | [best paper (2025)](https://www.sigarch.org/hpca-2025-trip-report/) | Derive dynamic control from time-varying workload properties. |
| [Pathfinding Future PIM Architectures by Demystifying a Commercial PIM Technology](https://arxiv.org/pdf/2308.00846) (2024)<br>`hpca-2024-pim-pathfinding` | [best paper (2024)](https://www.hpca-conf.org/2024/program/main.php) | Build a tool-to-observation-to-design implication argument. |
| [TALCO: Tiling Genome Sequence Alignment using Convergence of Traceback Pointers](https://sumit-walia.github.io/assets/paper/TALCO.pdf) (2024)<br>`hpca-2024-talco` | [best paper candidate (2024)](https://www.hpca-conf.org/2024/program/main.php) | Attach the qualification to a correctness or quality claim. |
| [Stretch: Balancing QoS and Throughput for Colocated Server Workloads on SMT Cores](https://homepages.inf.ed.ac.uk/bgrot/pubs/STRETCH_HPCA19.pdf) (2019)<br>`hpca-2019-stretch` | [best paper (2019)](https://ieeetcca.org/awards/hpca-best-paper-award/) | Turn asymmetric workload sensitivity into an allocation rule. |
| [Runahead Execution: An Alternative to Very Large Instruction Windows for Out-of-order Processors](https://people.inf.ethz.ch/omutlu/pub/mutlu_hpca03.pdf) (2003)<br>`hpca-2003-runahead` | [test of time (2021)](https://ieeetcca.org/awards/hpca-test-of-time-award/) | State the architectural invariant while explaining speculative execution. |
| [Dynamic Branch Prediction with Perceptrons](https://www.cs.utexas.edu/~lin/papers/hpca01.pdf) (2001)<br>`hpca-2001-perceptron` | [test of time (2019)](https://ieeetcca.org/awards/hpca-test-of-time-award/) | Explain why a mechanism works, including its domain of failure. |

### ASPLOS

| Paper / ID | Recognition | Writing function |
|---|---|---|
| [Centauri: Enabling Efficient Scheduling for Communication-Computation Overlap in Large Model Training via Communication Partitioning](https://jf-d.github.io/files/Centauri.pdf) (2024)<br>`asplos-2024-centauri` | [best paper (2024)](https://www.asplos-conference.org/asplos2024/best-paper-awards/index.html) | Explain which representational restriction prevents an existing optimizer from finding the desired schedule. |
| [TensorIR: An Abstraction for Automatic Tensorized Program Optimization](https://arxiv.org/pdf/2207.04296) (2023)<br>`asplos-2023-tensorir` | notable | Derive a new abstraction from the unit of computation that older representations obscure. |
| [GhostRider: A Hardware-Software System for Memory Trace Oblivious Computation](https://www.cs.umd.edu/~mwh/papers/ghostrider15.pdf) (2015)<br>`asplos-2015-ghostrider` | [best paper (2015)](https://asplos-conference.org/asplos2015/) | Define the protected property and attacker observations before interpreting performance. |
| [DianNao: A Small-Footprint High-Throughput Accelerator for Ubiquitous Machine-Learning](https://www.cs.princeton.edu/courses/archive/spring16/cos598F/p269-chen.pdf) (2014)<br>`asplos-2014-diannao` | [test of time (2024)](https://www.sigarch.org/benefit/awards/acm-sigarch-sigplan-sigops-asplos-influential-paper-award/) | Qualify a headline result by implementation stage and measurement scope. |
| [Paragon: QoS-Aware Scheduling for Heterogeneous Datacenters](https://people.csail.mit.edu/delimitrou/papers/2013.asplos.paragon.pdf) (2013)<br>`asplos-2013-paragon` | [test of time (2024)](https://www.sigarch.org/benefit/awards/acm-sigarch-sigplan-sigops-asplos-influential-paper-award/) | Turn historical experience into a concrete prediction-and-decision mechanism. |
| [Automatically Characterizing Large Scale Program Behavior](https://cseweb.ucsd.edu/~calder/papers/ASPLOS-02-SimPoint.pdf) (2002)<br>`asplos-2002-simpoint` | [test of time (2017)](https://www.sigarch.org/benefit/awards/acm-sigarch-sigplan-sigops-asplos-influential-paper-award/) | Connect an inexpensive representation to independent behavioral validation. |

### ISCA

| Paper / ID | Recognition | Writing function |
|---|---|---|
| [Constable: Improving Performance and Power Efficiency by Safely Eliminating Load Execution](https://arxiv.org/pdf/2406.18786) (2024)<br>`isca2024-constable` | [best paper (2024)](https://www.iscaconf.org/isca2024/) | Credit the closest technique, then isolate the remaining physical bottleneck. |
| [Mind the Gap: Attainable Data Movement and Operational Intensity Bounds for Tensor Algorithms](https://raw.githubusercontent.com/hqjenny/hqjenny.github.io/master/papers/2024ISCA/2024ISCA_Orojensis.pdf) (2024)<br>`isca2024-mind-the-gap` | [best paper candidate (2024)](https://www.iscaconf.org/isca2024/program/) | Expose why a familiar lower bound is uninformative, then define a more decision-relevant bound. |
| [Eyeriss: A Spatial Architecture for Energy-Efficient Dataflow for Convolutional Neural Networks](https://d1qx31qr3h6wln.cloudfront.net/publications/ISCA_2016_Eyeriss.pdf) (2016)<br>`isca2016-eyeriss` | notable | Make fair comparison part of the contribution and explain the accounting before reporting gains. |
| [Flipping Bits in Memory Without Accessing Them: An Experimental Study of DRAM Disturbance Errors](https://www.istc-cc.cmu.edu/publications/papers/2014/kim-isca14.pdf) (2014)<br>`isca2014-rowhammer` | notable | State the violated invariant, quantify the observed population, and separate demonstration from controlled characterization. |
| [Adaptive Insertion Policies for High Performance Caching](https://www.cs.cmu.edu/afs/cs/academic/class/15740-f18/www/papers/isca07-qureshi-dip.pdf) (2007)<br>`isca2007-dip` | [test of time (2026)](https://www.sigarch.org/isca-2026-trip-report/) | Decompose a familiar problem to reveal a small intervention with a measurable mechanism. |
| [Wattch: A Framework for Architectural-Level Power Analysis and Optimizations](https://mrmgroup.cs.princeton.edu/papers/isca2000.pdf) (2000)<br>`isca2000-wattch` | [test of time (2015)](https://ieeetcca.org/awards/influential-isca-paper-award/) | Position a fast model by the design decision it enables and the independent checks that justify using it. |

### MICRO

| Paper / ID | Recognition | Writing function |
|---|---|---|
| [A Case for Speculative Address Translation with Rapid Validation for GPUs](https://www.cs.cmu.edu/~18742/papers/Park2024.pdf) (2024)<br>`micro-2024-avatar` | [best paper candidate (2024)](https://www.microarch.org/micro57/program/) | Pair a fast speculative path with explicit validation and recovery semantics. |
| [Accelerating Zero-Knowledge Proofs Through Hardware-Algorithm Co-Design](https://people.csail.mit.edu/devadas/pubs/micro24_nocap.pdf) (2024)<br>`micro-2024-nocap` | [best paper candidate (2024)](https://www.microarch.org/micro57/program/) | Strengthen the comparison baseline using the same algorithmic improvements. |
| [Decoupled Vector Runahead](https://www.cl.cam.ac.uk/~tmj32/papers/docs/naithani23-micro.pdf) (2023)<br>`micro-2023-dvr` | [best paper candidate (2023)](https://www.microarch.org/micro56/program/) | Use a scaling sweep to expose an obsolete trigger condition. |
| [McPAT: An Integrated Power, Area, and Timing Modeling Framework for Multicore and Manycore Architectures](https://raw.githubusercontent.com/HewlettPackard/mcpat/master/Documents/micro09.pdf) (2009)<br>`micro-2009-mcpat` | notable | Match the validation target to the kind of measurement actually available. |
| [Optimizing NUCA Organizations and Wiring Alternatives for Large Caches with CACTI 6.0](https://www2.cs.utah.edu/~rajeev/pubs/micro07a.pdf) (2007)<br>`micro-2007-cacti6` | [test of time (2025)](https://www.sigmicro.org/awards/tot/) | Expose the model changes needed before applying a tool to a new design. |
| [Utility-Based Cache Partitioning: A Low-Overhead, High-Performance, Runtime Mechanism to Partition Shared Caches](https://users.ece.northwestern.edu/~rjoseph/eecs453/papers/quereshi-micro2006.pdf) (2006)<br>`micro-2006-ucp` | [test of time (2024)](https://www.sigmicro.org/awards/tot/) | Challenge the proxy metric with a concrete counterexample. |

## Scope and rights

Excerpts teach rhetorical choices; they are not a phrase bank. Do not transplant their technical results into a different study. Some source PDFs are author preprints or university-hosted copies, with version differences recorded in each card. Wattch required visual reading because its original font encoding prevents reliable text extraction. Full PDFs and temporary extraction files are not shipped with this skill. See [maintenance](corpus-maintenance.md) and [attribution](../NOTICE.md).
