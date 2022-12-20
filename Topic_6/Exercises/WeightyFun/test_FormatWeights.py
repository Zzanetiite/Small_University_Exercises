import unittest

from FormatWeights import FormatWeights


class TestCar(unittest.TestCase):

    def test_the_output_string(self):
        # Arrange
        pounds = FormatWeights(50, 'pound')
        pound = FormatWeights(1, 'pound')

        # Act
        text = pounds.return_text()
        text2 = pound.return_text()

        # Assert
        self.assertEqual('50 pounds', text)
        self.assertEqual('1 pound', text2)


# this runs the test automatically
if __name__ == '__main__':
    unittest.main()