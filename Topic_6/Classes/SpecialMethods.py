class Car:
    def __init__(self, make='Ford', model='Mondeo', colour='Black'):
        # defines attributes of the class
        self._make = make
        self._model = model
        self._colour = colour

    def __str__(self):
        # print format method
        return f'I am a {self._colour} {self._make} {self._model}'
