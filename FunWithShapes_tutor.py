import math
import os
# OS is imported but not used. Ok, it is used in another
# module in a new .py file. I will write it here bcs this
# is a check & learn version, so I only want to see if
# there are new methods I can learn
from os import system


def circle_calcs(dia):
    # This is a good way to check if number is valid,
    # much shorter than my function, however, it does
    # not allow user to try again.
    if not dia.isnumeric() or float(dia) <= 0:
        display_error_msg("circle")
        return -1, -1
    dia = float(dia)
    radius = dia / 2
    perimeter = math.pi * radius * 2
    area = math.pi * radius ** 2
    return perimeter, area


def display_error_msg(shape):
    print(f"illegal dimension(s). You can't make a {shape} with non numeric, negative or zero value.")


def triangle_calcs(a="3.0", b="4.0", c="5.0"):
    # The input statements are missing. The above does not work with
    # the statements below.
    # Can lengths be used to make a triangle?
    if not a.isnumeric() or not b.isnumeric() or not c.isnumeric():
        display_error_msg("triangle")
        return -1, -1
    # I changed these to a single line to save space
    a, b, c = float(a), float(b), float(c)
    if a <= 0 or b <= 0 or c <= 0:
        display_error_msg("triangle")
    elif a + b < c or a + c < b or b + c < a:
        return -1, 1
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return perimeter, area


def display_menu():
    # system allows to interact with the underlying system
    # why is it there?
    system('cls')
    print("SHAPE STATS CALCULATOR")
    print("Please enter one of the following: ")
    print("'c' for circle stats")
    print("'t' for triangle stats")
    print("'q' to quit")
    return input()


def display_results(shp, perim, ar):
    # now the description is lousy, but decimals are defined
    print(f"{shp} has a perimeter of {round(perim, 2)} and area of {round(ar, 2)}.")


def ui_module():
    choice = 'x'
    while choice != 'q':
        while choice not in ['c', 't', 'q']:
            choice = display_menu()
        if choice == 'c':
            dia = input("Please enter the dia of the circle: ")
            perimeter, area = circle_calcs(dia)
            shape = 'circle'
        if choice == 't':
            a = input("Please enter the length of side 1 of the triangle: ")
            b = input("Please enter the length of side 2 of the triangle: ")
            c = input("Please enter the length of side 3 of the triangle: ")
            perimeter, area = triangle_calcs(a, b, c)
            shape = 'triangle'
        # Pause to see the result of calculations
        if perimeter != -1 and area != -1:
            display_results(shape, perimeter, area)
        # this resets the menu ( a good way to reset things to None)
        perimeter = area = shape = ""
        input()
        choice = display_menu()
    print("Thank you for using the shape stats calculator.")


print(ui_module())

"""
Conclusions

[Preference] I think this solution should check each input separately if there is more
than one for each calc, because then user can finish the calculation without
going back to the main menu,

This solution has traceback errors when exiting (while not 1 is not a good choice I think:
1. q is specified within while loop that goes through many things before 
concluding that 'q' has been entered. Values within the while loop are 
referenced before assignment because there is no assignment for 'q'.

2. When one calc is done and then exit, due to nonetype the display results
function crashes. Maybe string would work better?

Triangle side check elif statement is wrong. It sometimes outputs 0. Did not check why.

system module is not working. sh: cls: command not found error everytime ui is launched.
"""