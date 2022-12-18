'''
Code a program that:
Opens a file called teams.txt
Inputs and writes at least 5 rows of comma separated data made
up of a numeric team ID, team name, team value, year
established and strip colour. Something like the following:
1, Acton Acolytes, 968.45, 1991, Green
2, Burnley Burghers, 1466.33, 2016, Red
3, Coventry Casuals, 2087.99, 2015, Blue
4, Darnley Donuts, 5.99, 2017, Yellow
5, Eltham Eejits, 2021.01, 2020, Pink

'''

# Data to write in the file
the_Teams_data = ['1, Acton Acolytes, 968.45, 1991, Green',
                  '2, Burnley Burghers, 1466.33, 2016, Red',
                  '3, Coventry Casuals, 2087.99, 2015, Blue',
                  '4, Darnley Donuts, 5.99, 2017, Yellow',
                  '5, Eltham Eejits, 2021.01, 2020, Pink'
]

# With open file teams.txt as stream
with open('./teams.txt', 'w+') as stream:
    # write lines of the teams data, each in new line
    stream.writelines('\n'.join(the_Teams_data))



