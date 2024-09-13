class Animal:
    def __init__(r,type1,spece):
        r.type=type1
        r.species=spece

    def ani_sound(r):
        print(f'{r.type} is making this type of sound')


class Cat(Animal):
    def __init__(r,Name,color):
        r.Name=Name
        r.color=color
        # Animal.__init__(r,type,spece='cat')

    def ani_sound(r):
        print(f'{r.name} is maki{r.color}  ng sound "Meow".')


ani=Animal('4 leg','cat')
ani.ani_sound()
cat=Cat('tom','blue')