a=float(input('''Enter the first number : '''))
b=float(input('''Enter the first number : '''))

c=input('''Enter the operation are given below : 
        +
        -
        /
        x
        ''')

match c:
    case '+':
        print(f'\n\n{a+b}')
    case '-':
        print(f'\n\n{a-b}')
    case '*':
        print(f'\n\n{a*b}')
    case '/':
        print(f'\n\n{a/b}')
    case _:
        print('invalid input')

