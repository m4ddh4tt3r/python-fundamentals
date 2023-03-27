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
