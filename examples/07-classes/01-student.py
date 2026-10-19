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
