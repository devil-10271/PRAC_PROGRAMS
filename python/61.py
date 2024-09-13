class emp:
    def __init__(self,name,id,add):
        self._name=name
        self._id=id
        self._add=add

    def info(self):
        print(f'{self._name} is {self._id} and they lived {self._add} {self.__dir__()}')


class e1(emp):
    def __init__(self,type):
        self.type=type
        
    def typeofemp(self):
        print(f'{super()._name} is a {self.type}')


a=emp('sahil',111,'nikol')
a.info()
b=e1('name')
b.typeofemp()