from src.calculator import Calculator


class TestCalculator:

    @staticmethod
    def test_add() -> None:
        assert Calculator.add(number1=10, number2=20) == 30

    @classmethod
    def test_subtract(cls) -> None:
        assert Calculator.subtract(number1=10, number2=20) == 10

    def test_multiply(self) -> None:
        assert Calculator.multiply(number1=10, number2=20) == 200

    def test_divide(self) -> None:
        assert Calculator.divide(number1=10, number2=20) == 0

    # Expecting Failure
    def test_divide_by_zero(self) -> None:
        assert Calculator.divide(number1=10, number2=0) == float("inf")
