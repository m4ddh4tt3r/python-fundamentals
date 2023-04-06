""" Task 1 """

pizzas = ['Supreme', 'Cheese', 'Pepperoni', 'Mushroom', 'Meat Lovers', 'Hawaiian']


def fav_pizza_list():
    for pizza in pizzas:
        print(pizza)


fav_pizza_list()


def more_pizza():
    pizzas.append('Margherita')
    pizzas.append('Greek')
    for pizza in pizzas:
        print(pizza)


print()
more_pizza()


""" Task 2 """

favorite_movies = {2022: 'Everything Everywhere All At Once', 2006: 'A Scanner Darkly', 2000: 'Requiem For A Dream',
                   1998: 'Fear And Loathing In Las Vegas', 1992: 'Aladdin'}


def movie_list():
    for key, value in favorite_movies.items():
        print(f'{key}: {value}')


print()
movie_list()
