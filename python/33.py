dic={
    'name':'Rahil',
    'age':17
}

print(dic)
print(dic['name'])
print(dic.keys())
print(dic.values())

for key in dic.values():
    print(key)

print(dic.items())


for i,j in dic.items():
    print(f'{i} : {j}'.title())