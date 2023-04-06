""" Lesson 12 - inheritance and polymorphism """
""" inheritance involves a parent object and
objects that will extend this parent object. they
are referred to as child objects. they gain all of
the attributes and methods of the parent
"""


class Cat:
    def __init__(self, name: str):
        self._name = name

    def move(self):
        print(f'{self._name} the cat can move fast.')


class Cheetah(Cat):
    def __init__(self, name, behavior):
        super().__init__(name)
        self._behavior = behavior

    def sound(self):
        print(f'{self._name} the cheetah {self._behavior}')


class Parent1:
    def __init__(self, first_name):
        self._first_name = first_name

    def my_first(self):
        print(f'My first name is {self._first_name}')


class Parent2:
    def __init__(self, last_name):
        self._last_name = last_name

    def my_last(self):
        print(f'My last name is {self._last_name}')


class Child(Parent1, Parent2):
    def __init__(self, first_name, last_name):
        Parent1.__init__(self, first_name)
        Parent2.__init__(self, last_name)

    def my_name(self):
        print(f'My name is {self._first_name} {self._last_name}')


class Child2(Child):
    def __init__(self, first_name, last_name, middle_name):
        super().__init__(first_name, last_name)
        self._middle_name = middle_name

    def my_real_name(self):
        print(f'My real name is {self._first_name} {self._middle_name} {self._last_name}')


def parent_example():
    # child object
    me = Child('Paul', 'Smith')
    # call child method
    me.my_name()
    # child calls parent1
    me.my_first()
    # child calls parent2
    me.my_last()
    # child2 object
    my_son = Child2('Leviticus', 'Brown', 'Nathaniel')
    # child2 calls method
    my_son.my_real_name()
    # child2 calls parent
    my_son.my_name()
    # child2 calls grandparent
    my_son.my_first()


def main():
    # instance of a child
    wild_cat = Cheetah('Chester', 'runs fast!')
    # call the child method
    wild_cat.sound()
    # call parent method
    wild_cat.move()


if __name__ == '__main__':
    # main()
    parent_example()
