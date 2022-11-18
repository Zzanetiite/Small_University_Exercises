import unittest
from FunWithShapes import Calcs


class FunWithShapesTests(unittest.TestCase):
    """
    Class that tests the functions in the FunWithShapes.py
    This is part of the unittest assignment.
    """

    def setUp(self) -> None:
        self.Calcs = Calcs()

    def test_call_circle_calc_with_positive_number(self):
        # Assume or Arrange
        dia_for_test = '20' # needs to be string to mimic user input
        expected_perimeter = 62.83
        expected_area = 314.16

        # Action or Act
        result_circle_perimeter, result_circle_area = self.Calcs.circle_calcs(dia_for_test)

        # Assert
        self.assertEqual(round(result_circle_perimeter, 2), expected_perimeter)
        self.assertEqual(round(result_circle_area, 2), expected_area)

# this runs the test automatically
if __name__ == '__main__':
    unittest.main()