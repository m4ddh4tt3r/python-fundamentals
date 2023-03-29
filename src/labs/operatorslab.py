""" Operators Lab """


""" First 2 calls commented out for simplicity """


""" Task 1 """


def math_problem():
    x = 10 + 32 * 12 / 3
    y = (10 + 32) * 12 / 3
    print(f"{x}, {y}")


# math_problem()


""" Task 2 """


def op_math(x, y):
    x += y
    print(f"x += y: x = {x}")
    x *= y
    print(f"x *= y: x = {x}")
    x %= y
    print(f"x %= y: x = {x}")


# op_math(3, 7)


""" Task 3 """


def comp_math(x, y):
    print(f"{x} == {y} = {x == y}")
    print(f"{x} >= {y} = {x >= y}")
    print(f"{x} != {y} = {x != y}")


comp_math(2, 6)
