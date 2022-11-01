def is_input_valid(question):
    while True:
        p = input(question)
        try:
            p = float(p)
            if p < 0:
                print('The amount of money cannot be negative. \
                \nPlease enter a positive number. ')
                continue
            else:
                return p
        except ValueError:
            print('Not a number. Please try again.')


# Calculate how many bags they can afford
def calc_how_many(sweet_price, money_in_wallet):
    if money_in_wallet == 0 and sweet_price == 0:
        return '\nSweets are free! Have as much as you like!'
    # Calculate how many bags can afford
    how_many = money_in_wallet // sweet_price
    # Calculate how much money they will cost
    how_much = how_many * sweet_price
    # Calculate how much money will be left
    money_left = money_in_wallet - how_much
    # Tell the user calculation results in specific format
    return f"\nIf the price is {sweet_price}p and you have {money_in_wallet}p, then \
     \nyou will be able to buy {how_many} bags with {money_left}p left over."


def main():
    # Prompt the user for the price of a bag of sweets in pennies
    sweet_price = is_input_valid('What is the price of a bag of sweets in pennies? ¢')
    # Prompt the user for the amount of money they have in pennies
    money_in_wallet = is_input_valid('What is the amount of money you have in pennies? ¢')
    return calc_how_many(sweet_price, money_in_wallet)

print(main())