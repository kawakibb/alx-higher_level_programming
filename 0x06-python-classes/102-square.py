#!/usr/bin/python3

class Square:
    """Represents a square

    """
    def __init__(self, size=0):
        """initializes the square

        Args:
            size (int): size of a side of the square
        """
        self.size = size

    def area(self):
        """calculates the square's area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """Compare if square is less than another by area
        Args:
            other (Square): square to compare against
        """
        return self.size < other.size

    def __le__(self, other):
        """Compare if square is less than or equal to another by area

        Args:
            other (Square): square to compare against
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Compare if square is equal to another by area
        Args:
            other (Square): square to compare against
        """
        return self.size == other.size

    def __ne__(self, other):
        """Compare if square is not equal to another by area
        Args:
            other (Square): square to compare against
        """
        return self.size != other.size

    def __ge__(self, other):
        """Compare if square is greater than or equal to another by area
        Args:
            other (Square): square to compare against
        """
        return self.size >= other.size

    def __gt__(self, other):
        """Compare if square is greater than another by area
        Args:
            other (Square): square to compare against
        """
        return self.size > other.size
