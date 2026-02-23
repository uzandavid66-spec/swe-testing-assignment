from __future__ import annotations

import sys
from decimal import Decimal, InvalidOperation
from typing import Callable, Dict, List

from quickcalc.calculator import (
    DivisionByZeroError,
    add,
    divide,
    multiply,
    subtract,
)


OPS: Dict[str, Callable[[object, object], Decimal]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def evaluate_tokens(tokens: List[str]) -> str:
    """
    Evaluate a simple expression: <number> <op> <number>
    Example: ["5", "+", "3"] -> "8"
    Returns a string display value.
    """
    if len(tokens) != 3:
        return "ERROR"

    left, op, right = tokens
    if op not in OPS:
        return "ERROR"

    try:
        result = OPS[op](left, right)
        # normalize: show integers without trailing .0
        if result == result.to_integral():
            return str(result.to_integral())
        return str(result.normalize())
    except (InvalidOperation, DivisionByZeroError):
        return "ERROR"


def main(argv: List[str] | None = None) -> int:
    """
    CLI modes:
      - Interactive: python -m quickcalc.cli
      - One-shot:    python -m quickcalc.cli 5 + 3
    """
    argv = sys.argv[1:] if argv is None else argv

    if len(argv) == 3:
        print(evaluate_tokens(argv))
        return 0

    print("Quick-Calc CLI")
    print("Enter: <number> <op> <number>  (e.g., 5 + 3)")
    print("Commands: C (clear), q (quit)")

    while True:
        raw = input("> ").strip()
        if raw.lower() == "q":
            return 0
        if raw.upper() == "C":
            print("0")
            continue
        tokens = raw.split()
        print(evaluate_tokens(tokens))


if __name__ == "__main__":
    raise SystemExit(main())