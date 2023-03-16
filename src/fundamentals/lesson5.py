""" Lesson 5 - Operators """

""" Arithmetic Operators """
alpha: int = 10
beta: int = 5


def basic_math(value1: int, value2: int):
    """ Basic mathe values calculate from left to
    right, then assigned to a variable
    """
    total_add = value1 + value2
    total_sub = value1 - value2
    total_multi = value1 * value2
    total_divide = value1 / value2
    print(f"{value1} = {value2} = {total_add}")
    print(f"{value1} - {value2} = {total_sub}")
    print(f"{value1} * {value2} = {total_multi}")
    print(f"{value1} / {value2} = {total_divide}")


basic_math(alpha, beta)


# Modulus
def math_modulus(value3: int, value4: float) -> float:
    """ The modulus returns the remainder of a division
    problem. If you input a float value, you will return
    a float value """
    return value3 % value4


total_mod = math_modulus(alpha, 24.5)
print(total_mod)


# Exponent
def math_expon(value5, value6):
    """ The exponent will raise the value of the first
    operand to the power of the second """
    return value5 ** value6


total_exp = math_expon(10, 5)
print(total_exp)


# Floor division
def math_floor(value7, value8):
    """ Floor division is division with
    no remainder provided. Integer answers """
    return value7 // value8


total_floor = math_floor(32, 9)
print(total_floor)


# PEMDAS
def math_order():
    """ This function demonstrates order of operation """
    pem1 = 10 / (3 + 5) * 4 + 5 ** 2 + 6 - 9
    pem2 = 10 / 3 + 5 * 4 + 5 ** 2 + 6 - 9
    print(f"With () {pem1}, without {pem2}")


math_order()


def assign_op(value1, value2):
    """ Assignment Operators use one of the variables
    to reassign values to instead of assigning to
    a new variable. What ever the value was, will
    be replaced with the new calculated value.
    """
    print(f"Value1 before {value1}")
    value1 += value2
    print(f"Value1 after + {value1}")
    value1 -= value2
    print(f"Value1 after - {value1}")
    value1 *= value2
    print(f"Value1 after * {value1}")
    value1 /= value2
    print(f"Value1 after / {value1}")


assign_op(10, 5)


# Assignment operator for modulus
def assign_modulus():
    value100 = 100
    value100 %= 10
    print(value100)


assign_modulus()


# Assignment operator exponents
def assign_expon():
    num1 = 10
    # num1 = num1 ** 5
    num1 **= 5
    print(num1)


assign_expon()


# Assignment operator for Floor division
def assign_floor():
    value54 = 54
    value54 //= 5
    print(value54)


assign_floor()


def compare_op(value1, value2):
    """Comparison operators compare teo values with
    a result of True or False """
    print(f'{value1} == {value2} = {value1 == value2}')
    print(f'{value1} != {value2} = {value1 != value2}')
    print(f'{value1} > {value2} = {value1 > value2}')
    print(f'{value1} < {value2} = {value1 < value2}')
    print(f'{value1} >= {value2} = {value1 >= value2}')
    print(f'{value1} <= {value2} = {value1 <= value2}')


compare_op(10, 5)


# Logical Operators
def logic_op(value3, value4):
    """ Logical Operators allow you to combine
    comparison operators
    """
    result1 = value3 > 10 and value4 < 5
    print(result1)
    result2 = value3 < 2 or value4 > 10
    print(result2)
    result3 = not(value3 > value4 and value4 < 5)
    print(result3)


logic_op(12, 3)


# Identity operator
def ident_op():
    """ Identity operators check to see if the
    object is the same in memory
    """
    idle = 'hello'
    jarvis = 'hello'
    result1 = idle is jarvis
    result2 = idle is not jarvis
    print(result1)
    print(result2)


ident_op()


# Membership operator
def member_op():
    """ Membership operators test to see if a
    sequence is in the object
    """
    kilo = 'some'
    lake = 'Some kind of words'
    result_a = kilo in lake
    result_b = kilo not in lake
    print(result_a)
    print(result_b)


member_op()
