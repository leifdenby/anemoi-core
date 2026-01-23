#!/usr/bin/env python3
"""Generate class_config_init_args.md for classes with config-like __init__ args."""

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

CONFIG_NAME_TOKENS = {"cfg", "conf", "config", "configuration", "hydra_config"}
CONFIG_TYPE_TOKENS = ["dictconfig", "omegaconf", "listconfig", "dotdict"]
PLAIN_DICT_TOKENS = ["dict", "mapping"]

OUT_PATH = Path("class_config_init_args.md")


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
    entries: Dict[Tuple[str, str], List[str]] = {}

    for module_name, base in BASE_DIRS.items():
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
                if not isinstance(node, ast.ClassDef):
                    continue
                class_name = node.name
                init_method = None
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and item.name == "__init__":
                        init_method = item
                        break
                if not init_method:
                    continue

                args = list(init_method.args.posonlyargs) + list(init_method.args.args)
                if args:
                    args = args[1:]
                kwonlyargs = list(init_method.args.kwonlyargs)
                all_args = args + kwonlyargs
                if not all_args:
                    continue

                for arg in all_args:
                    arg_name = arg.arg
                    name_lc = arg_name.lower()
                    anno = None
                    if arg.annotation is not None:
                        try:
                            anno = ast.unparse(arg.annotation)
                        except Exception:
                            anno = None
                    anno_lc = (anno or "").lower()

                    name_has_config = (
                        name_lc in CONFIG_NAME_TOKENS
                        or name_lc.endswith("config")
                        or "config" in name_lc
                    )
                    type_match = any(tok in anno_lc for tok in CONFIG_TYPE_TOKENS)
                    plain_dict_match = any(tok in anno_lc for tok in PLAIN_DICT_TOKENS)

                    if type_match or name_has_config or (plain_dict_match and name_has_config):
                        if plain_dict_match and not name_has_config and not type_match:
                            continue
                        if anno:
                            arg_display = f"{arg_name}: {anno}"
                        else:
                            arg_display = arg_name
                        arg_display = arg_display.replace("|", "\\|")
                        key = (module_name, class_name)
                        entries.setdefault(key, []).append(arg_display)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")
    git_hash = get_git_hash()

    lines: List[str] = []
    lines.append("# Anemoi Classes With Config __init__ Arguments\n\n")
    lines.append(
        "Class inventory for anemoi graphs, models, and training modules, "
        "listing classes whose __init__ takes config-like arguments.\n"
    )
    lines.append(f"Built on {now}, commit {git_hash}.\n\n")
    lines.append(f"Total classes: `{len(entries)}`\n\n")
    lines.append("| Class | __init__ argument(s) | Module |\n")
    lines.append("| --- | --- | --- |\n")

    for (module_name, class_name) in sorted(entries.keys(), key=lambda x: (x[0].lower(), x[1].lower())):
        args = entries[(module_name, class_name)]
        seen = set()
        unique_args: List[str] = []
        for arg in args:
            if arg in seen:
                continue
            seen.add(arg)
            unique_args.append(arg)
        arg_cell = ", ".join(f"`{arg}`" for arg in unique_args)
        lines.append(f"| `{class_name}` | {arg_cell} | `{module_name}` |\n")

    OUT_PATH.write_text("".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
