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
    total: str = sample + " " + sample2 + " " + fox
    return total


def concat_literal():
    cat3: str = 'Sample'
    combine = cat3 + ' Code'
    print(combine)


reveal: str = basic_concat()
print(reveal)
# only works if the function has a return
print(basic_concat())
print(concat_literal())


"""
String format is a method that allows strings or other data types
to be combined with each other using curly braces as placeholders.
"""


def basic_string_format(value: int):
    msg1: str = 'My dog is {} years old'
    print(msg1.format(value))


def other_string_format(name: str, age: int):
    msg2 = 'My dog {1} is {0} years old'
    print(msg2.format(age, name))


basic_string_format(5)
other_string_format('Spot', 4)


""" The f-string uses expressions within the string directly, it
also can use the same mini-programming as the format function.
Essentially the interpreter runs the format function itself.
 The f-string also uses placeholder curly braces.
 """


def basic_fstring(name: str, snack: str, num_snacks: int):
    print(f'My name is {name} and my favorite snack is {snack}')
    print(f'i eat {num_snacks} snacks per day, I should cut down')
    like: str = f'I like {snack} type snacks'
    print(like)


basic_fstring('Tom', 'Chocolate', 5)

""" String methods are methods built-in to strings to create
new values of the string. There are more than what we will write below.
"""
method_sample: str = ' Hello, Python '

# strip()
print(method_sample.strip())

# lower()
print(method_sample.lower())

# upper()
print(method_sample.upper())

# replace()
print(method_sample.replace('l', 'z'))

# split()
print(method_sample.split(','))


def basic_escape_seq():
    value_n: str = 'My name Roger O\'Dell. \tHow are\n you doing today?'
    print(value_n)


basic_escape_seq()
