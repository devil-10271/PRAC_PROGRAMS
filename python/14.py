a=int(input('Enter you age : '))

print('\n\n#','if-else'.center(25))
if (a>18):
    print(f'your age is {a}')
    print(f'you are an adult.')
else:
    print(f'your age is {a}')
    print(f'you are a kid.')

print('\n\n#','elif'.center(25))
if(a>18 and a<100):
    print(f'{a} is your age and it is greater than 18.')
elif(a==18):
    print(f'your age is 18.')
else:
    print(f'your age is less than.')

print('\n\n#','if else --nested'.center(25))
if(a>120):
    print(f'!!!! your is greater then 120 !!!!.\n may be this is invalid age.')
    b=input('Is correct your age is greater then ( Y/N or y/n) : ')
    if(b=='N' or b=='n'):
        print('please reenter your age : '.capitalize)
        print('please restart the code..........'.capitalize)
    elif((b!='N' or b!='n') or b!='Y' or b!='y'):
        print('!!!!     print give invalid input     !!!!')
    else:
        print('age is too high')

else:
    print('your age is normal.')