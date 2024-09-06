import random
from Circle import Circle
from Rectangle import Rectangle
from Square import Square


class ShapeWarehouse:
    COLORS = ["red", "green", "blue", "yellow", "purple"]
    SIDE_LENGTHS = range(1, 11)  # Lengths from 1 to 10

    def __init__(self):
        """
        initiate the shape warehouse with empty list of shapes
        """
        self.shapes = []

    def generate(self, x):
        """
        generate a chosen number of random shapes with random qualities
        :param x: the number of generated random shapes
        :return:
        """
        for _ in range(x):
            shape_type = random.choice([Rectangle, Square, Circle])
            color = random.choice(self.COLORS)
            if shape_type == Circle:
                radius = random.choice(self.SIDE_LENGTHS)
                self.shapes.append(Circle(radius, color))
            elif shape_type == Rectangle:
                side1 = random.choice(self.SIDE_LENGTHS)
                side2 = random.choice(self.SIDE_LENGTHS) if shape_type == Rectangle else side1
                self.shapes.append(shape_type(side1, side2, color))
            elif shape_type == Square:
                side_length = random.choice(self.SIDE_LENGTHS)
                self.shapes.append(shape_type(side_length, color))

    def sum_areas(self):
        """
        get the area sum of all shapes in the shape warehouse
        :return:
        """
        return sum(shape.area() for shape in self.shapes)

    def sum_perimeters(self):
        """
        get the perimeters sum of all shapes in the shape warehouse
        :return:
        """
        return sum(shape.circumference() for shape in self.shapes)

    def count_colors(self):
        """
        get the color count sum of all the shapes in the shape warehouse
        :return: a list of all the different color and their count
        """
        color_count = {}
        for shape in self.shapes:
            color = shape.get_color()
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
        return color_count
