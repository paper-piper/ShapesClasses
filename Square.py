from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_length, color=None):
        """
        initiate the square with length and color (optional)
        :param side_length:
        :param color:
        """
        super().__init__(side_length, side_length, color)
