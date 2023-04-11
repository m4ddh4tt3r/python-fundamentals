class Horse:
    def __init__(self, name: str, age: int, breed: str):
        self._name = name
        self._age = age
        self._breed = breed

    def behavior(self):
        print(f"{self._name} is galloping in the field of Hyrule.")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    @property
    def breed(self) -> str:
        return self._breed

    @breed.setter
    def breed(self, breed: str):
        self._breed = breed


class Mustang(Horse):
    def __init__(self, name: str, age: int, breed: str, size: str):
        super().__init__(name, age, breed)
        self._size = size

    def behavior2(self):
        print(f"{self._name} is spooked by a Poe.")

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, size: str):
        self._size = size


def main():
    my_horse = Horse('Epona', 8, 'Silver Bay')
    my_horse.behavior()
    print(f'{my_horse.name} is a {my_horse.breed}.')
    my_horse2 = Mustang('Dax', 7, 'Mustang', '13 Hands')
    my_horse2.behavior2()
    print(f'{my_horse2.name} is {my_horse2.size} tall.')


if __name__ == '__main__':
    main()
