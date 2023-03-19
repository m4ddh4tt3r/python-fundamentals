""" Task 1 """


task_1: str = 'This statement has empty spaces'


def get_pos_value():
    print(task_1[6:17])


def get_neg_value():
    print(task_1[-17:-6])


get_pos_value()
get_neg_value()


""" Task 2 """


def task_2():
    task_two: str = 'This statement has empty spaces'
    print(task_two.strip())
    print(task_two.upper())
    print(task_two.find('eme'))
    print(task_two.count('s'))


task_2()


""" Task 3 """


def task_3():
    task_three: str = '\nJack and Jill went up the hill' \
                      '\nto fetch a pail of water.\nJack fell down and broke' \
                      'his crown\nand Jill came tumbling after.'
    print(task_three)


task_3()


def footer():
    completed: str = '\nFin.'
    print(completed)


footer()
