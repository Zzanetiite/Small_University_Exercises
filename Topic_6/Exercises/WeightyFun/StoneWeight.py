from FormatWeights import FormatWeights
from KilogramWeight import KilogramWeight
from BMI_calculator import BMICalculator


class StoneWeight:

    def __init__(self,
                 weight_in_stones=0,
                 weight_in_pounds=0,
                 weight_in_ounces=0):
        self.weight_in_stones = weight_in_stones
        self.weight_in_pounds = weight_in_pounds
        self.weight_in_ounces = weight_in_ounces

        # Fix user input
        if self.weight_in_ounces >= 16:
            self.weight_in_pounds += self.weight_in_ounces // 16
            self.weight_in_ounces -= (self.weight_in_ounces // 16) * 16

        if self.weight_in_pounds >= 14:
            self.weight_in_stones += self.weight_in_pounds // 14
            self.weight_in_pounds -= (self.weight_in_pounds // 14) * 14

        # Calculate properties as per assignment
        self.total_weight_in_pounds = int(self.weight_in_stones * 14 + self.weight_in_ounces * 0.0625 + self.weight_in_pounds)
        self.total_weight_in_ounces = int(self.total_weight_in_pounds * 16)
        self.total_weight_in_kgs = KilogramWeight(self.total_weight_in_ounces * 0.0283495)

    def produce_weights_text(self):
        # make a list of formatted text
        text = [FormatWeights(self.weight_in_stones, 'stone').return_text(), FormatWeights(self.weight_in_pounds, 'pound').return_text(), FormatWeights(self.weight_in_ounces, 'ounce').return_text()]
        # filter takes the empty instances out
        return ' '.join(filter(None, text))

    def produce_BMI_of_person_this_weight(self, height_in_cm=175):
        return BMICalculator(self.total_weight_in_kgs.weight_in_kgs, height_in_cm).calculate_BMI()


