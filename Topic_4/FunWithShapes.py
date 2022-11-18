# Assignment: calc perimeter and area of certain shapes
# this is my own feedback when looking at
# the proposed solution
import math
# could have used from os import system


def is_number_inp_valid(msg):
    # ERROR MESSAGES COULD BE GENERIC
    # TUTOR USED if not inp,isnumeric() or float(inp) <= 0:
    # display_error_message("shape")
    """
    Helper function that checks input
    and outputs appropriate error message
    or output
    :param msg: string, Message when asking user input
    :return: integer
    """
    while True:
        inp = input(msg)
        # adding functionality to leave
        if inp == 'e':
            return 'e'
        try:
            # accept floats and integer inputs
            inp = float(inp)
            if inp <= 0:
                # this is not a good approach. Would be better to raise an error.
                print('\nValue cannot be negative or 0. Please try again.')
                continue

            else:
                # return integer for formatting reasons
                return inp
        except ValueError:
            print('\nNot a number. Please try again.')
            continue


class Calcs():

    def circle_calcs(dia=None):
        """
        Asks for dia and calculates perimeter
        and area of a circle
        :return: int, int, perimeter and area
        """
        # for testing purposes, take given input too
        if dia is None:
            # ask for user value
            dia = is_number_inp_valid('\nPlease enter the ⌀ of the circle: ')

        # does user want to leave?
        if dia == 'e':
            return None, None

        else:
            # makes sure testing purpose digit is float
            dia = float(dia)
            # get constants
            radius = dia / 2
            pi = math.pi

            # calculate the perimeter and radius
            circle_perimeter = 2 * radius * pi
            circle_area = pi * radius * radius

            # return the perimeter and area
            return circle_perimeter, circle_area

    def triangle_calcs():
        """
        Asks for 3 triangle sides and calculates
        the perimeter and area of triangle
        :param a: int, first side
        :param b: int, second side
        :param c: int, third side
        :return: int, int, perimeter and area
        """
        # ask for user values
        a = is_number_inp_valid('\nPlease enter the length of first side: ')
        # does user want to leave?
        if a == 'e':
            return None, None
        b = is_number_inp_valid('\nPlease enter the length of second side: ')
        # does user want to leave?
        if b == 'e':
            return None, None

        else:
            # ask for user values & sanity check the third side
            while True:
                # ask user input for side 3
                c = is_number_inp_valid('\nPlease enter the length of third side: ')
                # does user want to leave?
                if c == 'e':
                    return None, None

                # if input is checked as OK
                check, max_value, min_value = Calcs.third_side_check(a, b, c)
                if check:
                    # stop the loop
                    break
                # otherwise,
                else:
                    # continue, and ask for new input
                    print('\nError. Side not in range of {} to {}. Please try again.'.format(min_value, max_value))
                    continue

            # calculating the triangle perimeter
            triangle_perimeter = a + b + c
            # s constant
            s = triangle_perimeter / 2
            # calculating the triangle area
            triangle_area = math.sqrt(s * (s - a) * (s - b) * (s - c))

            # return the perimeter and area
            return triangle_perimeter, triangle_area

    def third_side_check(a, b, c):
        """
        Takes two sides of a triangle and
        sense checks if third is in the range.
        :param a: side 1
        :param b: side 2
        :param c: side 3
        :return: True (in range) / False (not in range)
        """
        # Min third side length
        min_length = max(a, b) - min(a, b) + 1
        # Max third side length
        max_length = max(a, b) + min(a, b) - 1

        # if c is not in range
        if min_length <= c <= max_length:
            print('Yes it is within range.')
            return True, max_length, min_length
        else:
            return False, max_length, min_length

    def square_calcs():
        """
        Asks for one triangle side
        and calculates perimeter and area
        :return: int, int, perimeter and area
        """
        # ask for user values
        a = is_number_inp_valid('\nPlease enter the length of square side: ')

        # calculate perimeter
        square_perimeter = 4 * a
        # calculate area
        square_area = a * a

        # return the perimeter and area
        return square_perimeter, square_area

    def rectangle_calcs():
        """
        Asks for two sides of rectangle
        and calculates rectangle perimeter
        and area
        :return: int, int, perimeter and area
        """
        # ask for user values
        a = is_number_inp_valid('\nPlease enter the length of one rectangle side: ')
        b = is_number_inp_valid('\nPlease enter the length of other rectangle side: ')

        # calculate perimeter
        rectangle_perimeter = 2 * (a + b)
        # calculate area
        rectangle_area = a * b

        # return the perimeter and area
        return rectangle_perimeter, rectangle_area


'''
Due to the input being called & tested
in the is_number_inp_valid function,
any tests that relate to validity of input, like 
one's in the assignment: (zero, negative values and textual values, etc.),
should be tested through validity function. 

This means that Calcs are only subject to mathematical correctness
checks.
'''