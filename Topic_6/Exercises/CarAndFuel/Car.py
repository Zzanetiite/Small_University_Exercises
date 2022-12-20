class Car:

    def __init__(self, fuel_efficiency=50, fuel_in_tank=0):
        self.fuel_in_tank = fuel_in_tank  # gallons
        self.fuel_efficiency = fuel_efficiency  # miles per gallon

    def drive(self, distance_miles):
        # calculate how much fuel was used
        gallons_spent = distance_miles / self.fuel_efficiency
        # reduce fuel in the tank
        self.fuel_in_tank -= gallons_spent

    def add_fuel(self, amount):
        self.fuel_in_tank += amount


