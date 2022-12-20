class BMICalculator:

    def __init__(self, person_weight=70, person_height=175):
        self.person_weight = float(person_weight)  # kgs
        self.person_height = person_height * 0.01  # cm

    def calculate_BMI(self):
        BMI = self.person_weight / (self.person_height * self.person_height)
        return round(BMI, 2)

