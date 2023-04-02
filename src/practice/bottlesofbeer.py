def beer_song():
    beer_number: int = 99
    word: str = 'bottles'

    while beer_number > 0:
        print(f'{beer_number} {word} of beer on the wall.')
        print(f'{beer_number} {word} of beer,')
        print('Take one down')
        print('Pass it around')

        beer_number -= 1

        if beer_number == 1:
            word = 'bottle'

        if beer_number > 0:
            print(f'{beer_number} {word} of beer on the wall.')
            print()
        else:
            print('No more bottles of beer on the wall.')


beer_song()
