import re

name = "Johnathon Johnson"
m = re.search(r'(?im)^john', name)
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())
