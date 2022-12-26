import re

testy = 'The quick brown fox jumps over the lazy dog'

m = re.search(r"(fox)", testy)
if m:
    print('Matched', m.groups()[0])
    print('Starting at', m.start())
    print('Ending at', m.end())
