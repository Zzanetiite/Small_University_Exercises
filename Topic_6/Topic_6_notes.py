class PresenterPascalCasing:
    def __init__(self, name):
        # constructor
        self.name = name

    def say_hello(self):
        # method
        print('Hello ' + self.name)

    @property
    # sets a property
    def name(self):
        print('In the getter')
        # as property use the underscore _name
        return self._name

    @name.setter
    # uses value to check if name is the same
    def name(self, value):
        print('in the setter')
        # cool validation here
        self._name = value


# Using the class to assign name to presenter
presenter = PresenterPascalCasing('Chris')
# renaming previously given name variable
presenter.name = 'Christopher'
# Using one of the class methods
presenter.say_hello()


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender.upper()

    def say_hello(self):
        print('Hello ' + self.name)

    def __str__(self):
        return self.name


# INHERITANCE
class Student(Person):
    def __init__(self, name, school):
        # when derive from the class you
        # need to call parent constructor
        # by using super()
        super().__init__(name)
        self.school = school

    def sing_school_song(self):
        print('Ode to ' + self.school)

    def __str__(self):
        return f'{self.name} attends {self.school}'


# Assigning student to class
student = Student('Christopher', 'UMD')
# Calling method say_hello() of Student class
student.say_hello()
# Calling method sing_school_song of Student class
student.sing_school_song()
person = Person('Christopher')
# Can call it because of __str__ method
# overrode name to string
print(person)
print(student)

# What are you?
# checking if student
print(f'Is this a student? {isinstance(student, Student)}')
print(f'Is this a person? {isinstance(student, Person)}')
print(f'Is Student a Person? {issubclass(Student, Person)}')


# inheritance - Employee from Person
class Employee(Person):
    def __init__(self, name, gender, dept):
        # name and gender are inherited from Person class
        super().__init__(name, gender)
        self.dept = dept

