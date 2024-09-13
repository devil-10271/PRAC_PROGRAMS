s='sahil'
for ind,i in enumerate(s):
    print(f'{ind} = {i}')
print()
for i in enumerate(s,start=1):
    print(f'{i}')

array=['mango','apple','banana']
print()
for ind,i in enumerate(array):
    print(f'{ind} = {i}')
    for ind2,j in enumerate(i,start=1):
        print(f'{ind2} = {j}')
    print()