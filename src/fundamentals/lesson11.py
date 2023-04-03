""" lesson 11 - encapsulation """
""" encapsulation is the concept of bundling data
and methods with ine class, but python has weak
encapsulation as it is not enforced.
"""


class MyClass:
    # protected
    _hi = 'Hello'

    def __init__(self):
        # private
        self.__value = 'World'


class Centimeter:
    """ constructor method """
    def __init__(self, size: float):
        self._size = size

    """ method to convert """
    def to_millimeters(self) -> float:
        return self._size * 10

    """ property decorator for size """
    @property
    def size(self) -> float:
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


class Feet:
    """ this (class) uses the (property) function style """
    def __init__(self, length):
        self._length = length

    # getter
    def get_length(self):
        return self._length

    # setter
    def set_length(self, value):
        self._length = value

    # delete
    def del_length(self):
        del self._length

    # creating property function
    length = property(get_length, set_length, del_length)

    # convert feet to inches
    def to_inches(self):
        return self.get_length() * 12


def example():
    measure = Feet(3)
    print(measure.length)
    print(measure.to_inches())
    measure.length = 32
    print(measure.to_inches())
    print(measure.get_length())


def main():
    """ starting point """
    # my_class = MyClass()
    # print(my_class._hi)
    # __value will cause an error
    # print(my_class.__value)
    my_measure = Centimeter(2)
    print(my_measure.size)
    print(my_measure.to_millimeters())
    my_measure.size = 4
    print(my_measure.to_millimeters())


if __name__ == '__main__':
    # main()
    example()
