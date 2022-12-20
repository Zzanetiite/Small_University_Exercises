from InheritancePerson import Person


class Employee(Person):
    def __init__(self, name, gender, dept):
        super().__init__(name, gender)
        self.__dept = dept
'''
If this isn't here the __str__ gets taken from
Superclass Person
    def __str__(self):
        # printed when self is called
        return "Department: " + self.__dept
        
'''
