# Mechanism and method sections

Open with the object and boundary: inputs, outputs, reused baseline, new state or
operations, legal transformations and operating constraints. A useful subsection is
need -> mechanism -> expected consequence -> invariant/cost, with a worked example.

Microarchitecture: explain trigger, state access/update, scheduling, communication,
critical path and recovery. Accelerator: explain mapping, residency, movement,
parallelism, metadata and host/service boundary. Co-design: explain compiler/runtime/
hardware contracts and legality. Tools: explain abstraction, consumed fields, coverage,
assumptions and independent validation. Measurements: explain apparatus and controls.

Name inherited machinery and the precise change. A list of modules or agents needs
the flow between them. Mechanism semantics come from actual design/source materials;
missing internals remain TODOs rather than generic nouns posing as an implementation.

Link each central mechanism to an experiment that can support its expected effect.
Correct outputs alone do not establish mechanism conformance, causality or complete
PPA. Use [architecture evaluation](architecture-evaluation.md) for the relevant checks.
