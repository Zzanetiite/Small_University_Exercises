import re

s = 'Ada Lovelace was the first computer programmer'
result = re.search(r'^\w+', s)
print(result.group())
result2 = re.search(r'\w+$', s)
print(result2.group())
