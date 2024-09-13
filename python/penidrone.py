a=int(input('Enter the number : '))
b=a
null=0

for i in range(len(str(a))):
    if(a==0):
        print("you enter a zero number.")
    else:
        remainder=a%10
        a=a//10
        null=(null*10)+remainder

if(b==null):
    print('Number is a penidrome number.')
else:
    print('Nummber is not a penidrome number.')
