"""
Write 2 functions to complete the below practice.
Both functions will accept 1 argument.
If you want to include annotations, this argument will be a float.
"""

"""
Function 1: Taking in the argument, write out the formula to
convert Celsius to Fahrenheit. assign the result to a variable,
 then provide a print function to display the result.
"""


# (Celsius * 9 / 5) + 32 = Fahrenheit
def cel_to_fah(celsius):
    fah_total = (celsius * 9 / 5) + 32
    print(fah_total)


cel_to_fah(12)


"""
Function 2: taking in the argument, write out the formula to
convert Fahrenheit to Celsius. Assign the result to a variable
then provide a print function to display the result.
"""


# (Fahrenheit - 32) * 5 / 9 = Celsius
def fah_to_cel(fahrenheit):
    cel_total = (fahrenheit - 32) * 5 / 9
    print(cel_total)


fah_to_cel(53.6)