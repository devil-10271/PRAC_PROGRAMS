class test:
    name='hello'
    def ___init__(self):
        self.name='hello'
        self.classs='world'


    def printf(self):
        print(f'{self.name} and {self.classs}')
    
    def __length__(self,stri):
        return len(stri)

a=test()
b=a.length(test.name)
print(b)