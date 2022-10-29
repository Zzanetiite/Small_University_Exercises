'''
cake_list = ["Fruit", "Muffin", "Battenberg", "Wedding", "Sponge", "Coffee and Walnut", "Rainbow"]
short_cakes = [len(c) for c in cake_list if len(c) < 7]

print(short_cakes)

fruits = {"Banana": "Yellow", "Apple": "Green", "Strawberry": "Red"}
fruit = fruits.popitem()
print (fruit)

card1 = int(input("Card1= "))
card2 = int(input("card2= "))
if card2 > 5:
    card1 += card2
print("Result:",card1)


card1 = int(input("Card1= "))
card2 = int(input("card2= "))
opr = input('Please input an operand of "+, -, /" or "*"')
if opr == "+":
    result = card1 + card2
elif opr == "*":
    result = card1 * card2
elif opr == "-":
    result = card1 - card2
elif opr == "/":
    result = float(card1 / card2)
else:
    result = "Invalid input."

print("Result:",result)

count = 0
valSum = 0
while True:
    inp = input('Please enter a card value or "s" to stop: ')
    if inp == "s":
        break
    else:
        count += 1
        valSum += int(inp)
print("Count of cards:", count,",sum of cards:",valSum)
'''

suitDict = {'spades':0,'clubs':0,'diamonds':0,'hearts':0}
theLargestValue = 0

while theLargestValue < 5 :

    # Requesting user inputs for suit
    suit = input('Please enter the suit of the card. "s" for spades,\n "c" for clubs, "d" for diamonds, "h" for hearts and "e" to exit ')
    # Test if the user wants to leave and if so -> exit
    if suit == 'e':
        print('User has exited the program.')
        break
    # Test if the input is valid and if not tell the user to try again
    if suit not in 'scdhe' :
        print('Input invalid, try again.')
        continue

    # Conversion to dict names, doing this so that it is easier for the
    # user. It is easier to input singular characters than whole words.
    if suit == 's':
        suit = 'spades'
    if suit == 'd':
        suit = 'diamonds'
    if suit == 'h':
        suit = 'hearts'
    if suit == 'c':
        suit = 'clubs'

    # for every input add it to the appropriate sut value in dict
    suitDict[suit] += 1
    print('\nA card of', suit, 'has been added to the deck.\n')
    # then extract the value and compare it to theLargestValue
    if suitDict[suit] > theLargestValue:
        theLargestValue = suitDict[suit]
    # If the largestvalue is 5 return the dict
    if theLargestValue == 5:
        print('Following cards have been submitted: ', suitDict)

