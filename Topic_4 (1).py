from datetime import datetime
import math

'''
# way to get timestamps
def print_time():
    """
    prints time
    :return: time
    """
    print(datetime.now())
    print()


print_time()
print('Hello')
print_time()

my_name: str = 'Zanete'


# saying True for uppercase adds a default value
def get_initial(name=my_name, \
                force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


print(get_initial(my_name))


def print_vat(gross, vatpc=17.5, message='Summary:'):
    net = gross / (1 + (vatpc / 100))
    vat = gross - net
    print(message, 'Net: {0:5.2f} Vat: {1:5.2f}'.format(net, vat))


print_vat(9.55)


def calc_vat(gross, vatpc=17.5):
    net = gross / (1 + (vatpc / 100))
    vat = gross - net
    return [f'{net:05.2f}', f'{vat:05.2f}']


result = calc_vat(42.30)

print(calc_vat(9.55))
'''

# Lambda functions - anonymous functions
'''
def double(n):
    return n*2
'''
# does the same as above double function
double = lambda n: n * 2
# used with a comparison
larger = lambda a, b: a if a > b else b
print(double(2))
print(larger(2, 3))

names = ["Alan", "Gregory", "Zlatan", "Jonas", "Tom", "Augustine"]
names.sort(key=lambda x: len(x))
print(names)

# syntax is - lambda arguments: expression
# Lambda functions can have any number of
# arguments but only one expression. The expression
# is evaluated and returned. Lambda functions can be
# used wherever function objects are required.

'''
def add(n1, n2):
    return n1 + n2
'''
add = lambda n1, n2: n1 + n2
print(add(10, 20))

numbers = [1, 2, 3, 4, 5]
'''
squared_nums = []
square = lambda n: n**2

for n in numbers:
    squared_nums.append(square(n))
'''
squared_nums = list(map(lambda n: n ** 2, numbers))
print(squared_nums)

num1 = [4, 5, 6]
num2 = [5, 6, 7]

# map function takes a function and a list,
# and then calls the function with all items in the
# list, and returns a new list which contains results
# of function for each item
result = map(lambda n1, n2: n1 + n2, num1, num2)
print(list(result))

numbers = [234, 3245, 639, 550, 654]
# filter function - takes a list and a function
# and returns list with list arguments that are True for func,
even_numbers = filter(lambda n: n % 2 == 0, numbers)
print(list(even_numbers))