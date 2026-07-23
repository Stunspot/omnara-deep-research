# Omnara Deep Research

**Research with a memory, not a mood.**

Omnara turns a consequential question into an inspectable research campaign. It keeps the inquiry, queries, sources, claims, contradictions, coverage, citations, and stopping decision separate so a polished report cannot quietly outrun its evidence.

Omnara is the deep-research skill shipped inside [Nova the Optimal AI](https://github.com/Stunspot/nova-the-optimal-ai-mind). This repository publishes that skill as a focused standalone source tree for inspection, reuse, and maintenance.

## Start with one useful campaign

When Omnara is available in your host, use a prompt like this:

```text
Use $omnara-deep-research.

Investigate whether small organizations should adopt passkeys for their customer accounts in 2026.
Audience: a product and security lead deciding what to ship.
Scope: consumer web accounts in the United States and European Union.
Include: implementation tradeoffs, account recovery, accessibility, adoption evidence, and credible objections.
Deliverable: a decision brief with a recommendation, evidence limits, contradictions, and refresh triggers.
```

A good result does not begin with a pile of links. It begins by stabilizing the question, mapping what must be covered, and naming the evidence burden.

For the recoverable first-run path, continue to [START-HERE.md](START-HERE.md).

## What Omnara does

Omnara supports bounded research campaigns that need more than search-and-summarize:

- preserves the user's inquiry verbatim;
- explores query families instead of synonym loops;
- distinguishes discovered, inspected, opened, deeply read, excluded, duplicate, inaccessible, and cited sources;
- records evidence notes before treating a source as deeply read;
- keeps source assertions, observations, deterministic results, inferences, synthesis, and speculation distinct;
- maps contradictions and the evidence that could resolve them;
- separates structural citation integrity from semantic entailment;
- checkpoints budgets, blockers, coverage, and the exact resume point.

The report is the final derivative. The campaign vault is the research memory.

## Repository status and activation boundary

This repository is a complete **skill source tree**, not a standalone Codex plugin package. It does not contain a marketplace manifest or claim one universal installation command.

You can use it in either of these ways:

1. **Through Nova:** install the Nova distribution, then invoke `$omnara-deep-research` when the research burden earns it.
2. **Through a skill-capable host:** place or import this directory where that host discovers individual skills. Follow the host's current skill-loading instructions; activation behavior is host-specific.

Python is not required for the research doctrine itself. Python 3 is required for the optional local campaign and validation helpers in [`scripts/`](scripts/).

## Campaign shape

A substantial campaign moves through this loop:

1. Frame the inquiry, audience, decision use, scope, time horizon, and evidence burden.
2. Map coverage loci, live explanations, source ecosystems, and disconfirming questions.
3. Sweep broadly and ledger every candidate before counting it as inspected.
4. Read the evidence-bearing subset in full and write source notes.
5. Build claim and contradiction ledgers.
6. Reconcile gaps and stop by coverage and marginal information value.
7. Draft from an evidence digest and ordered section briefs.
8. Run structural citation checks and a separate semantic claim audit.
9. Deliver the report with counts, limits, budget use, and refresh triggers.

Read [How an Omnara campaign works](docs/WORKFLOW.md) for the full operating path.

## What is in the vault

The reusable template in [`assets/campaign-vault/`](assets/campaign-vault/) includes:

- the canonical inquiry and campaign state;
- query, source, and claim ledgers;
- a coverage matrix and contradiction map;
- source-note, evidence-digest, outline, and report scaffolds;
- structural and semantic citation-audit records;
- a campaign summary for handoff or resumption.

See the [campaign-vault reference](docs/CAMPAIGN-VAULT.md) for field meanings, state transitions, naming conventions, and completion evidence.

## Verify the package

From the repository root:

```shell
python scripts/validate_release.py .
```

The validator checks the actual standalone package structure, JSON and JSONL syntax, retained canonical-file custody, and local Markdown links. It does **not** prove research quality, citation entailment, host activation, or release approval.

For a campaign:

```shell
python scripts/research_campaign.py validate path/to/campaign
python scripts/citation_audit.py path/to/campaign
```

The second command checks structural citation integrity only. A human or capable reviewer must still determine whether each citation supports the exact claim made.

Read [Validation and evidence boundaries](docs/VALIDATION.md) before making readiness claims.

## Documentation map

- [Run a first campaign](START-HERE.md)
- [Choose and shape prompts](docs/PROMPT-RECIPES.md)
- [Understand the workflow](docs/WORKFLOW.md)
- [Use the campaign vault](docs/CAMPAIGN-VAULT.md)
- [Validate the package and campaigns](docs/VALIDATION.md)
- [Recover from common failures](docs/TROUBLESHOOTING.md)
- [Protect credentials, private sources, and campaign data](docs/SECURITY-AND-PRIVACY.md)
- [Understand the current limitations](docs/LIMITATIONS.md)
- [Maintain or extend the skill](docs/MAINTAINERS.md)
- [Read the documentation review](verification/documentation-review.md)

## Provenance and license

This is the curated Omnara skill from the public Nova + MIND 1.0.0 contest release, copied into a fresh standalone history. Private development history is not included. The source snapshot remains available in the [Nova repository](https://github.com/Stunspot/nova-the-optimal-ai-mind/tree/e42dd11646bc548b9ac29d6f700370365ee68986/plugins/nova-the-optimal-ai/skills/omnara-deep-research).

The repository is available under the [MIT License](LICENSE.md). Retrieved research material remains subject to its own rights, access controls, and terms.
