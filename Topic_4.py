# way to get timestamps
from datetime import datetime


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
