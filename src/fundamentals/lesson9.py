""" Lesson 9 collections pt. 2 """
""" a set collection is un-ordered and because of this,
it is also un-indexed. this means we cannot use the index
syntax to print a specific value.
"""
ice_cream = {'Chocolate', 'Vanilla', 'Rocky Road', 'Chocolate Chip',
             'Tin Roof', 'Neapolitan', 'Cookies and Cream'}


def show_set():
    print(ice_cream)
    for flavor in ice_cream:
        print(flavor)


# show_set()


def add_set_value():
    """ (add) method will add a single item to the set.
    """
    ice_cream.add('Strawberry')
    for flavor in ice_cream:
        print(flavor)


# add_set_value()


def update_set_values():
    """ (update) method adds multiple items to the set. """
    ice_cream.update({'Penut butter pecan cup', 'Butter pecan', 'Bunny tracks'})
    for flavor in ice_cream:
        print(flavor)


# update_set_values()


def update_set_reference():
    more_flavors = {'Penut butter cup', 'Butter pecan', 'Bunny tracks'}
    ice_cream.update(more_flavors)
    for flavor in ice_cream:
        print(flavor)


# update_set_reference()


def remove_set_value():
    """  the (remove) method will attempt to remove the item
    based on the argument it supplies. if it is not in the collection
    you will generate an error.
    """
    ice_cream.remove('Tin Roof')
    for dessert in ice_cream:
        print(dessert)


# remove_set_value()


def discard_set_value():
    """ the (discard) method will attempt to remove the item
    based on the argument supplied. if it is not in the collection
    no error will be generated. the results will be unchanged.
    """
    ice_cream.discard('Vanilla')
    for dessert in ice_cream:
        print(dessert)


# discard_set_value()


def pop_set_value():
    """ the (pop) method will remove  the last item from that collection.
    because the collection is un-ordered, this affects what is removed. """
    value = ice_cream.pop()
    print(f'{value} was removed')
    for dessert in ice_cream:
        print(dessert)


# pop_set_value()


def clear_set_value():
    """ the (clear) method will empty the collection. the collection
    itself still exists accept  new items. returns set constructor
    """
    ice_cream.clear()
    # ice_cream.add('Apple)
    print(ice_cream)


# clear_set_value()


def del_set_values():
    """ the (del) statement will remove all the items from the set along with
    any reference to the collection assigned to the variable.
    """
    del ice_cream
    print(ice_cream)


# del_set_values()


""" Dictonary collection """
marvel_movies = {1: 'Captain America - The First Avenger', 2: 'Captain Marvel',
                 'Three': 'Iron Man', 4: 'Iron Man 2', 5: 'The Incredible Hulk',
                 6: 'Thor', 7: 'The Avengers', 8: 'Thor - Dark World'}


def get_value_bracket():
    """ [] require the key in the dictioary to return the value. """
    value = marvel_movies['Three']
    print(value)


# get_value_bracket()


def get_value_get():
    """ the (get) method requires the key to return the value. """
    value = marvel_movies.get(5)
    print(value)


# get_value_get()


def change_value():
    """ using [] with the key, we can update the value. make
    sure you use the correct key, or you will add a new item instead
    of updating the item.
    """
    marvel_movies[1] = 'Captain America'
    print(marvel_movies)


# change_value()


def add_value():
    """ using [] with the key, we can add a new item. for the item
    to be new, we need to use a key that hasn't been used, or it
    will update the item it matches.
    """
    marvel_movies[9] = 'Iron Man'
    print(marvel_movies)


# add_value()


def add_loop():
    """ standard for loop with (print) will only print keys. """
    for key in marvel_movies:
        print(key)


# loop_key()


def loop_values():
    """ getting the values using bracket notation. [] from the key. """
    for movie in marvel_movies:
        print(marvel_movies[movie])


# loop_values()


def values_method():
    """ the (values) method can return the values from a dictionary
    using a (for) loop.
    """
    for movie in marvel_movies.values():
        print(movie)


# values_method()


def whole_item():
    """ to get both the key and value, we need to use a
    (for) loop that can take 2 variables instead of 1. we
    will use a method called (items) with this (for) loop to
    get the whole (item) """
    for key, value in marvel_movies.items():
        print(f'{key}: {value}')


# whole_item()


nested_marvel = {'Captain America': {1: 'The First Avenger',
                 2: 'The Winter Soldier', 3: 'Civil War'},
                 'Iron Man': {1: 'Iron Man', 2: 'Iron Man 2', 3: 'Iron Man 3'}}


def nested_dictionary():
    """ to loop through a nested dictionary, we need
    to use more than one (for) loop. the first (for) loop
    uses the 2 variable syntax, while the inner (for)
    loop uses a single variable (for) loop.
    """
    for outer_key, value in nested_marvel.items():
        print(f'\nMovie type: {outer_key}')
        for inner_key in value:
            print(f'{inner_key}: {value[inner_key]}')


# nested_dictionary()


""" other methods of dictionary """
colors = {101: 'red', 102: 'blue', 103: 'green', 104: 'yellow', 105: 'orange'}


def example_pop():
    print(f'Length of Dictionary {len(colors)}')
    colors.pop(104)
    print(f'Length after pop {len(colors)}')


# example_pop()


def example_pop_item():
    print(f'Length of dictionary {len(colors)}')
    colors.popitem()
    print(f'Length after popitem {len(colors)}')


example_pop_item()
