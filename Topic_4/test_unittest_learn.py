import unittest
import unittest_learn


class TestUnittestLearn(unittest.TestCase):

    # method must start with test_
    # second part after _ is the name of that
    # describes what f is testing
    def test_add(self):
        self.assertEqual(unittest_learn.add(10, 5), 15)
        # edge cases
        self.assertEqual(unittest_learn.add(-1, 1), 0)
        self.assertEqual(unittest_learn.add(-2, -2), -4)

    def test_subtract(self):
        self.assertEqual(unittest_learn.subtract(10, 5), 5)
        # edge cases
        self.assertEqual(unittest_learn.subtract(-1, 1), -2)
        self.assertEqual(unittest_learn.subtract(-2, -2), 0)

    def test_multiply(self):
        self.assertEqual(unittest_learn.multiply(10, 5), 50)
        # edge cases
        self.assertEqual(unittest_learn.multiply(-1, 1), -1)
        self.assertEqual(unittest_learn.multiply(-2, -2), 4)

    def test_divide(self):
        self.assertEqual(unittest_learn.divide(10, 5), 2)
        # edge cases
        self.assertEqual(unittest_learn.divide(-1, 1), -1)
        self.assertEqual(unittest_learn.divide(-2, -2), 1)
        self.assertEqual(unittest_learn.divide(5, 2), 2.5)
        # To test exception errors - Opt 1
        self.assertRaises(ValueError, unittest_learn.divide, 10, 0)
        # Opt 2
        with self.assertRaises(ValueError):
            unittest_learn.divide(10, 0)

'''
Tests are called using:
python3 -m unittest test_unittest_learn.py
'''

# this runs the test automatically
if __name__ == '__main__':
    unittest.main()

