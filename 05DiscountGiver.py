def main():
    price = check_input()
    if type(price) == str:
        return price
    else:
        discount = calc_discount(price)
        return str(discount) + '%'


def check_input():
    while True:
        price = input('Please enter item price: ')
        try:
            if float(price) < 0.0:
                return 'Error! Price of an item cannot be negative.'
            if float(price) >= 0.0:
                return float(price)
        except:
            print('Invalid value. Please enter a number.')


def calc_discount(price):
    if price >= 400:
        return 40
    if 200 <= price <= 400:
        return 20
    if 100 <= price <= 200:
        return 10
    if price < 100:
        return 0


print(main())
