# Omnara documentation review

This record covers the Hesperos Clearpath pass that turned the standalone Omnara source tree into a task-oriented public repository.

## Decision

**REVIEW_PASS_WITH_CONDITIONS** for the repository documentation and local helper path within the evidence boundary stated in this record.

The public promise, activation boundary, first-campaign path, workflow explanation, vault reference, validation claims, recovery routes, security guidance, limitations, and maintainer handoff now agree with the shipped standalone skill and local scripts.

## Reader paths reviewed

| Reader and task | Entry point | Disposition |
|---|---|---|
| First-time evaluator deciding whether Omnara is relevant | `README.md` | Clear promise, boundaries, first prompt, and documentation map. |
| User starting a research campaign | `START-HERE.md` | Prerequisites, prompt shape, expected results, durable setup, validation, and completion evidence. |
| Researcher operating a campaign vault | `docs/WORKFLOW.md` and `docs/CAMPAIGN-VAULT.md` | States, ledgers, notes, contradictions, stopping, drafting, and audits are explicit. |
| User recovering from a failure or missing capability | `docs/TROUBLESHOOTING.md` | Symptom-first checks, safe stopping states, and re-entry conditions are present. |
| Reviewer evaluating a readiness claim | `docs/VALIDATION.md` | Structural, semantic, activation, accessibility, and approval claims are separated. |
| Maintainer changing or releasing the skill | `docs/MAINTAINERS.md` | Source authority, synchronized change surfaces, tests, and release triggers are named. |

## Material repair made during the pass

The published standalone `scripts/validate_release.py` inherited requirements and canonical hashes for files that are not present in the standalone repository. It therefore failed against the package it purported to validate.

The validator now checks the actual standalone package, retains custody for the canonical inquiry reference that is shipped, validates JSON and JSONL syntax, and checks local Markdown links. Documentation states the narrower claim directly.

The campaign initializer also creates the otherwise untracked `draft/` directory required by `assemble_report.py`, preventing the documented first-run path from stranding a user.

## Verification performed

- Package validation passed on the working tree.
- Campaign initialization, validation, and summary passed with Python 3.13.5.
- Report assembly passed with ordered Markdown drafts.
- An evidence-free structural citation audit failed as expected rather than issuing a false pass.
- Local Markdown links resolved through the package validator.
- Hesperos' Markdown structural linter was run and findings were reviewed manually.
- The public documentation set passed that linter. Two inherited full-corpus lexical matches were reviewed as non-actionable: the MIT License phrase “above copyright notice” and the persona phrase “falls below the campaign’s risk tolerance”; neither is a layout-direction instruction.
- The human journey was walked from README through first campaign, validation, recovery, security, limitations, and maintenance.

## Conditions and untested surfaces

- Host-level import and selector discovery were not tested in Codex, ChatGPT, Claude, or another skill host during this pass.
- No browser, keyboard, screen-reader, document-export, localization, or representative-user test was performed.
- No formal WCAG, Section 508, legal, security, or privacy conformance claim is made.
- No live research campaign was used to establish semantic citation quality; the deterministic audit remains structural by design.
- The repository remains an individual skill source tree, not a verified standalone plugin package.

The documentation may be released with those boundaries visible. A future host-specific package should add exact installation, discovery, removal, upgrade, and clean-host evidence for that host rather than inheriting generic claims.
