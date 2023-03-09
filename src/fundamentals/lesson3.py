""" Lesson 3 - All about Strings
Objectives
- What are strings?
- Getting a range of a string
- Concatenation
- The format method
- String Interpolation
- String methods
- Escape Characters
"""

""" What is a String?
A string is a sequence of Unicode Characters. It is defined with either
a single quote or double quote and can be letters, numbers, or characters.
"""
alpha = 'Hello'
apple: str = 'Red'

beta = "Python"
ball: str = "Blue"


def my_index_example(value: str):
    print(value[2])


my_index_example("Super")


""" Slicing allows to choose different ways to get
info from a string. Using index format.
"""
delta: str = 'Enjoy Python'


def get_pos_value():
    print(delta[2:6])


def get_neg_value():
    print(delta[-5:-2])


def get_value_left():
    print(delta[3:])


def get_value_right():
    print(delta[:6])


def get_increment_value():
    print(delta[2:7:2])


get_pos_value()
get_neg_value()
get_value_left()
get_value_right()
get_increment_value()


""" String Concatenation is the joining of strings.
This does include empty spaces, but not numbers.
"""
sample: str = 'Programming is'
sample2: str = 'fun'


def basic_concat() -> str:
    fox: str = 'for everyone'
    return sample + " " + sample2 + " " + fox


def concat_literal():
    cat3: str = 'Sample'
    combine = cat3 + ' Code'
    print(combine)


reveal: str = basic_concat()
print(reveal)
# only works if the function has a return
print(basic_concat())
print(concat_literal())
