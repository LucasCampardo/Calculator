def welcome():
    print('''
Welcome to Calculator
''')


def calculate():
    operation = input('''
______________________________________________________________________
| Please, type in the math operation you would like to complete:     |
| + for addition                                                     |
| - for subtraction                                                  |
| * for multiplication                                               |
| / for division                                                     |
| % for modulo                                                       |
______________________________________________________________________
    ''')

    n1: int = int(input('Type a number: '))
    n2: int = int(input('Type other number: '))

    if operation == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif operation == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif operation == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif operation == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)

    elif operation == '%':
        print('{} % {} = '.format(n1, n2))
        print(n1 % n2)

    else:
        print('You have not typed a valid operator, try again.')

    again()


def again():
    # Take input from user
    calc_again = input('''
Do you want to calculate again?
If yes, type Y
if no, type N 
    ''')

    if calc_again.upper() == 'Y':
        calculate()

    elif calc_again == 'N':
        print('See you later.')

    else:
        again()


welcome()
calculate()
