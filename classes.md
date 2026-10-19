# Класове
Класовете се дефинират с ключова дума `class` и при извикване на класът се създава обект от този клас:
```python
class Organization:
    name = ""
    size = 0


o = Organization()
o.name = "Elsys"
o.size = 520
print(o.name, o.size)
```
*Достъпваме променливите и функциите с точка(.)*

## Конструктур
Това е функция, която се извиква на първо място при създаване на нов обект и позволява начални операции по новият обект. Едно от най-срещаните операции е присвояването на променливи подадени на конструктура към текущия обект
```python
class Organization:
    # self е винаги първа позиция и е референция към текущият обект. Ако направим два обекта от класът, то тогава self.name ще има различни стойности спрямо всеки обект
    def __init__(self, name, size=0):
        self.name = name
        self.size = size

    def print(self): # Дефинирането на функциите става чрез def и подаваме self и други параметри към функцията
        print(self.name, self.size)
o = Organization("Elsys", 520)
o.print()
```

## Наследяване
При дефиниране на клас може да използваме друг клас, както в примера по-долу, за да получим готови предварително дефинираните функции и променливи на "родителският" клас
```python
class Shape:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print_sides(self):
        print(self.a, self.b, self.c)
    
    def perimeter(self):
        raise NotImplementedError("Not implemented")  # Очакваме това да е дефинирано само в наследяващите класове


class Triangle(Shape):
    def perimeter(self):  # Тук вече правим "реалната" имплементация на функцията
        return self.a + self.b + self.c

t = Triangle(3, 4, 5)
t.print_sides()
print(t.perimeter())
```

<!-- ПРИМЕРИ:НАЧАЛО (генерирано от tools/sync_examples.py - не редактирай ръчно) -->

## Примерни програми

Кодът е в [`examples/07-classes/`](./examples/07-classes/) — пусни го с `python3 examples/07-classes/<име>.py`.
Виж го ред по ред, с променливите и изхода на всяка стъпка, във [визуализатора](./visualizer.html).

### 1. Клас Student
*конструктор, функции и два отделни обекта*

```python
# Клас Student - конструктор, функции и два отделни обекта
class Student:
    def __init__(self, name, grade):   # self е референция към текущия обект
        self.name = name
        self.grade = grade
        self.marks = []                # всеки обект получава свой списък

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def info(self):
        print(self.name, "от", self.grade, "клас, среден:", self.average())


a = Student("Petar", 9)
b = Student("Ivan", 9)       # втори обект - собствени стойности

a.add_mark(6)
a.add_mark(5)
b.add_mark(3)

a.info()
b.info()
```

Изход:
```
Petar от 9 клас, среден: 5.5
Ivan от 9 клас, среден: 3.0
```

### 2. Банкова сметка
*класът пази и променя свое състояние*

```python
# Банкова сметка - класът пази и променя свое състояние
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append("+" + str(amount))
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:            # проверка преди промяната
            print("Недостатъчна сума!")
            return self.balance
        self.balance -= amount
        self.history.append("-" + str(amount))
        return self.balance

    def statement(self):
        print(self.owner, "баланс:", self.balance, self.history)


acc = BankAccount("Nasko", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(500)        # ще откаже
acc.statement()
```

Изход:
```
Недостатъчна сума!
Nasko баланс: 120 ['+50', '-30']
```

### 3. Наследяване
*общ родител и различна имплементация в наследниците*

```python
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
```

Изход:
```
Шаро има 4 крака
Шаро казва: Бау
Кики има 2 крака
Кики казва: Чик
```

<!-- ПРИМЕРИ:КРАЙ -->
