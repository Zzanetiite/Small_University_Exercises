import re

str = "because as we know, there are known knowns; " \
      "there are things we know we know. " \
      "We also know there are known unknowns; " \
      "that is to say we know there are some things we do not know. " \
      "But there are also unknown unknowns—the ones we don't know " \
      "we don't know. And if one looks throughout the history of our " \
      "country and other free countries, it is the latter category that " \
      "tends to be the difficult ones"
matches = re.findall(r'know', str)
print(matches)
