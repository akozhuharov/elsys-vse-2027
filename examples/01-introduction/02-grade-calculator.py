# Калкулатор на оценка - деление, остатък и преобразуване на типове
points = 47        # int - получени точки
maximum = 60       # int - максимални точки

percent = points / maximum * 100   # / винаги дава float
print("Процент:", percent)

rounded = int(percent)             # int() отрязва дробната част
print("Закръглено надолу:", rounded)

if rounded >= 90:
    grade = 6
elif rounded >= 75:
    grade = 5
elif rounded >= 60:
    grade = 4
elif rounded >= 50:
    grade = 3
else:
    grade = 2

print("Оценка:", grade)
print("Точки до отличен:", maximum * 90 // 100 - points)
