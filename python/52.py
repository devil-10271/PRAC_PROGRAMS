add = lambda a,b: a+b
print(add(5,5))

def add1(fun):
    return fun*2

fun=lambda a: int(a)-1

print(add1(fun(5)))