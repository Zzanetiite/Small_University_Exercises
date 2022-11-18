'''
Assignment:
Create a function which takes two arguments: a value
and a list.
The function appends the value to the list,
then prints the contents of the new list.
Call this function several times with various values,
defaulting the list each time by NOT passing
the second parameter.
'''


def append_to_list(value, a_list=None):
    """
    function that appends a value to a given list,
    or, by default, to an empty list
    :param value: value to append to list
    :param a_list: a given list or empty list
    :return: list
    """
    # if list is empty make one
    # this is needed bcs Python re-uses a list
    # that is defined as default in the function
    if a_list == None:
        a_list = []
    # append the value
    a_list.append(value)
    # return the list with values
    return a_list


print(append_to_list('snow'))
print(append_to_list(1))
print(append_to_list(2))
print(append_to_list('snow', ['rain', 'clouds']))
print(append_to_list('snow', []))
