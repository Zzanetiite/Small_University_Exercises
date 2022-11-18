from FunWithShapes import Calcs


def is_this_command_allowed(cmd, ok_commands):
    # This could be done with a lambda function
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


def print_results(shape, perimeter, area):
    # could be a lambda function within main?
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
           \n\n"e" - Exit the program or function (available throughout)\
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
        # below commands shortened
        # if circle is chosen
        if cmd == 'c':
            # launch the circle calc
            perimeter, area = Calcs.circle_calcs()
            if perimeter is None or area is None:
                print('User exited the function.')
            else:
                print_results('Circle', perimeter, area)

        # if triangle is chosen
        if cmd == 't':
            # launch the triangle calc
            perimeter, area = Calcs.triangle_calcs()
            if perimeter is None or area is None:
                print('User exited the function.')
            else:
                print_results('Triangle', perimeter, area)

        # if square is chosen
        if cmd == 's':
            # launch the square calc
            perimeter, area = Calcs.square_calcs()
            print_results('Square', perimeter, area)

        # if rectangle is chosen
        if cmd == 'r':
            # launch the rectangle calc
            perimeter, area = Calcs.rectangle_calcs()
            print_results('Rectangle', perimeter, area)

    return '\nExit chosen. This is the end.'


print(main())

'''
Reflection:
i did not implement the exit option just yet.
This program would benefit if the functions were in a 
separate file, perhaps, class. (Updated)

Code optimization could make this code shorter.

Input should be outside of the functions to allow
for easier testing.

Use of classes would also make testing easier. Not yet learned 
how to use classes fully.

Raise errors instead of print statements. They are testable. 
'''