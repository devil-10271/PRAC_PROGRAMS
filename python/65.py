class test:
    def __init__(self,num):
        self.num=num

    @staticmethod
    def add(a,b):
        num=a+b
        return num
    
a=test(5)
print(a.num)
print(a.add(5,5))

        