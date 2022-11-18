# Task 1
aList = [1, 2, 3, 4, 5, 6, 7]
aList_cubes = list(map(lambda x: x**3, aList))
print(aList_cubes)

# Task 2
list1 = ["Kamran", "", "Saeed", "Sadia", "", "Anne"]
list_result = []

for i in range(len(list1)):
    if list1[i] != "":
        list_result.append(list1[i])
print(list_result)

# Task 3
list2 = [5000, 6000]
list2[1] = list2[1] + 600
print(list2)

# Task 4
list3 = [300, 400, [5000, 6000], 500]
list3[2][1] += 600
print(list3)

# Task 5
list4 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list4[2][2][1] += 600
print(list4)

# Task 6
people = [['Fred', 'Flintstone', 23],
         ['Barney', 'Rubble', 22],
         ['Homer', 'Simpson', 45],
         ['Marge', 'Simpson', 43]]

for row in people:
    row[2] += 1
print(people)

# Task 7
people2 = [['Fred', 'Flintstone', 23],
         ['Barney', 'Rubble', 22],
         ['Homer', 'Simpson', 45],
         ['Marge', 'Simpson', 43]]

for row in people2:
    if row[0] == 'Homer' and row[1] == 'Simpson':
        row[2] += 1
print(people2)

# Task 8
aList3 = [100, 200, 300, 400, 500]
aList3.reverse()
print(aList3)

