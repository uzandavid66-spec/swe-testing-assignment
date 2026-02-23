from decimal import Decimal

import pytest

from quickcalc.calculator import (
    DivisionByZeroError,
    add,
    divide,
    multiply,
    subtract,
    to_decimal,
)


def test_to_decimal_from_int():
    assert to_decimal(5) == Decimal("5")


def test_to_decimal_from_str_decimal():
    assert to_decimal("3.14") == Decimal("3.14")


def test_addition_simple():
    assert add(5, 3) == Decimal("8")


def test_subtraction_simple():
    assert subtract(10, 4) == Decimal("6")


def test_multiplication_simple():
    assert multiply(6, 7) == Decimal("42")


def test_division_simple():
    assert divide(9, 3) == Decimal("3")


def test_division_by_zero_raises():
    with pytest.raises(DivisionByZeroError):
        divide(1, 0)


def test_negative_numbers():
    assert add(-5, -3) == Decimal("-8")
    assert subtract(-5, 3) == Decimal("-8")


def test_decimal_numbers():
    assert add("0.1", "0.2") == Decimal("0.3")
    assert divide("1.5", "0.5") == Decimal("3")


def test_very_large_numbers():
    big = "999999999999999999999999"
    assert add(big, "1") == Decimal("1000000000000000000000000")