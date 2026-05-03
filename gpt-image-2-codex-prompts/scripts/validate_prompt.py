#!/usr/bin/env python3
"""Validate a Codex-only GPT Image 2 prompt for this skill.

This script checks for common prompt-package mistakes:
- missing aspect ratio
- use of API/client/curl terminology
- aspect ratio outside the requested 3:1 to 1:3 range

It does not judge artistic quality or platform safety policy.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BANNED_PATTERNS = [
    r"\bcurl\b",
    r"\bapi[_ -]?key\b",
    r"\bauthorization:\s*bearer\b",
    r"\bapi\.openai\.com\b",
    r"\bimages/generations\b",
    r"\bimages/edits\b",
    r"\bopenai\s*\(",
    r"\bfrom\s+openai\s+import\b",
    r"\bclient\.images\b",
    r"\bresponses\.create\b",
]

RATIO_RE = re.compile(r"(?i)(?:aspect\s*ratio|ar|ratio)\s*[:=\-]?\s*(\d+(?:\.\d+)?)\s*:\s*(\d+(?:\.\d+)?)")


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8")
    if args.prompt:
        return args.prompt
    return sys.stdin.read()


def validate(prompt: str) -> list[str]:
    errors: list[str] = []
    text = prompt.strip()
    if not text:
        return ["prompt is empty"]

    for pattern in BANNED_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"contains API/Codex-only banned pattern: {pattern}")

    match = RATIO_RE.search(text)
    if not match:
        errors.append("missing aspect ratio, e.g. 'Aspect ratio: 16:9'")
    else:
        w = float(match.group(1))
        h = float(match.group(2))
        if h == 0:
            errors.append("aspect ratio height cannot be zero")
        else:
            numeric_ratio = w / h
            if numeric_ratio > 3.0 or numeric_ratio < (1.0 / 3.0):
                errors.append("aspect ratio must be between 3:1 and 1:3")

    if len(text) > 6000:
        errors.append("prompt is unusually long; consider reducing keyword clutter")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Codex-only GPT Image 2 prompt")
    parser.add_argument("--prompt-file", help="path to a text file containing the prompt")
    parser.add_argument("--prompt", help="prompt text to validate")
    args = parser.parse_args()

    prompt = read_prompt(args)
    errors = validate(prompt)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
