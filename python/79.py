class test:
    def __init__(r,name):
        r.name = name

    def show(r):
        print(f'my name is {r.name}'.capitalize())
    
class test1():
    def __init__(r,color):
        r.color= color

    def show(t):
        print(f'my favrite color is {t.color}')


class main_test(test,test1):
    def  __init__(self,name,color):
        self.name=name
        self.color=color    



a=main_test('sahil','black')
print(a.name)
print(a.color)

a.show()
print(main_test.mro())
