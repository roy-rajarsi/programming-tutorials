from src.calculator import Calculator


def test_add() -> None:
    assert Calculator.add(number1=10, number2=20) == 30


def test_subtract() -> None:
    assert Calculator.subtract(number1=10, number2=20) == 10


def test_multiply() -> None:
    assert Calculator.multiply(number1=10, number2=20) == 200


def test_divide() -> None:
    assert Calculator.divide(number1=10, number2=20) == 0


# Expecting Failure
def test_divide_by_zero() -> None:
    assert Calculator.divide(number1=10, number2=0) == float("inf")
