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
