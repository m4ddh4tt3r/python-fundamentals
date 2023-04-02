""" Task 1 """


def compare_args(arg1, arg2):
    if arg1 == arg2:
        print(f"{arg1} and {arg2} are equal.")
    else:
        print(f"{arg1} and {arg2} are not equal.")


# compare_args(3, 7)


# compare_args(7, 7)


# compare_args("Zelda", "Link")


compare_args("Link", "Link")


""" Task 2 """


def evaluate_grade(grade):
    if grade == "E":
        print("Excellent")
    elif grade == "V":
        print("Very Good")
    elif grade == "G":
        print("Good job")
    elif grade == "A":
        print("Average")
    elif grade == "F":
        print("Failed")
    else:
        print("Not a valid grade")


# evaluate_grade("A")


evaluate_grade("J")
