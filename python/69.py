class test:
    no=0
    def __init__(hiral,name):
        hiral.name1=name
        # hiral.no+=1

    
    @classmethod
    def change_value(hiral):
        hiral.no=10


a=test('sahio')
print(a.no)
a.change_value()
print(a.no)
