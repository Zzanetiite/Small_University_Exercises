import math

# images to make it easier for user to understand
# which side is being discussed
triangle_pictures = [
    '\n     /|    \
   \n    / | a   \
   \n   /__|',
    '\n     /|    \
   \n    / |     \
   \n   /__|      \
   \n    b',
    '\n     /|    \
   \n  c / |     \
   \n   /__|       '
]

# messages to use for prompts
msg = [
    'Please enter the length of the shortest side \nof a right-angled triangle: ',
    'Please enter the length of the second shortest side \nof a right-angled triangle: ',
    'The length of the longest side is: '
]


def is_input_valid(msg, i):
    '''
    Function that validates the user input
    :param msg: String. Prompt for the user.
    :param i: index of pictures. index = side (0=a,1=b,2=c)
    :return: returns the length of the side
    '''
    msg = triangle_pictures[i] + '\n' + msg
    while True:
        side = input(msg)
        try:
            side = float(side)
            if side < 0:
                print('\nNegative values are invalid. Please try again.\n')
                continue
            elif side == 0:
                print('\nInvalid value of 0 entered. Please try again.\n')
            else:
                return side
        except ValueError:
            print('\nNot a number. Please try again.\n')


def calc_c(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return round(c, 2)


def main():
    '''
    Function to calculate the hypotenuse
    from the two short edges
    :return: number, hypotenuse
    '''
    # asking for each edge length
    a = is_input_valid(msg[0], 0)
    b = is_input_valid(msg[1], 1)
    # calculate the c (hypotenuse)
    c = calc_c(a, b)
    return triangle_pictures[2] + '\n' + msg[2] + str(c)


print(main())