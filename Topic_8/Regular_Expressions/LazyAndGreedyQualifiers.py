import re

line = "<em>I'm saving my strength for running</em>"
m = re.search(r'<.+>', line) # Greedy
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())

m = re.search(r'<.+?>', line) # Lazy
if m:
    print('Starting at', m.start())
    print('Ending at', m.end())
