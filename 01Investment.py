def take_inputs():
    """
    Ask user inputs and ensure they are correct
    :return: 3 values
    """

    msg = [
        '\nPlease enter initial investment value: £',
        '\nPlease enter target value: £',
        '\nPlease enter annual interest rate (0-100 [%]): ',
    ]
    # ask for investment and target value
    initial_investment = check_inputs(msg[0])
    target_investment_value = check_inputs(msg[1])

    # ask user for interest rate
    annual_int_rate = check_inputs(msg[2])
    while 0 <= annual_int_rate > 100:
        print('\nNot in range. Please try again. \nUse a value between 0 and 100.')
        annual_int_rate = check_inputs(msg[2])

    # convert annual interest rate to decimal
    if annual_int_rate == 0:
        annual_int_rate = annual_int_rate
    else:
        annual_int_rate = annual_int_rate / 100

    return initial_investment, target_investment_value, annual_int_rate


def check_inputs(msg):
    # while input isn't correct loop
    while True:
        # ask for initial input
        inp = input(msg)
        # try to convert input to integer
        try:
            inp = float(inp)
            # check if negative, if so, try again
            if inp < 0:
                print('Value cannot be negative. Please try again.')
                continue
            # once confirmed it is int and >100 return input
            else:
                return inp
        # if input is not a number try again
        except ValueError:
            print('This is not a number. Please try again.')
            continue


def calc_years(initial_investment, target_investment_value, annual_int_rate):
    # starting with 0 years and investment value equal to investment
    years = 0
    investment_value = initial_investment

    # loop year by year until value is more than needed
    while target_investment_value > investment_value:
        # add annual interest
        investment_value = investment_value * (1 + annual_int_rate)
        # add a year
        years += 1

    return years


def main():
    # ask user input & calculate years
    a, b, c = take_inputs()
    years = calc_years(a, b, c)
    return 'It will take ' + str(years) + ' years ' + 'to grow your investment of £' + str(a) + ' to £' + str(b)


print(main())
