class person:
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ
    def info(self):
        print(f'{self.name} is a {self.occ}')
        print(f'{self.name}')
    name='hello'
    print(name)

a=person('saahil','hr')

a.info()
a.name='sahil'
a.info()

