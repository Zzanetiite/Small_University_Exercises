import re

line = 'Perl for Perl Programmers'
cs, num = re.subn('Perl', 'Python', line)
if num:
    print(cs)
