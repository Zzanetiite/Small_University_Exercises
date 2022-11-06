n = input('Please input a number: ')


def factorial(n):
    """
    Takes a number and gives back it's factorial
    :return: factored n
    """
    # first factorial of any number is one
    result = 1

    # factoring using a loop
    for num in range(1, int(n) + 1):
        result = result * num

    return result


def factorial_rec(n):
    """
    Takes a number and gives back it's factorial
    :return: factored n
    """
    n = int(n)
    # base case
    if n == 1:
        return 1
    # any other case
    else:
        return n * factorial_rec(n - 1)


print(factorial(n))
print(factorial_rec(n))

