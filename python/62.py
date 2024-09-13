class test:
    def __init__(self,name):
        self.__name=name
        self._name='rahil'
        self.name='monil'

    def info(self):
        print(f'{self.__name} {self._name} ,, {self.name}')


class test2(test):
    pass


obj=test('sahilkfjfkjf ')
print(obj.name)
print(obj._test__name)
print(obj._name)
obj.info()