from src.rectangle import Rectangle
from pytest import fixture


class TestRectangle:

    def setup_method(self) -> None:
        print(f'Initializing Rectangle ...')
        self.rectangle: Rectangle = Rectangle(length=20, breadth=10)
        print(f'Test Setup Completed ....')

    def test_area(self) -> None:
        assert self.rectangle.get_area() == 200

    def test_perimeter(self) -> None:
        assert self.rectangle.get_perimeter() == 60

    def teardown_method(self) -> None:
        print(f'Deleting Rectangle -> {self.rectangle}')
        del self.rectangle
        print(f'Test Teardown Completed...')


# fixtures demo
@fixture
def get_rectangle() -> Rectangle:
    return Rectangle(length=20, breadth=10)


def test_area(get_rectangle) -> None:
    assert get_rectangle.get_area() == 200


def test_perimeter(get_rectangle) -> None:
    assert get_rectangle.get_perimeter() == 60
