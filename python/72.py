class parent:
    def __init__(hi):
        hi.name='sahil'
        hi.job='programmer'

    def info(hi):
        print(f'name : {hi.name}\njob : {hi.job}')


class child(parent):
    def __init__(chi,name1=None,job1=None):
        chi.name='harry' or name1
        chi.job='hr'or job1
        super().__init__()
    
    def info11(chi):
        print(f'name : {chi.name}\njob : {chi.job}')

a=parent()
print(a.__dict__)
b=child('name','job')
print(b.__dict__)
print(b.info())