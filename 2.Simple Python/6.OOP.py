class Person:
    def __init__(self, name, age):
        #print("Створено об'єкт класу")
        self.__name = name # __ це приватні зміннні
        self.__age = age

    def display(self):
        print(f"Name: {self.__name}\t age: {self.__age}")

    def setName(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name=name

    def __del__(self):
        print("Даний об'єкт покинув корабель")
'''
    def __init__(self):
        print("Створено об'єкт класу")
        '''

ivan = Person("Іван", 23)

print(ivan.name)
ivan.setName("Оксана")
ivan.name="Козак"
# print(ivan.__name)
ivan.display()
#ilona = Person()
