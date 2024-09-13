a=input(f'Enter number between 1 and 5 (type quit for exit): '.capitalize())

if(a=='quit'):
    pass
elif(int(a)>=1 and int(a)<=5):
    print('Enter value is : ',a)
else:
   raise ValueError(f'you can not enter the number between 1 and 5 or quit')
