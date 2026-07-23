# Validation and evidence boundaries

Omnara uses deterministic checks to prevent several common forms of evidence drift. Each check has a deliberately narrow claim.

## Validate the standalone package

From the repository root:

```shell
python scripts/validate_release.py .
```

A passing result confirms:

- required runtime and human-facing files are present;
- the retained canonical inquiry reference matches its recorded SHA-256;
- JSON files parse;
- nonblank JSONL rows are JSON objects;
- local Markdown links resolve;
- no `__pycache__` directory is packaged.

It does not confirm that a host discovered the skill, that a research campaign ran, that sources are accurate, or that documentation is accessible in every rendered format.

## Smoke-test campaign creation

```shell
python scripts/research_campaign.py init /tmp/omnara-smoke \
  --title "Omnara smoke test" \
  --query "Can the campaign template initialize and validate?" \
  --tier focused
python scripts/research_campaign.py validate /tmp/omnara-smoke
python scripts/research_campaign.py summary /tmp/omnara-smoke
```

Use a writable destination suitable for your operating system. Remove the smoke-test directory when finished.

Expected validation result:

```text
VALID: /tmp/omnara-smoke
```

This confirms initialization and internal counter consistency. It does not claim that the campaign contains research evidence.

## Validate a live campaign

```shell
python scripts/research_campaign.py validate path/to/campaign
```

The validator checks:

- campaign format, tier, phase, status, inquiry, and resume point;
- source-state prerequisites and terminal-state conflicts;
- substantive notes for deeply read sources;
- source and claim ID uniqueness;
- source links from claims and queries;
- counters against the retained ledgers;
- required artifacts;
- additional completion evidence when phase is `complete`.

## Assemble a report

```shell
python scripts/assemble_report.py path/to/campaign
```

The command concatenates `draft/*.md` in lexical filename order, writes `report.md`, and records word and page-estimate evidence in `report-metrics.json`.

The page figures are estimates at 300 and 500 words per page. They are not rendered-page counts and do not account for figures, tables, layout, or citation density.

## Check structural citation integrity

```shell
python scripts/citation_audit.py path/to/campaign
```

A passing result confirms that:

- the report contains source markers;
- every marker resolves to a source record;
- cited records are not duplicate or inaccessible;
- cited records are marked deeply read and cited;
- substantive evidence notes exist;
- cited source IDs appear in the claim ledger;
- input hashes bind the audit to the current report and ledgers.

## Run the semantic audit separately

The deterministic script cannot determine whether a source entails a claim. Review every consequential claim for:

- exact wording and strength;
- scope, population, geography, version, and time;
- correlation versus causation;
- quantitative units, denominator, period, and method;
- quote accuracy and location;
- stale, transformed, derivative, or conflicted support.

Record each claim as `supported`, `partially supported`, `contradicted`, `mis-scoped`, `stale`, or `unverifiable`. Repair the claim, evidence, or visible uncertainty, then rerun the structural audit if report markers or ledgers changed.

## Documentation checks performed for this pass

The documentation upgrade was checked with:

- the package validator;
- Hesperos' bounded Markdown structural linter;
- a manual task walkthrough from README to first campaign, recovery, validation, and maintenance;
- a local Markdown-link resolution pass through the package validator;
- Python smoke tests for campaign initialization, validation, summary, report assembly, and the expected failure of an evidence-free citation audit.

These checks do not establish formal WCAG conformance, screen-reader compatibility across rendered GitHub surfaces, universal comprehension, or host activation.
