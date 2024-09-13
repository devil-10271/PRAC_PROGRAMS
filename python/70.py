class test:
    def __init__(self,name,salary):
        self.name1=name
        self.salary1=salary

    @classmethod
    def test(self,str1ing):  # here self take a class test
        return self(str1ing.split(',')[0],int(str1ing.split(',')[1]))


    def info(self): 
        print(f'name : {self.name1}\nsalary : {self.salary1} ')
        print(type(self.name1),type(self.salary1))



if __name__=="__main__":
    a=test('sahil',12344)
    a.info()

    string='hiiiii,67686'
    a2=test.test(string)
    a2.info()

