#!/usr/bin/env python3
"""Validate the standalone OMNARA skill source tree."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

EXPECTED_HASHES = {
    "references/canonical/inquiry-engine-v1.md": (
        "351183C36A1D14B1FA28B1DDCE9D0AD0437ECF627CFF90150F4ACBB02928AFD0"
    ),
}

REQUIRED = [
    "README.md",
    "START-HERE.md",
    "LICENSE.md",
    "SKILL.md",
    "agents/openai.yaml",
    "personas/omnara-investigative-research-intelligence.md",
    "knowledge/source-navigation.md",
    "references/operating-doctrine.md",
    "references/search-cartography.md",
    "references/evidence-and-investigation.md",
    "references/synthesis-and-citation-audit.md",
    "references/tooling-cost-and-security.md",
    "references/campaign-operations.md",
    "references/canonical/inquiry-engine-v1.md",
    "assets/campaign-vault/campaign.json",
    "assets/campaign-vault/draft/.gitkeep",
    "schemas/research-campaign.schema.json",
    "scripts/research_campaign.py",
    "scripts/citation_audit.py",
    "scripts/assemble_report.py",
    "fallbacks/degraded-capability.md",
    "fallbacks/universal-copy-paste-workflow.md",
    "docs/README.md",
    "docs/PROMPT-RECIPES.md",
    "docs/WORKFLOW.md",
    "docs/CAMPAIGN-VAULT.md",
    "docs/VALIDATION.md",
    "docs/TROUBLESHOOTING.md",
    "docs/SECURITY-AND-PRIVACY.md",
    "docs/LIMITATIONS.md",
    "docs/MAINTAINERS.md",
    "verification/documentation-review.md",
]

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def validate_json(path: Path) -> list[str]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"invalid JSON {path.as_posix()}: {exc}"]
    if not isinstance(value, (dict, list)):
        return [f"invalid JSON root {path.as_posix()}: expected object or array"]
    return []


def validate_jsonl(path: Path) -> list[str]:
    errors: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except Exception as exc:
            errors.append(f"invalid JSONL {path.as_posix()}:{line_number}: {exc}")
            continue
        if not isinstance(value, dict):
            errors.append(
                f"invalid JSONL {path.as_posix()}:{line_number}: expected object"
            )
    return errors


def link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target:
        target = target.split(" ", 1)[0]
    return unquote(target.split("#", 1)[0])


def validate_markdown_links(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    checked = 0
    for markdown in sorted(root.rglob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = link_target(match.group(1))
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            checked += 1
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(
                    f"local Markdown link escapes package: {markdown.relative_to(root)} -> {target}"
                )
                continue
            if resolved.is_dir():
                continue
            if not resolved.is_file():
                errors.append(
                    f"broken local Markdown link: {markdown.relative_to(root)} -> {target}"
                )
    return errors, checked


def validate(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"missing {relative}")

    for relative, expected in EXPECTED_HASHES.items():
        path = root / relative
        if path.is_file() and sha256(path) != expected:
            errors.append(f"canonical hash mismatch: {relative}")

    for path in sorted(root.rglob("*.json")):
        errors.extend(validate_json(path))
    for path in sorted(root.rglob("*.jsonl")):
        errors.extend(validate_jsonl(path))

    link_errors, link_count = validate_markdown_links(root)
    errors.extend(link_errors)

    if any(path.name == "__pycache__" for path in root.rglob("*")):
        errors.append("package contains __pycache__")
    return errors, link_count


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    root = root.resolve()
    errors, link_count = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    files = sum(1 for path in root.rglob("*") if path.is_file())
    print(f"VALID: {root}")
    print(f"FILES: {files}")
    print(f"CANONICAL_HASHES: {len(EXPECTED_HASHES)} matched")
    print(f"MARKDOWN_LINKS: {link_count} checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
