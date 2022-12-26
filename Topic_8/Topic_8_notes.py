import re

# Line to edit
line = "I'd like a piece of fruit"
# cs = changed string, num = number of changes
cs, num = re.subn('fruit', 'banana', line)
# if number is not none or True
if num:
    print(cs, num)


drink = 'A glass of Miller'
if re.search(r'Bud|Miller|Coors', drink):
    print("It's a beer!")

pattern = r'A (glass|bottle|barrel) of (Bud|Miller|Coors)'

if re.search(pattern, drink):
    print("This drink is suitable for Americans")


s = 'Ada Lovelace was the first computer programmer'
result = re.search(r'^\w+', s)
print(result.group())
result2 = re.search(r'\w+$', s)
print(result2.group())


txt = 'Stranger in a strange land'
m = re.search(r'range\b', txt)
print(m.start())
print(m.group())


