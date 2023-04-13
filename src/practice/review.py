# String concatenation
def concat_example():
    phrase: str = 'Happy'
    phrase2: str = 'Review Day'
    combined: str = phrase + ' ' + phrase2
    print(combined)


# Format method
def format_example(value: int, value2: int):
    msg = 'I like {0} scoops of icecream or {1} pieces of pie.'
    print(msg.format(value, value2))


# String Interpolation (f-string)
def basic_fstring(movie: str, views: int):
    print(f'I have seen {movie} about {views} times.')


# if with elif and else
def control_example(grade: str):
    if grade.upper() == 'A':
        print('Awesome.. good job')
    elif grade.upper() == 'B':
        print('Pretty Good. Almost an A')
    elif grade.upper() == 'C':
        print('Average. Let\'s do better')
    else:
        print('Sorry you failed')


if __name__ == '__main__':
    # concat_example()
    # format_example(3, 2)
    # basic_fstring('Highlander', 500)
    control_example('b')
