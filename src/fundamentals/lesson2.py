""" Lesson 2 - Intro to Python
Objectives in this section
- Python Overview
- Code Comments & DocString
- Reserved Words
- Function Overview
- Push to GitHub
"""

""" Variables both with or without Annotations. Annotations
are hints to what the data type should be. They are not
forced by the interpreter.
"""
apple = "red"

grape: str = "purple"

# basic comment over a print function
print("comment above")

""" Basic docstring above a print function """
print("docstring above")

print(apple)


def demo_function():
    print('Hello')
    print('Python')


def demo_function2(echo, foxtrot):
    print(echo)
    print(foxtrot)


demo_function2("Happy", "Coding")


def demo_function3(value1, value2):
    return value1 + value2


def demo_function4(data1: int, data2: int) -> int:
    """ Function show annotations and return example. """
    return data1 + data2


demo3 = demo_function3(3, 5)
demo4 = demo_function4(4, 6)
print(demo3)
print(demo4)

