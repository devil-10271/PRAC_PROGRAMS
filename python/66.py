class test:
    com_name='Google'
    noe=0
    def __init__(self,name):
        self.name=name
        test.noe+=1

    def info(self):
        print(f'{self.name} is {self.noe} in {self.com_name}')

test.com_name='Microsoft'.capitalize()
a=test('sahil')
a.com_name='Apple'
a.info()
b=test('rahil')
b.info()
c=test('sundar')
c.info()