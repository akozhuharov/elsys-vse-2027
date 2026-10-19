# Библиотеки/модул
В python има голям брой включени в езика библиотеки, които могат да бъдат ползвани и също така публично достъпни за инсталация чрез инструмента pip

## Включване в текущата програма
Ако искате да използвате функции/класове от друг модул става по следният начин:
```python
import math # Включва се целият модул
print(math.sqrt(4))  # Функцията се извиква с името на модула преди името на функцията



from math import sqrt  # Включва се само функцията
print(sqrt(4))  # Може да се извика директно с нейното име
```

Примерни полезни библиотеки вградени в езика:
* math - математичски функции
* os - интерфейс към операционната систем
* email - работа и изпращане на имейли
* datetime - работа с време(години/месеци/дни/часове)
* zipfile - работа с архиви

Пълен списък може да намерите тук:
[Python standard library](https://docs.python.org/3/library/index.html)  

Публични модули може да намерите тук:  
[PYPI](https://pypi.org/)

<!-- ПРИМЕРИ:НАЧАЛО (генерирано от tools/sync_examples.py - не редактирай ръчно) -->

## Примерни програми

Кодът е в [`examples/06-import/`](./examples/06-import/) — пусни го с `python3 examples/06-import/<име>.py`.
Виж го ред по ред, с променливите и изхода на всяка стъпка, във [визуализатора](./visualizer.html).

### 1. Квадратно уравнение
*math.sqrt*

```python
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
```

Изход:
```
D = 1
x1 = 3.0
x2 = 2.0
Закръгляне нагоре: 3
Пи: 3.1416
```

### 2. Броене на дни
*модул datetime*

```python
# Броене на дни - модул datetime
from datetime import date, timedelta    # включваме само нужните класове

today = date(2026, 10, 19)       # за истинската дата: date.today()
end_of_year = date(2027, 6, 30)

left = end_of_year - today               # разликата е timedelta обект
print("Остават дни до края:", left.days)
print("Остават седмици:", left.days // 7)

print("Днес е ден", today.day, "от месец", today.month)

next_week = today + timedelta(days=7)    # добавяме време
print("След седмица:", next_week)

if today.weekday() < 5:                  # 0 = понеделник, 6 = неделя
    print("Работен ден е")
else:
    print("Почивен ден е")
```

Изход:
```
Остават дни до края: 254
Остават седмици: 36
Днес е ден 19 от месец 10
След седмица: 2026-10-26
Работен ден е
```

### 3. Хвърляне на зар
*модули random и os*

```python
# Хвърляне на зар - модули random и os
import random
import os

random.seed(42)              # seed прави резултата еднакъв при всяко пускане

rolls = []
for i in range(6):
    rolls.append(random.randint(1, 6))   # случайно цяло число от 1 до 6

print("Хвърляния:", rolls)

sixes = 0
for roll in rolls:
    if roll == 6:
        sixes += 1

print("Шестици:", sixes)
print("Случаен ученик:", random.choice(["Petar", "Ivan", "Ogi"]))
print("Текуща папка:", os.path.basename(os.getcwd()))
```

Изход:
```
Хвърляния: [6, 1, 1, 6, 3, 2]
Шестици: 2
Случаен ученик: Petar
Текуща папка: programa
```

<!-- ПРИМЕРИ:КРАЙ -->
