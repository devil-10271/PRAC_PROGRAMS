class test:
    def __init__(r,i,j,k):
        r.i=i
        r.j=j
        r.k=k
    
    def __str__(r):
        return f'{r.i}i + {r.j}j + {r.k}k'
    
    def __add__(r,otr_cla):
        return test(r.i+otr_cla.i, r.j+otr_cla.j, r.k+otr_cla.k)
    
    def __sub__(r,otr_cla):
        return test(r.i-otr_cla.i, r.j-otr_cla.j, r.k-otr_cla.k)


a=test(1,2,3)
print(a)
b=test(3,2,1)
print(b)
print(a+b)
print(a-b)
print(type(a-b))