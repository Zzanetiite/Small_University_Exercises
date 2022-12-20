import unittest

from Car import Car


class TestCar(unittest.TestCase):

    def test_the_amount_of_fuel_is_correct(self):
        # Arrange
        car = Car(50)

        # Act
        car.add_fuel(5)  # Tank 5 gallons
        car.drive(205)  # Drive 205 miles

        # Assert
        self.assertEqual(0.90, round(car.fuel_in_tank, 2))  # get fuel


# this runs the test automatically
if __name__ == '__main__':
    unittest.main()