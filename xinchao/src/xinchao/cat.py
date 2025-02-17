class Cat:
    def __init__(self, name):
        self.__name = name
    def describe(self):
        return(self.__name)
name = 'khanh'
a = Cat(name)
# print(a.describe())
print(a.describe())