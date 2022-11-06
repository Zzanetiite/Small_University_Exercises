user_text = input('Please enter some text: ')
vowels = 'aeiou'
count = 0

for letter in user_text:
    if letter in vowels:
        count += 1

print('Vowels in the provided text: ' + str(count))
