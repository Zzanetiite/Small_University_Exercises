from BMI_calculator import BMICalculator


class KilogramWeight:

    def __init__(self, kgs=23.34):
        self.weight_in_kgs = round(kgs, 2)
        self.weight_in_pounds = int(self.weight_in_kgs * 2.20462)
        self.weight_in_stones = self.weight_in_pounds // 14
        self.weight_in_ounces = int(self.weight_in_kgs * 35.274)

    def __str__(self):
        return f"{self.weight_in_kgs} kgs"

    def produce_BMI_of_person_this_weight(self, height_in_cm=175):
        return BMICalculator(self.weight_in_kgs, height_in_cm).calculate_BMI()

