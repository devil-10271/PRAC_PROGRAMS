def avg(list_num):
    sum=0
    for j in list_num:
        sum=j+sum
    return sum/len(list_num)


a=[]
totnum=int(input('How many numbers do you have : '))
print()
for i in range(1,totnum+1):
    b=float(input(f'Enter the {i} number : '))
    a.append(b)

average=avg(a)
print(average)

a=None
print(a)