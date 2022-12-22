def my_func():
    try:
        f = open('foo')
    except FileNotFoundError as err:
        print(err)
    else:
        print('Everything is OK')
    finally:
        print("Finally block")

try:
    my_func()
except OSError:
    print('An OS error occurred')

print('We are all done')
