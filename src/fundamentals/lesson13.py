""" Lesson 13 - Exception handling """
""" The below function is a problem to solve. """


def problem_demo():
    try:
        name = input('What is your name?')
        height = int(input('What is your height in inches?'))
        feet = int(height / 12)
        inches = height % 12
        print(f'{name} is {feet} feet {inches} inches tall.')
    except ValueError:
        print('You have entered an invalid entry for  height. Numbers only.')
        problem_demo()


def example_error(value1, value2):
    try:
        combined = int(value1) + int(value2)
        print(combined)
    except (TypeError, ValueError):
        print('Cannot combine strings and numbers using the (+) operator.')


def example_divide(num1: int, num2: int):
    try:
        total = num1 / num2
        print(total)
    except ZeroDivisionError:
        print('You cannot divide by 0.')
    except TypeError:
        print('You have entered a string value in a math problem.')


def problem_demo_else():
    name = input('What is your name?')
    try:
        height = int(input('What is your height in inches?'))
        feet = int(height / 12)
        inches = height % 12
    except ValueError:
        print('You have entered an invalid entry for height. Numbers only.')
    else:
        print(f'{name} is {feet} feet {inches} inches tall.')


def finally_example(value1, value2):
    try:
        combined = value1 + value2
        print(combined)
    except TypeError:
        print('Cannot combine strings and numbers using the (+) operator.')
    finally:
        print('This (finally) always processes.')


def raise_example():
    try:
        raise NameError('Hello There')
    except NameError:
        print('A name exception')


if __name__ == '__main__':
    # problem_demo()
    # example_error('5', 5)
    # example_divide(5, 23)
    # problem_demo_else()
    # finally_example("5", 6)
    raise_example()
