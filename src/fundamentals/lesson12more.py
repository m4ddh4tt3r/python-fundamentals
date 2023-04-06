""" this file is more content from lesson 12 """


class Car:
    def __init__(self, model, color):
        self._model = model
        self._color = color

    def info(self):
        print(f'I like my {self._color} {self._model}')

    def move(self):
        print(f'My {self._model} drives fast on the road.')


class Boat:
    def __init__(self, model, color):
        self._model = model
        self._color = color

    def info(self):
        print(f'I like my {self._color} {self._model}')

    def move(self):
        print(f'My {self._model} drives fast on the water.')


def poly_example():
    car1 = Car('Camaro', 'Blue')
    boat1 = Boat('Ranger', 'Black')

    for vehicle in (car1, boat1):
        vehicle.move()
        vehicle.info()


class Animal:
    def __init__(self, family):
        self._family = family

    def info(self):
        pass

    def make_sound(self):
        return f'RIBBIT! goes the {self._family}'

    def __str__(self):
        return self._family


class Frog(Animal):
    def __init__(self, name):
        self._name = name
        super().__init__('Amphibian.')

    def info(self):
        return f'My frog\'s name is {self._name}; he is an {self._family}'

    def __str__(self):
        return self._name


class Dog(Animal):
    def __init__(self, name):
        self._name = name
        super().__init__('Canine.')

    def info(self):
        return f'My dog\'s name is {self._name}; she is a {self._family}'

    def make_sound(self):
        return f'{self._name} Barks!'

    def __str__(self):
        return self._name


def my_animal():
    dog1 = Dog('Penny')
    frog1 = Frog('Kermit')
    print(dog1.info())
    print(frog1.info())
    print(dog1.make_sound())
    print(frog1.make_sound())


def main():
    # poly_example()
    my_animal()


if __name__ == '__main__':
    main()
