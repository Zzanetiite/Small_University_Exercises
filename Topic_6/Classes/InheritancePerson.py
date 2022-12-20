class Person:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender.upper()

    def __str__(self):
        # printed when self is called
        return "Name: " + self.__name + \
               " Gender: " + self.__gender
