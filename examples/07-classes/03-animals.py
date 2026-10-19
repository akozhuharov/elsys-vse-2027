# Наследяване - общ родител и различна имплементация в наследниците
class Animal:
    def __init__(self, name, legs=4):
        self.name = name
        self.legs = legs

    def describe(self):
        print(self.name, "има", self.legs, "крака")

    def sound(self):
        raise NotImplementedError("Всеки вид си прави своя звук")


class Dog(Animal):
    def sound(self):                  # "реалната" имплементация
        return "Бау"


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, 2)     # super вика конструктора на родителя

    def sound(self):
        return "Чик"


animals = [Dog("Шаро"), Bird("Кики")]

for animal in animals:
    animal.describe()                 # наследена функция
    print(animal.name, "казва:", animal.sound())
