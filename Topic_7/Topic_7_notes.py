try:
    # number = int(input('Please enter a number:'))
    number = 10
    if number < 0:
        print('Cannot be negative')
    else:
        print(number)
except ValueError:
    print('Invalid Input.')
except ZeroDivisionError:
    print('Divided by zero.')


expression = ZeroDivisionError  # ZeroDivision Error, ValueError
# variable = err  # as error, e, err
x = 42
y = 10

try:
    print(x/y)
    # or pass
except expression as variable:
    # pass
    print('Not allowed to divide by zero.')
else:
    # pass
    print('Statement if there is no exception.')
finally:
    #  pass
    print('Final statements.')

print()

# MODULES
'''
# It is Python file that can be imported in Python
# Many modules available in Python Module Index.

# import module as namespace
import helpers

# import all into current namespace
from helpers import *

# import specific items into current namespace
from helpers import display

'''

# INSTALL PACKAGES
'''
# install an individual package
pip install colorama

# install from a list of packages
pip install -r requirements.txt

# requirements.txt
colorama
'''

import random
print(random.randint(2, 10))


import re

str = "Peter Piper picked a peck of pickled peppers. " \
      "A peck of pickled peppers Peter Piper picked. " \
      "If Peter Piper picked a peck of pickled peppers, " \
      "Where’s the peck of pickled peppers Peter Piper picked?"

Myvar = re.findall("pick", str)

print(Myvar)


import re
string = 'Red and yellow and pink and green, purple and orange and blue I can sing a rainbow'
result = re.sub('red|yellow|pink|green|purple|orange|blue', 'black', string)
print(result)


import re
quote = "Here's looking at you kid"
x = re.split("\s", quote, 3)
print(x)

try:
    print('something try')
except ValueError:
    print('something except')
else:
    print('something else')


def foo():
    try:
        return 'To me'
    finally:
        return 'To you'


k = foo()
print(k)

print('1' == 1)
def foo1():
    try:
        print('To me')
    finally:
        print('To you')


k = foo1()
print(k)

