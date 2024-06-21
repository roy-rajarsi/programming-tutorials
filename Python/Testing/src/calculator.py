from time import sleep
from typing import Callable, Union


class Calculator:

    @staticmethod
    def add(number1: int, number2: int) -> int:
        return number1 + number2

    @staticmethod
    def subtract(number1: int, number2: int) -> int:
        return abs(number1 - number2)

    @staticmethod
    def multiply(number1: int, number2: int) -> int:
        return number1 * number2

    @staticmethod
    def slow_multiply(number1: int, number2: int) -> int:
        product: int = 0
        for _ in range(number2):
            product += number1
            sleep(2)
        return product

    @staticmethod
    def safe_divide(divide_function: Callable) -> Callable:
        def handle_zero_division_error(number1: int, number2: int) -> Union[int, float]:
            return float("inf") if number2 == 0 else divide_function(number1=number1, number2=number2)

        return handle_zero_division_error

    @staticmethod
    @safe_divide
    def divide(number1: int, number2: int) -> Union[int,float]:
        return number1 // number2

    @staticmethod
    def divide_zero_div_not_handled(number1: int, number2: int) -> Union[int,float]:
        return number1 // number2
