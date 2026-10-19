# Квадратно уравнение - math.sqrt
import math                       # включваме целия модул

a = 1
b = -5
c = 6

d = b ** 2 - 4 * a * c            # дискриминанта
print("D =", d)

if d < 0:
    print("Няма реални корени")
else:
    root = math.sqrt(d)           # функцията се вика с име_на_модула.функция
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)

print("Закръгляне нагоре:", math.ceil(2.1))
print("Пи:", round(math.pi, 4))
