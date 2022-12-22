filename = "foo"
try:
    print('Trying to open', filename)
    f = open(filename)
except FileNotFoundError:
    errmsg = filename + " not found"
except (TypeError, ValueError):
    errmsg = "Invalid filename"
    print(errmsg)

if errmsg != "":
    exit(errmsg)
