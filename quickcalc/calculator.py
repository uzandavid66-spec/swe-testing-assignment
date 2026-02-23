from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Union


NumberLike = Union[int, float, str, Decimal]


class DivisionByZeroError(ZeroDivisionError):
    """Raised when attempting to divide by zero."""


def to_decimal(value: NumberLike) -> Decimal:
    """
    Convert input to Decimal using str() to avoid float precision surprises.
    Accepts int, float, str, Decimal.
    """
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def add(a: NumberLike, b: NumberLike) -> Decimal:
    return to_decimal(a) + to_decimal(b)


def subtract(a: NumberLike, b: NumberLike) -> Decimal:
    return to_decimal(a) - to_decimal(b)


def multiply(a: NumberLike, b: NumberLike) -> Decimal:
    return to_decimal(a) * to_decimal(b)


def divide(a: NumberLike, b: NumberLike) -> Decimal:
    denominator = to_decimal(b)
    if denominator == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return to_decimal(a) / denominator


@dataclass
class CalculatorState:
    display: Decimal = Decimal("0")

    def clear(self) -> None:
        self.display = Decimal("0")