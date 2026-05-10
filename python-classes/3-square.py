#!/usr/bin/python3
"""Kvadratı təyin edən klass modulu."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Kvadratı ölçüsü ilə inisializasiya edir.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        self.size = size

    @property
    def size(self):
        """Kvadratın ölçüsünü götürmək üçün getter.

        Returns:
            Kvadratın ölçüsü.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin etmək üçün setter.

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini hesablayır.

        Returns:
            Kvadratın cari sahəsi.
        """
        return self.__size ** 2
