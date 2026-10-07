# OMNARA Deep Research — expert critique before repair

Recommendation: repair the accepted 1.3.0 promise. The core research doctrine is thoughtful: inquiry, corpus, claim and report are distinct; source ecology and disconfirming observations matter; connection is not support. The artifact machinery and customer journey do not consistently uphold that doctrine. This is not cured by adding more admonitions to SKILL.md. A polished evidence atlas can faithfully display an unearned judgment, and a validator can reward enough words while ignoring whether the actual inquiry was reviewed.

## Accepted baseline and responsibility

Canonical source is the repository root at E:/Github/omnara-deep-research, Git HEAD48b7b231ea91851bcd48a494240436044bc9c202. Accepted shelf ZIP SHA256713e4885f8db656b8894775f30fb08cfd9d114d60f5be5782f06052772de07c6, version1.3.0. Existing SKILL/RELEASE-NOTES edits and extensive untracked room/releases/artwork are preserved in baseline.json and baseline-owned-source.zip. Current declared consumers are Nova Free and Emergent; standalone MIND remains retired. The repair worker owns only this product source and private candidates; root owns shared acceptance/delivery.

## Detailed findings and actionable treatment

### OM-01 — Complete means contradictory things (critical)

Evidence: scripts/research_campaign.py:validate checks phase only; baseline status-complete-only.

Consequence: An empty framing campaign with status complete validates. UI shows complete without either research gate.

Repair: Require phase/status consistency and the same completion checks for any complete declaration; preserve valid sparse active and bounded partial work.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-02 — Semantic review is prose theater at the completion boundary (critical)

Evidence: research_campaign.py COMPLETE_ARTIFACTS; contradicted-complete fixture.

Consequence: Word counts and one citation permit contradicted claims and absent semantic review. Repeating generic words fills every gate.

Repair: Replace word-count proof with typed declared review of report and claim treatment, bound to current question, scope, report, source notes/ledgers and consequential context. Preserve legacy judgments as historical, never silently stamp them current. Recompute deterministic integrity rather than trusting a self-written pass file.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-03 — A changed evidence note retains a fresh-looking verdict (high)

Evidence: citation_audit.py inputs_sha256; changed-note fixture; app.js tone/disposition.

Consequence: Notes and scope can materially change while audit hashes remain current; the atlas paints supported green from unbound native text.

Repair: Bind evidence notes and scope to review subject. Display recorded historical judgments separately from current review; editing relevant content visibly invalidates current review until saved/reviewed. Read-only subject calculation must never generate approval.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-04 — The report is not self-contained or necessarily visible (high)

Evidence: citation_audit.py marker scan; missing-bibliography and hidden-citations fixtures.

Consequence: Markers can occur only in hidden comments; absent title/locator bibliography passes. Reader needs the app to discover sources.

Repair: Check visible prose outside comments/fences; require source entries with title and locator for cited records. Keep claims/numbers/causal entailment with substantive reviewer. Include readable bibliography and mechanism-matched synthesis examples.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-05 — Typed and temporal contracts are mostly unenforced (high)

Evidence: research_campaign.py read_json/validate; schemas/research-campaign.schema.json; typed-fields fixture.

Consequence: Numbers/objects count as inquiry and resume text, required fields disappear, duplicate JSON keys overwrite silently, no clock/cutoff validation exists.

Repair: Validate substantive field types, duplicate keys, IDs, joins and recorded dates with controlled errors. Accept sparse work and explicit unknown dates; reject impossible dates/offsets and post-cutoff publication when declared as a knowledge cutoff, without conflating later retrieval with later knowledge.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-06 — Source states require erasing the work that justified exclusion (high)

Evidence: STATE_PREREQUISITES and TERMINAL_STATES; excluded-after-reading fixture.

Consequence: A researcher cannot honestly retain opened/deeply-read history after excluding a source. Opened also ambiguously means successful reading or failed attempt.

Repair: Preserve acquired reading history when excluding/duplicating; require exclusion reason and canonical duplicate link. Inaccessible cannot substantiate a citation. Clarify opened successful content versus attempted access; actual source-state counts remain overlapping recorded events.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-07 — Assembly can replace a better report with stale drafts (high)

Evidence: scripts/assemble_report.py:assemble.

Consequence: A direct edit in Synthesis/native report is overwritten by draft concatenation without a comparison, backup, or refusal. Old structural/semantic receipts remain next to changed report.

Repair: Refuse changed existing reports unless explicit replace flag; retain prior report before replacement, write atomically, expose changed/current review state and lexical section order.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-08 — Custody checks miss aliases, reparse roots and portable names (high)

Evidence: workspace/campaign.py import resolves before checking links, checked_name permits CON.md; builder walks links.

Consequence: Import can conceal a linked source root; reserved names fail late; builder may ingest junction bytes or silently omit symlink files.

Repair: Reject unresolved symlinks/reparse ancestors before resolving aliases; preflight complete portable namespaces, strict native file boundary and controlled malformed request bodies. Stage import/create/build and preserve prior outputs on failure.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-09 — Save recovery is incomplete across multi-file failure (high)

Evidence: workspace/campaign.py:save; runtime.atomic.

Consequence: History is useful but a write failure leaves half-updated canonical records. Concurrent external agent writes are only detected before the loop.

