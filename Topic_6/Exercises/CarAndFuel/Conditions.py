'''
•	Create a project called CarAndFuel.
Give the project 2 classes, CarTester and Car which will contain the
‘car’ functionality and be tested.
•	Implement the Car classwith the following functionality:
•	A car has a certain fuel efficiency (measured in miles/gallon)
and a certain amount of fuel in the gas tank.
•	The efficiency should be passed as a parameter to the Car class’s
constructor, and the initial fuel level should be 0.
See the code below for an example of expected usage
•	Car should have a drive  method that simulates driving the car
for a certain distance, reducing the amount of petrol in the fuel tank.
The method should take a parameter that specifies the distance (in miles)
the car will travel.
•	Give the Car class a read-only property called petrol_in_tank, that
returns the current amount of petrol in the fuel tank.
•	Add a method to the class called add_petrol() that will be used to
 add petrol to the fuel tank.
•	You may assume that the drive() method is never called with a
 distance that consumes more than the available fuel, i.e.
 don’t worry about running out of petrol.
•	Test the ‘Car’ class fully by adding unit tests to the CarTester class.
•	Sample usage:
# Arrange
car = Car(50) # 50 miles per gallon

# Act
car.add_petrol(5)     # Tank 5 gallons
car.drive(205)        # Drive 205 miles

# Assert
self.assertEqual(0.90, car.petrol_in_tank)# get fuel

'''