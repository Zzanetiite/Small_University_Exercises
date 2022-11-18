'''
Create a program that displays powers of number 2.
1 to 63 (inclusive)
'''


def power_Of(n):
    """
    Takes a number and makes it the power of 2
    :param n: the times of power of 2
    :return: float, 2**n
    """

    # check if n is in the assignment range
    if not (1 <= n <= 63):
        return 'Value not in range of 1 to 63. Exiting.'
    else:
        return 2 ** n


#max_result_value = float(input('Please enter a maximum value of power: '))
max_result_value = 100000000000


# Test to check if display is according to assignment
for number in range(1, 63):
    result = int(power_Of(number))
    if result > max_result_value:
        break
    else:
        # spacings
        sp2 = 2**63
        sp2 = len(str(sp2)) # max length of the answer

        # left aligned
        #print('2 to the power of {0:<0} is {1:<30}{0:<20}{1:>10}'.format(number, str(result)))
        # other formatting method
        print('2 to the power of %-*s is %-*s%-*s%-*s' % (2, number, sp2, str(result), 2, str(number).rjust(2), 2, str(result).rjust(sp2)))
        # right aligned
       # print('{0:<10}{1:>10}'.format(str(number), str(result)))