import random


def generate_num():
    # range according to assignment
    first = 1
    last = 39

    # the amount of numbers to be generated
    n = 6

    # place to store numbers
    # choosing list as it is easy to work with
    random_numbers = []

    # while n is more than 0
    while n > 0:
        # generate numbers & add them to tuple list
        random_numbers.append(random.randint(first, last))
        # deduct n by 1
        n -= 1

    return 'Your random numbers are: ' + str(random_numbers)


print(generate_num())
