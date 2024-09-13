class Animal : 
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def show_details(self):
        print(f'Name : {self.name}')
        print(f'Species : {self.species}')


class Cat(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species='Cat')
        self.breed=breed

    def show_details(self):
        Animal.show_details(self)


class breead(Cat):
    def __init__(self,name,color):
        Cat.__init__(self,name,breed='consumer')
        self.color=color


    def show_details(self):
        Cat.show_details(self)
        print(f'breed : {self.breed}')
        print(f'colour : {self.color}')


a=breead('tommy','black')
a.show_details()

print(a.name)
print(a.breed)
print(a.color)
print(a.species)
