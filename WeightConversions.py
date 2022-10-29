
def convert_input_to_stones_and_pounds():
    '''
    Ask the total weight of user & convert it
    :return: string example: '1 stone 4 pounds'
    '''

    # Ask user for input and check if it's correct
    # Input helper function created to assist with this
    pounds = inputHelper('Please enter the total weight in pounds: ')

    # Getting the stones (larger measurement):
    stones = pounds // 14
    # Getting the resulting pounds
    rpounds = pounds % 14
    print(stones, 'stone(s) and',rpounds,'pound(s)')

def convert_kgs_to_stones_pounds():
    '''
    Ask the weight in kgs & convert it
    :return: string example: '1 stone 4 pounds'
    '''

    # Ask user for input and check if it's correct
    kgs = inputHelper('Please enter the weight in kilograms: ')

    # Convert the weight to the smallest used unit -> pounds
    pounds = kgs * 2.20462

    # At this point I would prefer to call up convert_input_to_stones_and_pounds

    # function but those are not the rules of the task
    # Getting the stones (larger measurement):
    stones = int(pounds // 14)
    # Getting the resulting pounds
    rpounds = int(pounds % 14)
    print(stones, 'stone(s) and',rpounds,'pound(s)')

def convert_stones_and_pounds_to_kgs():
    '''
    Ask the weight in stones & pounds & converts it
    :return: string example: '20 kgs'
    '''

    stones = inputHelper('Please enter the weight in stones: ')
    pounds = inputHelper('Please enter the weight in pounds: ')

    # Convert stones & pounds to kgs
    kgs = stones * 6.35029 + pounds * 0.453592
    print(round(kgs,2),'kgs')

def inputHelper(msg):
    inp = input(msg)
    while str.isdigit(inp) is False :
        print('Invalid input. Please try again.')
        inp = input(msg)
        continue
    return int(inp)

def main():
    '''
    Ask the user which calc to use and then call it
    :return: function
    '''

    while True:
        Q = input(' \
        \nWhich function would you like to use today? Please enter \
        \n"p" for lbs to st lbs conversion, \
        \n"sp" for st lb to kgs conversion, \
        \n"kg" for kgs to st lbs, \
        \n "e" to exit the program.\
        \n')

        # Check if user wishes to exit the program
        if Q == "e":
            print('User has chosen to exit the program.')
            break
        # Sanity check - is the input valid?
        if Q not in "spkg":
            print('Input invalid. Try again.')
            continue

        # Use the answer to determine which function to call
        if Q == "p":
            convert_input_to_stones_and_pounds()

        if Q == "kg":
            convert_kgs_to_stones_pounds()

        if Q == "sp":
            convert_stones_and_pounds_to_kgs()

print(main())