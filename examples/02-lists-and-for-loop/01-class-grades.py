# Статистика за оценки - обхождане на списък с for
grades = [4, 6, 3, 5, 6, 2]
print("Оценки:", grades)

total = 0
best = grades[0]      # приемаме първия елемент за най-голям

for grade in grades:
    total += grade
    if grade > best:
        best = grade

average = total / len(grades)   # len() връща броя елементи
print("Сума:", total)
print("Средно:", average)
print("Най-висока:", best)
