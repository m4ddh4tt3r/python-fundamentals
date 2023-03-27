"""lesson - 7 Looping statements """


def basic_while():
    """ Basic (while) loop that has an initialized value,
    condition, and increment using number values
    """
    num = 0
    while num < 10:
        print('Happy Python')
        num += 1


# basic_while()


def other_while():
    """ This (while) loop takes a string and uses the
    (len) function to get its length. The (print) uses the
    index of the string to provide output of a single
    character. """
    value = 'happy day'
    num = 0
    while num < len(value):
        print(value[num])
        num += 1


# other_while()


def basic_for():
    """ A basic (for) loop that iterates through a sequence.
    The (in) keyword indicates the individual characters of
    the string and assign them to the variable. It will
    continue until the sequence ends.
    """
    value = 'Python rocks'
    for single in value:
        print(single)


# basic_for()


def other_for():
    """ This (for) loop includes an (if) statement.
    """
    value = 'Will this be cool'
    for single in value:
        if single == 'i':
            print('This will be cool')
        print(single)


# other_for()


def basic_range():
    """ This basic range function takes the end value
    and iterates through the (for) loop from 0 to 9
    and prints the values of the range.
    """
    for able in range(4, 11):
        print(able)


# basic_range()


def other_range():
    """ This (range) function takes both a start and stop
    argument. It can accept negative values. The start
    value has to be smaller than the stop for positive values.
    Otherwise, you get an empty result.
    """
    for able in range(-1, -11):
        print(able)


# other_range()


def more_range():
    """ This example of (range) includes the (step) argument.
    The (step) determines the increment of the (range).
    """
    for beta in range(0, 30, 5):
        print(beta)


# more_range()


def nested_for():
    """ This nested (for) loop defines an outer and inner
    (for) loop. For every outer loop, the inner loop will
    iterate through its whole sequence.
    """
    for outer in range(1, 11):
        for inner in range(1, 11):
            print(outer * inner, end=' ')
        print()


# nested_for()


def break_while():
    """ This (while) loop uses the (break) statement
    to end the loop based on an (if) condition.
    """
    num: int = 0
    while num < 10:
        if num == 5:
            break
        print(num)
        num += 1


# break_while()


def break_for():
    """ This (for) loop uses the break statement to end
    the loop on an (if) condition.
    """
    for value in range(10):
        if value == 4:
            break
        print(value)


# break_for()


def continue_while():
    """ This (while) loop uses a (continue) statement
    to skip a loop and begin another loop.
    """
    num: int = 0
    while num < 10:
        if num == 5:
            continue
        print(num)
        num += 1


# continue_while()


def continue_for():
    """ This (for) loop uses a (continue) statement
    to skip an iteration of the loop based on an
    (if) statement and begins another iteration.
    """
    for letters in 'Python Lesson 7':
        if letters == 'o':
            continue
        print(letters)


# continue_for()


def example_else():
    """ This (while) loop uses an (else) statement to
    perform a block once the loop ends. The else
    statement will not execute if a break statement
    is used in thr loop.
    """
    value: str = 'Learning Python Loops'
    num: int = 0
    while num < len(value):
        print(value[num])
        num += 1
    else:
        print('Last topic complete')


example_else()
