# Prompt the user for the price of
# an item being sold by an online store
def ask_price():
    while True:
        price = input('Please enter the item price: £')
        try:
            price = round(float(price),2)
            if price <0:
                print('Price cannot be negative.\
                \nPlease try again.\n')
                continue
            else:
                return price
        except ValueError:
            print('\nThis is not a number.\
            \nPlease try again.\n')

# Calculate the price the user
# must pay based on the following:

# They have a 10% discount
# VAT is 20%
# Delivery costs £4.50
def calc_final_price(price):
    discounted_price = price * 0.9
    VAT = discounted_price * 0.2
    fin_price = discounted_price + VAT + 4.5
    return '\nThe total price of your item is: £' + str(fin_price) + '\n'

def main():
    '''
    A program that takes a price from user
    and calculates total price
    :return: price with applied discount, tax and delivery
    '''
    price = ask_price()
    print(calc_final_price(price))

    # Giving user a choice to play more until
    # they want to stop
    stop = ask_to_play()
    while stop is False:
        price = ask_price()
        print(calc_final_price(price))
        stop = ask_to_play()
    return 'Exit successful.'

def ask_to_play():
    while True:
        play = input('Would you like to try again?'
                     '\n(y) yes\
                      \n(n) no\
                      \n')

        if play in ['yes','y','Y','Yes']:
            return False
        elif play in ['no','n','N','No']:
            return True
        else:
            print('\nThis is not one of the answers.\
            \nPlease try again.\n')

print(main())
