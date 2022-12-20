import unittest

from BMI_calculator import BMICalculator


class TestKilogramWeight(unittest.TestCase):

    def test_if_properties_are_correct(self):
        # Arrange
        person = BMICalculator(60, 175)

        # Assert
        self.assertEqual(60, person.person_weight)
        self.assertEqual(1.75, person.person_height)

    def test_if_BMI_calculates_correctly(self):
        # Arrange & Act
        person_BMI = BMICalculator(60, 175).calculate_BMI()

        # Assert
        self.assertEqual(19.59, person_BMI)


# this runs the test automatically
if __name__ == '__main__':
    unittest.main()