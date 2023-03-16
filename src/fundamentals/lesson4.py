""" Lesson 4 - All about Numbers """

""" Numeric types are broken down into 3 
distinct types: int, float, and complex
"""
# int
alpha = 42
beta = 816488888
charlie: int = -45679
delta: int = 12345678987654321

# float
echo = 3.14
foxtrot: float = 2.1
golf: float = -42.2

# complex
kilo = 3j
lamp: complex = 3 + 5j
marble: complex = -5j

# Scientific Notation
hotel: float = 25E4
indigo: float = 42.39
juliet: float = 98.6E2

""" Numeric Types - Binary, Decimal, Octal & Hexadecimal """


def numeric_types(value1: int):
    """ the below methods will provide the numeric
    type based on the argument supplied
    """
    print(bin(value1))
    print(oct(value1))
    print(hex(value1))
    print(value1)


""" Below functions represent Numeric types based
on the number 26.
"""


# binary
def basic_binary():
    print(0b11010)


# octal
def basic_octal():
    print(0o32)


# hexadecimal
def basic_hexadecimal():
    print(0x1a)


numeric_types(42)
basic_binary()
basic_octal()
basic_hexadecimal()

""" Numeric Separators
Improve readability of numbers using underscores.
"""
# group decimals by thousands
amount: float = 19_845.34

# group hexadecimals by words
addr: int = 0xCAF_F00D

# group binary in bits
flags: int = 0b_0011_1111_0100

print(amount)
print(addr)
print(flags)


""" Type Conversion
We can convert or explicit cast to different types
using the built-in python functions
"""


# int casting
def cast_int():
    value1 = int(echo)
    value2 = int(True)
    value3 = int('2378')
    value_i = int('01011', 8)
    print(f"Values = {value1}, {value2}, {value3}, & {value_i}")


cast_int()


# float casting
def cast_float():
    value4 = float(alpha)
    value5 = float(False)
    value6 = float('32.45')
    print(f"Values = {value4}, {value5}, & {value6}")


cast_float()


# complex casting
def cast_complex():
    value7 = complex(32, 3)
    value8 = complex(2.3, 4)
    value9 = complex(True, 2)
    value10 = complex('32')
    print(f"Values = {value7}, {value8}, {value9}. & {value10}")


cast_complex()


# bool casting
def cast_bool():
    value11 = bool(5)
    value12 = bool(2.5)
    value13 = bool(23+4j)
    value14 = bool('Python')
    print(f'Values = {value11}, {value12}, {value13}, & {value14}')


cast_bool()


# string casting
def cast_str():
    value15 = str(5)
    value16 = str(87.3345)
    value17 = str(34.34j)
    value18 = str(False)
    print(f'Values = {value15}, {value16}, {value17}, & {value18}')


cast_str()

""" Getting input from the user
the input function always returns a string, so type conversion
needs to be done for number values
"""


def basic_input_demo():
    name = input('What is your name?')
    height = int(input('What is your height in inches?'))
    feet = int(height / 12)
    inches = height % 12
    print(f'{name} is {feet} feet {inches} inches tall.')


basic_input_demo()
