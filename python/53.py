def cube(a):
    return a*a*a


l=[1,2,3,4,5,6]
li=list()

for i in l:
    li.append(cube(i))

newli=set(map(cube,li))

newli=list(filter(lambda a: True ,l))

print(newli)
print(l)
print(li)