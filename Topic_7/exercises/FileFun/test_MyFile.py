import unittest
from MyFile import MyFile


class TestMyFile(unittest.TestCase):

    def test_non_existing_file(self):
        # Arrange
        my_file = MyFile('wordlist10001.t')

        # Act

        # Assert
        # __str__ function
        self.assertEqual("File not found.", str(my_file))
        # __len__ function
        self.assertRaises(IOError, lambda: len(my_file))
        # err_return function
        self.assertEqual(True, my_file.err_return())

    def test_existing_file(self):
        # Arrange
        my_file = MyFile('wordlist10000.txt')

        # Act
        str(my_file)

        # Assert
        self.assertEqual(my_file._error, False)

# this runs the test automatically
if __name__ == '__main__':
    unittest.main()