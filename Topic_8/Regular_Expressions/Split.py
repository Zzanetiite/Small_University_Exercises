import re

line = 'root:;0.0:superuser,/root;/bin/sh'
elems = re.split('[:;.,]', line)
print(elems)
