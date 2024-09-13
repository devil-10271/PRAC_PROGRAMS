class shape:
    def __init__(self,x,y):
        self.length=x
        self.breath=y
    
    def area(self):
        return self.length * self.breath
    

class circle(shape):
    def __init__(self,radius):
        self.rad=radius
        super().__init__(radius,radius)

    def area(self):
        return (22/7) * super().area()
    
    def parameter(self):
        return 2*(22/7)*self.rad
    

sha=shape(5,6)
print(sha.area())
cir=circle(2)
print(cir.area())
print(cir.parameter())



