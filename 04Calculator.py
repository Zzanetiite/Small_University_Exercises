def menu():
    '''
    Menu of the app. Shows choices and calls functions
    :return: functions
    '''
    # Ask user for input
    msg1 = 'Please enter a number: '
    x = checkIntInput(msg1)
    y = checkIntInput(msg1)

    # print the menu with choices
    print(' ----- MENU ----- \
    \n Operands and their symbols: \
     \n *Add           + \n *Subtract      - \
     \n *Multiply      * \n *Divide        / \
     \n *Square        ^2 \n *Power         ^y \
     \n------------------\
     \n To EXIT press "e"')

    # ask user what they would like to do
    msg2 = 'Please enter your choice of operand symbol, for example, "+": '
    opr = checkMenuInput(msg2)

    if opr == 'e':
        print('EXIT chosen.')
        return ''

    else:
        return calculate(opr, x, y)

def checkMenuInput(msg):
    '''
    Checks if the user's input is valid
    :param msg: string
    :return: string
    '''
    inp = input(msg)
    while inp not in '+-*/e' and inp not in ['^y', '^2']:
        print('Invalid input. Please try again.')
        inp = input(msg)
    return inp

def checkIntInput(msg):
    inp = input(msg)
    while str.isdigit(inp) is False :
        print('Invalid input. Please try again.')
        inp = input(msg)
        continue
    return int(inp)

def calculate(opr,x,y):
    '''
    Transforms operands into actions
    :param opr:string
    :return: integer
    '''
    if opr == '*':
        return x * y
    if opr == '/':
        return round(x / y,2)
    if opr == '-':
        return x - y
    if opr == '+':
        return x + y
    if opr == '^2':
        return str(x * x) + " and " + str(y * y)
    if opr == '^y':
        return pow(x,y)
    else:
        return "Sorry! I don't know how to answer that!"

print(menu())