#!/usr/bin/env python3
'''
@desc    description
@author  SDQ <sdq@afnor.org>
@version 0.0.1
@date    2020-03-24
@note    0.0.1 (2020-03-24) : Init file
'''
from typing import List, Tuple
import pytest
from calculator import Calculator


CalculatorValues = Tuple[int, int, int]


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


def add_values() -> List[CalculatorValues]:
    return [(1, 2, 3), (2, 3, 5), (3, 4, 7)]


def sub_values() -> List[CalculatorValues]:
    return [(2, 1, 1), (1, 2, -1), (1, -2, 3)]


def mul_values() -> List[CalculatorValues]:
    return [(2, 2, 4), (2, 0, 0)]


def div_values() -> List[CalculatorValues]:
    return [(2, 2, 1), (10, 5, 2)]


def div_values_float() -> List[CalculatorValues]:
    return [(1, 2, 0.5), (5, 2, 2.5)]


class TestCalculator:
    @pytest.mark.parametrize('a,b,result', add_values())
    def test_add(
        self, calculator: Calculator, a: int, b: int, result: int
    ) -> None:
        assert calculator.add(a, b) == result

    @pytest.mark.parametrize('a,b,result', sub_values())
    def test_sub(
        self, calculator: Calculator, a: int, b: int, result: int
    ) -> None:
        assert calculator.sub(a, b) == result

    @pytest.mark.parametrize('a,b,result', mul_values())
    def test_mul(
        self, calculator: Calculator, a: int, b: int, result: int
    ) -> None:
        assert calculator.mul(a, b) == result

    @pytest.mark.parametrize('a,b,result', div_values())
    def test_div_int(
        self, calculator: Calculator, a: int, b: int, result: int
    ) -> None:
        assert calculator.div(a, b) == result

    @pytest.mark.parametrize('a,b,result', div_values_float())
    def test_div_float(
        self, calculator: Calculator, a: int, b: int, result: int
    ) -> None:
        assert calculator.div(a, b) == result

    def test_div_zero_division(self, calculator: Calculator) -> None:
        with pytest.raises(ZeroDivisionError):
            calculator.div(1, 0)
