# Работа с файлове
Има два синтаксиса за работа с файлове. И в двата използваме функцията open, за да получим обект с който да работим с файла
## Функция open
Два параметъра, за които трябва да използваме:
* Име на файла на първа позиция
* Режим на четене - те биват r(ead), w(rite), a(ppend), r+(read+write), a+(append + read), w+(write + read)

> [!IMPORTANT]  
> Трябва да се внимава, в коя папка се намира файлът, който отваряме. Ако не е в папката на програмата е добре като параметър да се подаде целият път до файла - "C:\Users\elsyser\Desktop\test.txt"


## С with
```python
with open("test.txt", "r") as f:
    lines = f.readlines()
```

## С присвояване на променлива
```python
f = open("test.txt", "r") 
lines = f.readlines()
f.close() # Не трябва да се забравя затварянето
```

<!-- ПРИМЕРИ:НАЧАЛО (генерирано от tools/sync_examples.py - не редактирай ръчно) -->

## Примерни програми

Кодът е в [`examples/04-file-handling/`](./examples/04-file-handling/) — пусни го с `python3 examples/04-file-handling/<име>.py`.
Виж го ред по ред, с променливите и изхода на всяка стъпка, във [визуализатора](./visualizer.html).

> [!IMPORTANT]
> Трите програми създават файловете си в папката, от която ги пускаш.


### 1. Записване и прочитане на файл
*режими "w" и "r"*

```python
# Записване и прочитане на файл - режими "w" и "r"
with open("students.txt", "w") as f:       # "w" създава нов (или изтрива стария!)
    f.write("Petar\n")                    # \n е нов ред
    f.write("Ivan\n")
    f.write("Ogi\n")

print("Файлът е записан")

with open("students.txt", "r") as f:       # "r" само чете
    lines = f.readlines()                 # списък от редовете, с \n в края

print("Прочетени редове:", lines)

for line in lines:
    print("Ученик:", line.strip())        # strip маха \n и празните символи
```

Изход:
```
Файлът е записан
Прочетени редове: ['Petar\n', 'Ivan\n', 'Ogi\n']
Ученик: Petar
Ученик: Ivan
Ученик: Ogi
```

### 2. Дневник
*режим "a" (append) добавя, без да трие*

```python
# Дневник - режим "a" (append) добавя, без да трие
events = ["влизане", "решена задача", "излизане"]

for event in events:
    with open("log.txt", "a") as f:       # "a" пише в края на файла
        f.write(event + "\n")
    print("Записано:", event)

with open("log.txt", "r") as f:
    content = f.read()                    # read връща целия файл като един низ

print("Съдържание:")
print(content)
print("Брой редове:", len(content.splitlines()))
```

Изход:
```
Записано: влизане
Записано: решена задача
Записано: излизане
Съдържание:
влизане
решена задача
излизане

Брой редове: 3
```

### 3. Отчет от файл
*четене, обработка и записване на резултата*

```python
# Отчет от файл - четене, обработка и записване на резултата
f = open("grades.txt", "w")               # без with - сами затваряме
f.write("Petar 5\nIvan 3\nOgi 6\n")
f.close()                                 # затварянето е задължително!

f = open("grades.txt", "r")
lines = f.readlines()
f.close()

total = 0
report = []

for line in lines:
    name, grade = line.split()            # split прави списък ["Petar", "5"]
    grade = int(grade)                    # от файл всичко идва като str!
    total += grade
    report.append(name + ": " + str(grade))
    print("обработен:", name, grade)

average = total / len(lines)
report.append("Средно: " + str(average))

with open("report.txt", "w") as out:
    for row in report:
        out.write(row + "\n")

print("Отчетът е готов, средно:", average)
```

Изход:
```
обработен: Petar 5
обработен: Ivan 3
обработен: Ogi 6
Отчетът е готов, средно: 4.666666666666667
```

<!-- ПРИМЕРИ:КРАЙ -->
