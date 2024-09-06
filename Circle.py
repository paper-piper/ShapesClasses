import math
from Shape import Shape


class Circle(Shape):
    def __init__(self, radius, color=None):
        """
        initiate the circle with radius and color (optional)
        :param radius:
        :param color:
        """
        super().__init__(color)
        self.radius = radius

    def area(self):
        """
        calculate the area of the circle
        :return: the area
        """
        return math.pi * self.radius ** 2

    def circumference(self):
        """
        calculate the circumference of the circle
        :return: the circumference
        """
        return 2 * math.pi * self.radius


# Asserting area calculation
assert Circle(5).area() == math.pi * 5 ** 2
# Asserting circumference calculation
assert Circle(5).circumference() == 2 * math.pi * 5
# Edge case: Zero radius
assert Circle(0).area() == 0
assert Circle(0).circumference() == 0

