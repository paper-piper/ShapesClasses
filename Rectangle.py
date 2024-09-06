from Shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height, color=None):
        """
        initiate the rectangle with a height, width and color (optional)
        :param width:
        :param height:
        :param color:
        """
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        """
        calculate the area of the rectangle
        :return: the area
        """
        return self.width * self.height

    def circumference(self):
        """
        calculate the circumference of the rectangle
        :return: the circumference
        """
        return 2 * (self.width + self.height)

    def join(self, other):
        """
        combine two rectangle shapes together by "joining" them together
        :param other: the other shape to combine
        :return: the new shape
        """
        if not isinstance(other, Rectangle):
            raise ValueError("Can only join with another Rectangle or Square")

        if self.width == other.width:
            return Rectangle(self.width, self.height + other.height)
        elif self.height == other.height:
            return Rectangle(self.width + other.width, self.height)
        elif self.width == other.height:
            return Rectangle(self.width, self.height + other.width)
        elif self.height == other.width:
            return Rectangle(self.width + other.height, self.height)
        else:
            raise ValueError("No matching edge to join")
