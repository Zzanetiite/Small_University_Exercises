import unittest

from KilogramWeight import KilogramWeight


class TestKilogramWeight(unittest.TestCase):

    def test_if_conversions_are_correct(self):
        # Arrange
        kgs_weight = KilogramWeight(30)

        # Assert
        self.assertEqual(30, kgs_weight.weight_in_kgs)  # get weights
        self.assertEqual(66, kgs_weight.weight_in_pounds)
        self.assertEqual(4, kgs_weight.weight_in_stones)
        self.assertEqual(1058, kgs_weight.weight_in_ounces)

    def test_BMI_producer(self):
        # Arrange
        person_BMI = KilogramWeight(70).produce_BMI_of_person_this_weight(175)

        # Assert
        self.assertEqual(22.86, person_BMI)

# this runs the test automatically
if __name__ == '__main__':
    unittest.main()