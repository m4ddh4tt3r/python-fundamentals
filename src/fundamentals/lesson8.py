""" Lesson 8 collections part 1 """


""" List collection using []. Allows duplicates,
is changeable. and is an ordered list.
"""
colors = ['green', 'red', 'blue', 'magenta', 'yellow',
          'orange', 'purple', 'black', 'gray']
trucks = ['chevy', 'ford', 'doge', 'toyota', 'nissan', 'jeep']


""" this list collection has different data types, duplicates,
and another list.
"""
my_list = [42, 'Happy', 'Python', True, colors, 'Happy']


def example_direct():
    """ Print the list directly will provide a result
    that mirrors the list directly. including brackets and
    how each type was entered into the list.
    """
    print(colors)


# example_direct()


def example_for():
    """ To print a list it is best to use a (for) loop. """
    for color in colors:
        print(color)


# example_for()


def single_item():
    """ To get a single item from a list, you use bracket
    notation and the index number.
    """
    print(colors[2])


# single_item()


def slice_list():
    """ Slicing will get a range of values from the list.
    This list includes a start and stop index. These items
    are added to a new variable as its own list.
    """
    examples = my_list[1:4]
    print(examples)
    for value in examples:
        print(value)


# slice_list()


def negative_slice():
    """ This slice uses negative numbers. It begins
    from -1 instead of 0 when it comes to the first item.
    """
    example2 = my_list[-4:-2]
    print(example2)
    for value in example2:
        print(value)


negative_slice()
