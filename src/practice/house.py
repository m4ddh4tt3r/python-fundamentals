""" this (class) is a base example for OOP """


class House:
    def __init__(self, foundation_type: str, roof_style: str,
                 door_color: str, window_size: int):
        self._foundation_type = foundation_type
        self._roof_style = roof_style
        self._door_color = door_color
        self._window_size = window_size

    @property
    def foundation(self) -> str:
        return self._foundation_type

    @foundation.setter
    def foundation(self, foundation_type: str):
        self._foundation_type = foundation_type

    @property
    def roof(self) -> str:
        return self._roof_style

    @roof.setter
    def roof(self, roof_style):
        self._roof_style = roof_style

    @property
    def door_color(self) -> str:
        return self._door_color

    @door_color.setter
    def door_color(self, color):
        self._door_color = color

    @property
    def window_size(self) -> int:
        return self._window_size

    @window_size.setter
    def window_size(self, size):
        self._window_size = size

    def door_function(self):
        print(f'The {self._door_color} door is open.')


class Condo(House):
    def __init__(self, foundation_type: str, roof_style: str, door_color: str,
                 window_size: int, balcony: str):
        super().__init__(foundation_type, roof_style, door_color, window_size)
        self._balcony = balcony

    @property
    def balcony(self) -> str:
        return self._balcony

    @balcony.setter
    def balcony(self, balcony_style):
        self._balcony = balcony_style

    def maintenance(self):
        print(f'We will be up to fix your {self._balcony} balcony')


def main():
    my_house = House('Concrete', 'Composite', 'Red', 34)
    my_house.door_function()
    print(my_house.roof)
    my_condo = Condo('brick', 'steel', 'yellow', 43, 'medium sized')
    my_condo.door_function()
    my_condo.maintenance()


if __name__ == '__main__':
    main()
