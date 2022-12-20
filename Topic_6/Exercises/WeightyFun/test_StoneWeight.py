import unittest

from StoneWeight import StoneWeight


class TestCar(unittest.TestCase):

    def test_the_output_string_correct(self):
        # Arrange
        data = StoneWeight(1, 20, 3)
        data2 = StoneWeight(3, 1, 1)
        data3 = StoneWeight(0, 0, 0)
        data4 = StoneWeight(0, 2, 20)
        data5 = StoneWeight(1, 0, 0)

        # Act
        text = data.produce_weights_text()
        text2 = data2.produce_weights_text()
        text3 = data3.produce_weights_text()
        text4 = data4.produce_weights_text()
        text5 = data5.produce_weights_text()

        # Assert
        self.assertEqual('2 stones 6 pounds 3 ounces', text)
        self.assertEqual('3 stones 1 pound 1 ounce', text2)
        self.assertEqual('', text3)
        self.assertEqual('3 pounds 4 ounces', text4)
        self.assertEqual('1 stone', text5)

    def test_properties(self):
        # Arrange
        data = StoneWeight(13, 5, 6)

        # Assert
        self.assertEqual(13, data.weight_in_stones)
        self.assertEqual(5, data.weight_in_pounds)
        self.assertEqual(6, data.weight_in_ounces)
        self.assertEqual(187, data.total_weight_in_pounds)
        self.assertEqual(2992, data.total_weight_in_ounces)
        self.assertEqual(84.82, data.total_weight_in_kgs.weight_in_kgs)

    def test_BMI_producer(self):
        # Arrange
        person_BMI = StoneWeight(10, 5, 6).produce_BMI_of_person_this_weight(175)

        # Assert
        self.assertEqual(21.48, person_BMI)

# this runs the test automatically
if __name__ == '__main__':
    unittest.main()