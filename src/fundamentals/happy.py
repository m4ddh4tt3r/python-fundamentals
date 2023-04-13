""" This file will be used as an import for lesson 14 """


def express(is_happy: bool = True) -> str:
    if is_happy:
        result = 'I am happy'
    else:
        result = 'I am not happy'
    return result
