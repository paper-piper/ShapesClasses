from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color=None):
        """
        base initiator for a shape
        :param color:
        """
        self._color = color

    def set_color(self, color):
        """
        set a color for the shape
        :param color: the color to set
        :return:
        """
        self._color = color

    def get_color(self):
        """
        get the shape's color
        :return: the color
        """
        return self._color

    @abstractmethod
    def area(self):
        """
        get the shape's area
        :return: the area
        """
        pass

    @abstractmethod
    def circumference(self):
        """
        get the shape's circumference
        :return: the circumference
        """
        pass
