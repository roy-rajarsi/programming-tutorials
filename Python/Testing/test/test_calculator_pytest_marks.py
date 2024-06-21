from src.calculator import Calculator
from pytest import mark, raises


class TestCalculator:

    @staticmethod
    def test_divide() -> None:
        assert Calculator.divide(number1=10, number2=0)

    @staticmethod
    @mark.slow
    def test_slow_multiply() -> None:
        number1: int = 10
        number2: int = 5
        assert Calculator.slow_multiply(number1=number1, number2=number2) == Calculator.multiply(number1=number1, number2=number2)

    @staticmethod
    @mark.skip
    def test_divide_zero_div_not_handled_skipped() -> None:
        assert Calculator.divide(number1=10, number2=0)

    @staticmethod
    @mark.xfail
    def test_divide_zero_div_not_handled_expecting_failure() -> None:
        assert Calculator.divide(number1=10, number2=0)

    @staticmethod
    def test_divide_zero_div_not_handled_exception_handling() -> None:
        with raises(expected_exception=ZeroDivisionError):
            assert Calculator.divide_zero_div_not_handled(number1=10, number2=0)

    @staticmethod
    @mark.parametrize(argnames=('number1', 'number2', 'expected_sum'), argvalues=((10, 10, 20), (30, 40, 70)))
    def test_addition_with_params(number1: int, number2: int, expected_sum: int) -> None:
        assert Calculator.add(number1=number1, number2=number2) == expected_sum
