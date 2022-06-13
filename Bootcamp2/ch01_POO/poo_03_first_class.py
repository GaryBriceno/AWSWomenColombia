class MyFirstClass:
    pass


a = MyFirstClass()
print(type(a))


class Point:

    # Define a method is similar to define a function.
    # The self argument to a method is a reference to the object that the method is being invoked on.
    def reset(self):
        self.x = 0
        self.y = 0


p = Point()
p.reset()
print(p.x, p.y)


import math


class BetterPoint:

    def __init__(self):
        self.x = None
        self.y = None

    # Using hints
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # Define a method is similar to define a function.
    # The self argument to a method is a reference to the object that the method is being invoked on.
    def reset(self):
        self.x = 0
        self.y = 0


# Implementing Inheritance in Python
class InheritancePoint(BetterPoint):

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


# MyPy is a tools for check type hints
# >mypy --strict src/*.py
class PointDocString:
    """
    Represents a point in two-dimensional geometric coordinates
    >>> p_0 = Point()
    >>> p_1 = Point(3, 4)
    >>> p_0.calculate_distance(p_1)
    5.0
    """
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin.
        :param x: float x-coordinate
        :param y: float x-coordinate
        """
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Move the point to a new location in 2D space.
        :param x: float x-coordinate
        :param y: float x-coordinate
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Reset the point back to the geometric origin: 0, 0
        """
        self.move(0, 0)

    def calculate_distance(self, other: "Point") -> float:
        """
        Calculate the Euclidean distance from this point
        to a second point passed as a parameter.
        :param other: Point instance
        :return: float distance
        """
        return math.hypot(self.x - other.x, self.y - other.y)


# >python -i point.py
# help(Point)<enter>


