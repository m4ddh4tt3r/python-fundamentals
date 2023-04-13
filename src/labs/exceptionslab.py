def check_leap_year():
    year_str = input("Please enter a year (format: YYYY): ")

    try:
        year = int(year_str)
        if len(year_str) != 4:
            raise ValueError
    except ValueError:
        print("You did not provide a valid year. Please enter a year in the format: YYYY")
        return

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")


if __name__ == '__main__':
    check_leap_year()
