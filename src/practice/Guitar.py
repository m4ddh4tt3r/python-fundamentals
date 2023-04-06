""" practices with classes and inheritance """


class Guitar:
    def __init__(self, strings_num, body_style):
        self._strings_num = strings_num
        self._body_style = body_style

    def play(self):
        print(f'{self._strings_num} string {self._body_style} guitar is fun to play.')


class Mandolin(Guitar):
    def __init__(self):
        super().__init__(8, 'bowl shaped')


def main():
    my_guitar = Guitar(6, 'Round Back')
    my_guitar.play()

    my_mando = Mandolin()
    my_mando.play()


if __name__ == '__main__':
    main()
