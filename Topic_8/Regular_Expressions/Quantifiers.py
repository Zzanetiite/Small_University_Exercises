import re

value = '0748652123'
m = re.search(r'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$'
              , value)
if m:
    print('The value is valid!')
