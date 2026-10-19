# Списъци (Lists)
Списъкът е структура от данни, която служи за запазване на много стойности под една променлива. Има различни функции, които помагат с работата със списъци, като всяка функция се извиква в формат `var.func() `, където var e името на променливата, а func e функцията.
```python
# Дефинираме списък с квадратни скоби:
names = ["Petar", "Ivan", "Ogi", "Nasko"]
# Достъпът до елементи става чрез индекса, като броим от 0
names[0] # Result: Petar
# Отрицателен индекс
names[-1] # Result: Nasko
# range(обхват) - не включва елемента на затварящия индекс, в случая 3
names[1:3] # Result: ["Ivan", "Ogi"] 
# добавяне на елемент
names.append("Boyan") # Result: ["Petar", "Ivan", "Ogi", "Nasko", "Boyan"]
# Премахване на елемент по стойност
names.remove("Ogi") # Result: ["Petar", "Ivan", "Nasko", "Boyan"]
# Премахване на елемент по индекс
names.pop(0) # ["Ivan", "Nasko", "Boyan"]
```

# For цикъл
Синтаксис
```python
names = ["Petar", "Ivan", "Ogi", "Nasko"]
for i in names:
    # Ключова дума for следвана от променливата която ще приема всяка стойност(i), ключова дума in и променлива за обхождане(в случая списъка names)
    print(i)
# Petar
# Ivan
# Ogi
# Nasko
```
## range фунцкия
```python
# Генериране на числата от 0 до 99(100-1)
for i in range(100):
    print(i)
# Генериране на числата от 5 до 9
for i in range(5,10):
    print(i)
# Генериране на числата от 50 до 100 със стъпка 3
for i in range(50,101):
    print(i)
```

## Излизане от цикъл(break)
Излизането от цикъл става с ключова дума break, най-често използвана при някакво условие(if)
```python
names = ["Petar", "Ivan", "Ogi", "Nasko"]
for i in names:
    print(i)
    if i == "Ogi":
        # Когато достигне елемента със стойност Ogi ще излезем от цикъла
        break
    
```

## Продължава на цикъла(continue)
Като горният пример, само че тук не изпълняваме оставащият код в цикълния блок
```python
for i in names:
    if i == "Ogi":
        # Когато достигне елемента със стойност Ogi ще пропуснем изпълнението на print-a
        continue
    print(i)
```

<!-- ПРИМЕРИ:НАЧАЛО (генерирано от tools/sync_examples.py - не редактирай ръчно) -->

## Примерни програми

Кодът е в [`examples/02-lists-and-for-loop/`](./examples/02-lists-and-for-loop/) — пусни го с `python3 examples/02-lists-and-for-loop/<име>.py`.
Виж го ред по ред, с променливите и изхода на всяка стъпка, във [визуализатора](./visualizer.html).

### 1. Статистика за оценки
*обхождане на списък с for*

```python
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
```

Изход:
```
Оценки: [4, 6, 3, 5, 6, 2]
Сума: 26
Средно: 4.333333333333333
Най-висока: 6
```

### 2. range със стъпка и continue
*квадрати на числата*

```python
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
```

Изход:
```
Квадрати на четните: [4, 16, 36, 64, 100]
Стъпка 5: 0
Стъпка 5: 5
Стъпка 5: 10
Стъпка 5: 15
Стъпка 5: 20
Обратно с отрицателна стъпка:
3
2
1
```

### 3. Присъствия
*добавяне, премахване и търсене с break*

```python
# Присъствия - добавяне, премахване и търсене с break
present = ["Petar", "Ivan", "Ogi", "Nasko"]

present.append("Boyan")       # идва още един ученик
print("След append:", present)

present.remove("Ogi")         # премахване по стойност
print("След remove:", present)

first = present.pop(0)        # pop по индекс - връща премахнатия елемент
print("Излезе:", first, "->", present)

searched = "Nasko"
found_at = -1

for index in range(len(present)):
    print("Проверявам индекс", index)
    if present[index] == searched:
        found_at = index
        break                 # намерихме го, няма смисъл да търсим нататък

print(searched, "е на позиция", found_at)
print("Последният в списъка е", present[-1])
```

Изход:
```
След append: ['Petar', 'Ivan', 'Ogi', 'Nasko', 'Boyan']
След remove: ['Petar', 'Ivan', 'Nasko', 'Boyan']
Излезе: Petar -> ['Ivan', 'Nasko', 'Boyan']
Проверявам индекс 0
Проверявам индекс 1
Nasko е на позиция 1
Последният в списъка е Boyan
```

<!-- ПРИМЕРИ:КРАЙ -->
