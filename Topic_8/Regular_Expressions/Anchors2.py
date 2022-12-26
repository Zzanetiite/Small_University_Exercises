import re

txt = 'Stranger in a strange land'
m = re.search(r'range\b', txt)
print(m.start())

m = re.search(r'range\B', txt)
print(m.start())
