class one:
    def __init__(self,val):
        self.val=val
    
    @property
    def multen(self):
        return self.val*10

    @multen.setter
    def multiten(self,var):
        return var/10
    

a=one(10)
print(a.val)
# print(a.multen(123))
# print(b)

        