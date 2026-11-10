# Intake fields and missing evidence

Use `assets/intake_form.html` offline or `assets/intake.example.json`. The schema is
`architecture-intake.v2`: project metadata, research argument, evidence records,
figure plan and verified bibliography text. Free-form author input is equally valid.

Core method-writing facts are the problem and actual mechanism. Useful context is
prior approach, limitation and reason, insight, closest work and scope. Experimental
records include readable ID, claim, status (measured/modeled/derived/planned/unavailable),
metric/unit, values, baseline, conditions, source and locator. Missing results remain
pending; do not downgrade a valid mechanism description into an imaginary experiment.

For an existing abstract, extract these fields and mark present/vague/missing before
rewriting substantive claims. Ask one compact question only for facts needed now.
Use the input's actual numbers and source terminology; a converter never verifies them.
`intake_to_brief.py` emits a brief and optional ledger/BibTeX. Exit 2 means missing
core method facts; the brief is still produced for supported partial drafting.
