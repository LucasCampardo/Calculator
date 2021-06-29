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

    # Add again() function to calculate() function
    again()


def again():
    # Take input from user
    calc_again = input('''
Do you want to calculate again?
If yes, type Y
if no, type N 
    ''')

    # If user types Y, run the calculate() function
    # Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    # Accept 'n' or 'N' by adding str.upper()
    elif calc_again == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()


# Call calculate() outside of the function
# And, don't forget to call the function
welcome()
calculate()
