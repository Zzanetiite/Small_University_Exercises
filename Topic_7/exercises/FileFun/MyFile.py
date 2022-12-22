import os.path
from os.path import exists as file_exists


class MyFile:
    _error = False

    def __init__(self, filename):
        self._fname = filename

    def __str__(self):
        try:
            s = open(self._fname, 'r').read()
            return s
        except IOError as err:
            self._error = True
            print(err)
            return "File not found."

    def __len__(self):
        if self._error:
            raise IOError("File not found.")
        return os.path.getsize(self._fname)

    def get_fname(self):
        return self._error

    def err_return(self):
        return self._error

