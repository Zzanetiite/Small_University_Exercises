

class main():

    def age_in_years():
        Year = input('Please enter the year you were born: ')
        Age = 2022 - int(Year)
        return 'You are ' + str(Age) + ' years old!'


print(main.age_in_years())

