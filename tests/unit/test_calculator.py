#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-24
@note    0.0.1 (2020-03-24) : Init file
'''
import pytest
from calculator import Calculator


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


class TestCalculator:
    def test_add(self, calculator: Calculator) -> None:
        assert calculator.add(1, 2) == 3
        assert calculator.add(3, 4) == 7

    def test_sub(self, calculator: Calculator) -> None:
        assert calculator.sub(2, 1) == 1
        assert calculator.sub(1, 2) == -1
        assert calculator.sub(1, -2) == 3

    def test_mul(self, calculator: Calculator) -> None:
        assert calculator.mul(2, 2) == 4
        assert calculator.mul(2, 0) == 0

    def test_div_int(self, calculator: Calculator) -> None:
        assert calculator.div(2, 2) == 1
        assert calculator.div(10, 5) == 2

    def test_div_float(self, calculator: Calculator) -> None:
        assert calculator.div(1, 2) == 0.5

    def test_div_zero_division(self, calculator: Calculator) -> None:
        with pytest.raises(ZeroDivisionError):
            calculator.div(1, 0)
