# Assignment: calc perimeter and area of certain shapes
import math


def is_number_inp_valid(msg):
    """
    Helper function that checks input
    and outputs appropriate error message
    or output
    :param msg: string, Message when asking user input
    :return: integer
    """
    while True:
        inp = input(msg)
        try:
            # accept floats and integer inputs
            inp = float(inp)
            if inp < 0:
                print('\nValue cannot be negative. Please try again.')
                continue
            else:
                # return integer for formatting reasons
                return inp
        except ValueError:
            print('\nNot a number. Please try again.')
            continue


def is_this_command_allowed(cmd, ok_commands):
    """
    Checks if user has picked one
    of the allowed commands
    :param cmd: command user chose
    :param ok_commands: commands allowed
    :return: True / False
    """
    if cmd in ok_commands:
        return True
    else:
        return False


def circle_calcs():
    """
    Asks for dia and calculates perimeter
    and area of a circle
    :return: int, int, perimeter and area
    """
    # ask for user value
    dia = is_number_inp_valid('\nPlease enter the ⌀ of the circle: ')

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
    b = is_number_inp_valid('\nPlease enter the length of second side: ')

    # ask for user values & sanity check the third side
    while True:
        # ask user input for side 3
        c = is_number_inp_valid('\nPlease enter the length of third side: ')
        # if input is checked as OK
        check, max_value, min_value = third_side_check(a, b, c)
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


def print_results(shape, perimeter, area):
    """
    Makes the statement to print to user
    :param shape: string - triangle, circle, rectangle or square
    :param perimeter: int, value of perimeter
    :param area: int, value of area
    :return:
    """
    print('\n{0} perimeter is {1:5.2f} units and area {2:5.2f} square units.\n'.format(shape, perimeter, area))


def main():
    """
    Asks user which shape to calculate.
    Then asks for input and calculates.
    :return: string of results
    """
    # messages to be displayed in the main menu function
    msg =[
        '\nPlease pick the function you would like to use.\
         \n"c" - Circle\
          \n"t" - Triangle \
          \n"s" - Square \
          \n"r" - Rectangle\
           \n\n"e" - Exit the program\
          \nYour choice: ',
        '\nSorry! This is not one of the commands. \
        \nPlease try again.\n'
    ]

    while True:
        # Asking user to pick a function
        cmd = input(msg[0])
        # checking if function exists and if not start again
        if not is_this_command_allowed(cmd, 'ctsreCTSRE'):
            print('\nThis command does not exist. Please try again.')
            continue

        # if command is exit, break the loop
        if cmd == 'e':
            break

        # if circle is chosen
        if cmd == 'c':
            # launch the circle calc
            circle_perimeter, circle_area = circle_calcs()
            print_results('Circle', circle_perimeter, circle_area)

        # if triangle is chosen
        if cmd == 't':
            # launch the triangle calc
            triangle_perimeter, triangle_area = triangle_calcs()
            print_results('Triangle', triangle_perimeter, triangle_area)

        # if square is chosen
        if cmd == 's':
            # launch the square calc
            square_perimeter, square_area = square_calcs()
            print_results('Square', square_perimeter, square_area)

        # if rectangle is chosen
        if cmd == 'r':
            # launch the rectangle calc
            rectangle_perimeter, rectangle_area = rectangle_calcs()
            print_results('Rectangle', rectangle_perimeter, rectangle_area)

    return '\nExit chosen. This is the end.'


print(main())
