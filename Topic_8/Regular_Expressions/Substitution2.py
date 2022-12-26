import re

line = 'Perl for Perl Programmers'

cs, num = re.subn('Perl', 'Python', line, 1)
if num:
    print(cs)