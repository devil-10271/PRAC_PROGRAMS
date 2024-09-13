def greet(fun):
    def mfun(*args,**kwargs):
        print('morning')
        fun(*args,**kwargs)
        print('thank you..\n')
    return mfun


@greet
def mor():
    print('hello world')

@greet
def add(a,b):
    print(a+b)

mor()
greet(add)(4,5)

