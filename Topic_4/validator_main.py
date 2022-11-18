from validator import Validator

username = 'Reval'
validator = Validator()
if validator.username_is_valid(username):
    print('Username is valid')
else:
    print('Usernami is invalid')