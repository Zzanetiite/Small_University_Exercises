# function to do the print statements
def text_nums(n, num):
    print(str(n) + ' x ' + str(num) + ' = ' + str(n * num))


# create multiplier table for 5
for num in range(12 + 1):
    text_nums(4, num)

print('')

# create multiplier table for 4
for num in range(12 + 1):
    text_nums(5, num)


def check_inputs():
    '''
    Helper function to check inputs from user
    :param msg: message to display to usee
    :return:
    '''
    # while input isn't correct loop
    while True:
        # ask for initial input
        inp = input('\nPlease enter a number between 1 to 12 :')
        # try to convert input to integer
        try:
            inp = int(inp)
            # check if negative, if so, try again
            if inp < 0:
                print('\nValue cannot be negative. Please try again.')
                continue
            # check if input is in range
            if 1 <= inp <= 12:
                return inp
            # if not in range try again
            else:
                print('\nValue not in range. Please try again.')
                continue
        # if input is not a number try again
        except ValueError:
            print('\nThis is not a number. Please try again.')
            continue

'''
# create a multiplier table for
# an integer 1 to 12 that takes user input
n = check_inputs()
for num in range(n + 1):
    text_nums(n, num)
'''

# create a multiplier table for int 1 to 12
# that outputs each number table
for numsy in range(1, 12 + 1):
    print('')
    for num in range(numsy + 1):
        text_nums(numsy, num)
