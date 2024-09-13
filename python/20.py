print(f'print()    is aBuilt-in function',end="\n\n") #-------> Built-in function

def avg():
    a=int(input('enter the first number : '))
    b=int(input('enter the second number : '))
    c=int(input('enter the third number : '))

    return (a+b+c)/3
a=avg()
print(a)