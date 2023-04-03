""" Lesson 10 - Classes and methods """
""" a (class) is an object or blueprint. defined with 
the keyword (class) followed by the name, which should
be Pascal Case or Upper Camel Case: Each word capitalized.
"""


class Cat:
    def __init__(self, name: str):
        self.name = name

    def move(self):
        print(f'{self.name} can move fast.')


def example_key_arg(firstname: str, lastname: str):
    """ keyword arguments are a way to change the
    order of how you call a method or function.
    """
    print(f'Welcome {firstname} {lastname}')


def example_arg(*args: int):
    """ the arbitrary argument will allow you to pass in a
    number of non-key worded variables into the function
    """
    for value in args:
        total = value + 10
        print(f'{value} + 10 = {total}')


def example_kwarg(**kwargs):
    """ this arbitrary argument ids like a dictionary
    in that it requires a key and value representing a single
    argument. the difference is how it is defined using = instead
    of an : """
    for key, value in kwargs.items():
        print(f'The {key} and {value} of the kwargs')


def example_default(value1: int, value2: int = 10):
    """ the default argument id a parameter that has a
    default literal assigned to it in a function or method.
    """
    total = value1 + value2
    print(f'{value1} + {value2} = {total}')


def example_args2(value: str, *args: str):
    print(f'The first argument is {value}')
    for message in args:
        print(f'Next argument in *args is {message}')


def main():
    """ Execute code here instead of directly. """
    alpha = Cat('Felix')
    beta = Cat('Garfield')
    # print(f'My cats are called {alpha.name} & {beta.name}')
    # alpha.move()
    # beta.move()
    # example_key_arg('Happy', 'Gilmore')
    # example_key_arg(lastname='Gilmore', firstname='Happy')
    # example_arg(4, 6, 8, 10, 12, 14, 16, 18)
    # example_kwarg(chevy='Silverado', ford='F150')
    # example_default(3, 5)
    # example_default(42)
    example_args2('first', 'second', 'third', 'fourth', 'fifth', 'sixth')


if __name__ == '__main__':
    main()
    # print(f'{__name__} within the if above')
