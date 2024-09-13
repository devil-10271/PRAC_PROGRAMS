# a=[]
# print(type(type(a)))


# string=""
# a=[]
# if(type(a) != type(string)):
#     a=tuple(a)
#     print(type(a))


try:
    i=int(input(f'Enter Number : '))
except ValueError:
    print('not is int')
except NameError:
    print('helo')
