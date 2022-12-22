try:
    f = open("foo")
except FileNotFoundError as err:
    print("Could not open",
          err.filename, err.args[1])
    print("Exception arguments:", err.args)