Repair: Rollback ordinary write failures to original exact native bytes, report rollback failure distinctly, preserve recovery snapshot. Document that an actively writing external agent requires coordination; do not promise distributed atomicity.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-10 — Campaigns disappear instead of asking for repair (high)

Evidence: workspace/campaign.py:/api/list catches and ignores malformed campaign.

Consequence: A malformed campaign becomes invisible to its owner; no path or repair action appears.

Repair: List damaged native campaigns with bounded error and path, preserve open/native-file repair where possible, never convert parse failure into an empty library.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-11 — Navigation and review presentation lose context (medium)

Evidence: app.js reading related-claim jump does not clear atlas filter; source filter leaves unrelated note selected; reportFile persists across campaign switch.

Consequence: A clicked claim may be replaced by another due to active filters; an empty reading search still displays an unrelated source; stale selected document opens blank in another campaign.

Repair: Reset incompatible filters on explicit jumps, align reader selection with visible queue, reset document to report on campaign switch, preserve comparison deliberately, and test actual browser task paths.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-12 — Customer entry and site describe an obsolete product (high)

Evidence: README/docs install and lifecycle; docs/index.html declares1.0.1; privacy denies background service.

Consequence: Users are sent to retired standalone MIND and both-plugin installation; current room is largely absent from onboarding and privacy truth.

Repair: Use current Nova Free/Emergent and complete portable package entry, reachable Open/return/help routes, Python3.10 requirement, honest loopback service/history/export boundary. Preserve historical ancestry only as history.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-13 — Research practice has instructions but no inspectable complete example (high)

Evidence: assets/campaign-vault is only placeholders; references/synthesis-and-citation-audit.md.

Consequence: Users cannot see how evidence that is topically related fails a particular causal claim or how a negative result can still be useful.

Repair: Author a complete, clearly bounded source-to-claim-to-report example and perform a real primary-source comparative inquiry. Demonstrate the decisive mechanism/metric distinction, actual source scope, disconfirming search, honest stopping, audience answer and return event; label synthetic test reviews.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-14 — Persona and authority can replace the caller or reask settled permission (medium)

Evidence: personas/omnara... Let Nova govern; SKILL paid/authenticated separate edge; fallback wholecampaign.

Consequence: Standalone caller is subordinated to Nova; existing grants risk repeated permission gates; small work acquires the full vault ceremony.

Repair: Preserve caller identity and prior task authority. Scale records to useful return/traceability, keep ambitious campaigns possible, and stop only at genuinely new authority or missing consequence-changing inputs.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-15 — Package verification does not verify the accepted full product (high)

Evidence: scripts/validate_release.py required runtime omits workspace and new references; builder recursive exclusions.

Consequence: A package missing its advertised room can pass. Repository scans recurse old frozen archives and verification data, producing unrelated failures; old PASS receipt ships as current.

Repair: Inventory owned current cargo explicitly, require every advertised dependency, verify exact source/package hashes, exclude historical/test state deliberately, preserve old review as historical and provide current bounded evidence. Keep help read-only and native extraction/rebuild checks.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

### OM-16 — Builder overwrites current artifact and stale receipt claims (high)

Evidence: build_workspace_release.py fixed destination, no output option or validation.

Consequence: Failed builds can damage previous candidate and hard-coded skin-only rationale misstates a larger repair. Consumer sets can omit current room or references.

Repair: Build deterministic complete one-root candidate under new output directory, stage and verify before publication, reject full namespace collisions, preserve old bytes, current truthful receipt and exact downstream inventory. Carry sidecar/version/art/CI semantics with whole delta.

Acceptance: demonstrate the stated failure is rejected or recovered while a nearby legitimate research journey still succeeds. Retain exact fixture or authored/browser evidence, and name any unsupported assurance.

## Why previous quality checks missed the defects

The six existing Python tests primarily establish initialization, basic save/conflict handling, launch reuse and minimum packaging. The small JavaScript test deliberately accepts native judgment variants; it never tests whether a judgment still describes the current evidence. Historical documentation PASS is tied to an old content commit but copied into new packages. State presence, word count and a current hash of only three files are proxies for the accepted promise. They cannot establish claim treatment, reader access, correct source custody or a working full product.

Repair validation will challenge actual task outcomes: a changed mechanism cannot inherit a prior verdict, a bibliography must remain visible and complete, an excluded reading retains history, a corrupted campaign remains findable, and saved user work survives ordinary failure. Expert analysis and local browser execution will be labeled separately from independent model trials and participant studies, which have not occurred.

## Independent root review: three further failures

### OM-17 — Review chronology compares days instead of known instants

Accepts a review predating source access on the same day; rejects a valid cross-zone sequence and accepts unknown -00:00 as UTC. Compare exact known timestamp instants; preserve explicit date-only granularity; reject unknown offset. Evidence: `OM17-before.json`; repaired outcome in root-acceptance.json.

### OM-18 — Exponent overflow bypasses finite budget validation

Raw JSON 1e400 is parsed as infinity and accepted as a usable budget. Reject non-finite float results in the common JSON parser, including exponent overflow. Evidence: `OM18-before.json`; repaired outcome in root-acceptance.json.

### OM-19 — Nova integration retains a stale incomplete owner selection

Both consumers retained84files with stale1.1.0 candidate coordinates; the helper excluded examples and linked documentation. Integrate the full107-file current owner closure, bind both manifests, retain historical overlays before current owner and read future selection/version from the owner. Evidence: `delivery-before`; repaired outcome in root-acceptance.json.

