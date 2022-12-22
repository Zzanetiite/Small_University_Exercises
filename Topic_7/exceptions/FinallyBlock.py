def my_func():
    try:
        f = open("foo")
    finally:
        print("Finally block")

try:
    my_func()
except OSError:
    print("An OS error occurred")
