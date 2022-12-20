class FormatWeights:

    def __init__(self, weight=1, unit='pound'):
        self.weight = weight
        self.unit = unit

    def return_text(self):
        if self.weight == 0:
            return ''
        if self.weight == 1:
            return f'{self.weight} {self.unit}'
        else:
            return f'{self.weight} {self.unit}' + 's'
