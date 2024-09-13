tup=('hello ', ' world', 1, 2 ,4)

# tuple are imutable but we change the tuple using type-casting 

tup=list(tup)
print(tup)
tup.insert(4,3)
tup=tuple(tup)
print(tup)

