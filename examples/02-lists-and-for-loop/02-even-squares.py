# range със стъпка и continue - квадрати на числата
squares = []

for i in range(1, 11):          # числата от 1 до 10
    if i % 2 != 0:
        continue                # нечетните се прескачат
    squares.append(i * i)       # append добавя в края на списъка

print("Квадрати на четните:", squares)

# range с три аргумента: начало, край, стъпка
for i in range(0, 25, 5):
    print("Стъпка 5:", i)

print("Обратно с отрицателна стъпка:")
for i in range(3, 0, -1):
    print(i)
