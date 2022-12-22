def my_func(*arguments):
    if not all(arguments):
        raise ValueError('False argument in my_func')


try:
    my_func('Tom', '', 42)
except (ValueError, NameError) as err:
    print('Oops:', err)
