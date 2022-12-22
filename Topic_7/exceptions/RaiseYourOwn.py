class AgeError(Exception):
    pass


def set_current_age(age):
    if not 0 <= age <= 120:
        raise AgeError('Age must lie between 0 and 120')


try:
    set_current_age(-3)
except AgeError as err:
    print('Error:', err)
