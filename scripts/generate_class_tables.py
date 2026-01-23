#!/usr/bin/env python3
"""Generate class_tables.md with base/derived class breakdowns."""

from __future__ import annotations

import ast
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


BASE_DIRS: Dict[str, Path] = {
    "anemoi-graphs": Path("graphs/src/anemoi/graphs"),
    "anemoi-models": Path("models/src/anemoi/models"),
    "anemoi-training": Path("training/src/anemoi/training"),
}

ABC_BASE_TOKENS = {"ABC", "abc.ABC", "ABCMeta", "abc.ABCMeta"}
MODULE_BASE_TOKENS = {"Module", "nn.Module", "torch.nn.Module"}

OUT_PATH = Path("class_tables.md")


def parse_bases(node: ast.ClassDef) -> List[str]:
    bases: List[str] = []
    for base in node.bases:
        if isinstance(base, ast.Name):
            bases.append(base.id)
        elif isinstance(base, ast.Attribute):
            parts: List[str] = []
            cur = base
            while isinstance(cur, ast.Attribute):
                parts.append(cur.attr)
                cur = cur.value
            if isinstance(cur, ast.Name):
                parts.append(cur.id)
            dotted = ".".join(reversed(parts))
            bases.append(dotted if dotted else base.attr)
        else:
            if hasattr(ast, "unparse"):
                bases.append(ast.unparse(base))
            else:
                bases.append("<expr>")
    return bases


def compute_derived_set(
    name_to_bases: Dict[str, List[List[str]]], direct_tokens: Iterable[str]
) -> set[str]:
    derived: set[str] = set()
    for cls, bases_list in name_to_bases.items():
        if any(any(b in direct_tokens for b in bases) for bases in bases_list):
            derived.add(cls)
    changed = True
    while changed:
        changed = False
        for cls, bases_list in name_to_bases.items():
            if cls in derived:
                continue
            if any(any(b in derived for b in bases) for bases in bases_list):
                derived.add(cls)
                changed = True
    return derived


def get_git_hash() -> str:
    head = Path(".git/HEAD")
    if not head.exists():
        return "unknown"
    content = head.read_text(encoding="utf-8").strip()
    if content.startswith("ref: "):
        ref = content.split(" ", 1)[1].strip()
        ref_path = Path(".git") / ref
        if ref_path.exists():
            return ref_path.read_text(encoding="utf-8").strip()[:7]
    return content[:7] if content else "unknown"


def main() -> None:
    results: Dict[str, List[Tuple[str, List[str], Path]]] = {}

    for name, base in BASE_DIRS.items():
        classes: List[Tuple[str, List[str], Path]] = []
        for path in base.rglob("*.py"):
            try:
                src = path.read_text(encoding="utf-8")
            except Exception:
                src = path.read_text()
            try:
                tree = ast.parse(src, filename=str(path))
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    bases = parse_bases(node)
                    classes.append((node.name, bases, path))
        results[name] = classes

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")
    git_hash = get_git_hash()

    lines: List[str] = []
    lines.append("# Anemoi Class Inventory\n\n")
    lines.append(
        "Class inventory for anemoi graphs, models, and training modules, "
        "listing base/derived classes, files, and markers for abstract and torch "
        "module inheritance.\n"
    )
    lines.append(f"Built on {now}, commit {git_hash}.\n\n")

    lines.append("Table of contents:\n\n")
    lines.append("| Module | Base count | Non-base count |\n")
    lines.append("| --- | --- | --- |\n")

    section_counts: Dict[str, Tuple[int, int]] = {}
    for name, classes in results.items():
        name_to_bases: Dict[str, List[List[str]]] = {}
        for cls, bases, _ in classes:
            name_to_bases.setdefault(cls, []).append(bases)
        abc_derived = compute_derived_set(name_to_bases, ABC_BASE_TOKENS)

        base_rows = [c for c in classes if len(c[1]) == 0 or c[0] in abc_derived]
        derived_rows = [c for c in classes if not (len(c[1]) == 0 or c[0] in abc_derived)]
        section_counts[name] = (len(base_rows), len(derived_rows))

    for name, (base_count, derived_count) in section_counts.items():
        anchor = name.replace(" ", "-").lower()
        lines.append(f"| [{name}](#{anchor}) | {base_count} | {derived_count} |\n")

    lines.append("\n")

    for name, classes in results.items():
        name_to_bases: Dict[str, List[List[str]]] = {}
        for cls, bases, _ in classes:
            name_to_bases.setdefault(cls, []).append(bases)

        abc_derived = compute_derived_set(name_to_bases, ABC_BASE_TOKENS)
        module_derived = (
            compute_derived_set(name_to_bases, MODULE_BASE_TOKENS)
            if name == "anemoi-models"
            else set()
        )

        base_rows = []
        derived_rows = []
        for cls, bases, path in classes:
            is_base = len(bases) == 0 or cls in abc_derived
            if is_base:
                base_rows.append((cls, bases, path))
            else:
                derived_rows.append((cls, bases, path))

        base_rows = sorted(base_rows, key=lambda x: (x[0].lower(), str(x[2])))
        derived_rows = sorted(derived_rows, key=lambda x: (x[0].lower(), str(x[2])))

        lines.append(f"## {name}\n")
        lines.append(f"Base classes (no explicit base or ABC-derived): {len(base_rows)}\n")
        lines.append("| Class | File |\n")
        lines.append("| --- | --- |\n")
        for cls, _, path in base_rows:
            mark = ""
            if cls in abc_derived:
                mark = "*"
            if name == "anemoi-models" and cls in module_derived and cls in abc_derived:
                mark = "*\u2020"
            lines.append(f"| {cls}{mark} | {path} |\n")
        lines.append("\n")
        lines.append("* indicates abstract base class (derives from ABC).")
        if name == "anemoi-models":
            lines.append(" \u2020 indicates class derives from ABC and torch.nn.Module.")
        lines.append("\n\n")

        if name == "anemoi-models":
            module_derived_rows = [c for c in derived_rows if c[0] in module_derived]
            other_derived_rows = [c for c in derived_rows if c[0] not in module_derived]

            lines.append(
                "Derived from torch.nn.Module (direct or indirect): "
                f"{len(module_derived_rows)}\n"
            )
            lines.append("| Class | Base(s) | File |\n")
            lines.append("| --- | --- | --- |\n")
            for cls, bases, path in module_derived_rows:
                mark = "\u2020" if cls in abc_derived else ""
                lines.append(f"| {cls}{mark} | {', '.join(bases)} | {path} |\n")
            lines.append("\n")
            lines.append("\u2020 indicates class derives from ABC and torch.nn.Module.")
            lines.append("\n\n")

            lines.append(
                "Other derived classes (explicit base list): "
                f"{len(other_derived_rows)}\n"
            )
            lines.append("| Class | Base(s) | File |\n")
            lines.append("| --- | --- | --- |\n")
            for cls, bases, path in other_derived_rows:
                lines.append(f"| {cls} | {', '.join(bases)} | {path} |\n")
            lines.append("\n")
        else:
            lines.append(f"Derived classes (explicit base list): {len(derived_rows)}\n")
            lines.append("| Class | Base(s) | File |\n")
            lines.append("| --- | --- | --- |\n")
            for cls, bases, path in derived_rows:
                lines.append(f"| {cls} | {', '.join(bases)} | {path} |\n")
            lines.append("\n")

    OUT_PATH.write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
