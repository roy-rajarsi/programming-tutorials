class Rectangle:

    def __init__(self, length: float, breadth: float) -> None:
        self.__length: float = length
        self.__breadth: float = breadth

    def get_length(self) -> float:
        return self.__length

    def get_breadth(self) -> float:
        return self.__breadth

    def set_length(self, length: float) -> None:
        self.__length = length

    def set_breadth(self, breadth: float) -> None:
        self.__breadth = breadth

    def get_area(self) -> float:
        return self.__length * self.__breadth

    def get_perimeter(self) -> float:
        return 2 * (self.__length + self.__breadth)

    @staticmethod
    def is_valid_rectangle(length: float, breadth: float) -> bool:
        return length >= breadth
