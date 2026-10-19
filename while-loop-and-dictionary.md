# While loop
Синтаксисът не е като for цикъла, като тук имаме условие, което трябва да се отъждествява на вярно, за да се изпълни кода на цикъла:
```python
a = 0
while a < 5:
    print(a)
    a += 1 # кратка форма на a = a + 1
```

Останалите елементи като `break` и `continue` са налични и за този цикъл.  

> [!ВАЖНО]
> В while цикъл сами се грижим условието да бъде изпълнено и е много лесно да оставим цикъла да стане вечен

# Dictionary
Структура от данни, която е от типа ключ стойност
```python
d = {"name": "Atanas", "age": 76, "city": "Sofia"} # дефиницията става с къдрави скоби, ключовете обикновенно са string-ове, но може и да са числа(ако трябва да са числа е по-добре да се ползва list)

# Достъп до елементи става като при списък
d["name"]  # "Atanas"
d["age"]  # 76

# Обхождане - тук key ще приема ключовете
for key in d:
    print(key, d[key]) # Трябва да достъпим стойността с текущия ключ в променливата key
# "name" "Atanas"
# "age" 76
# "city" "Sofia"

# Функция на dictionary values - връща директно стойностите, ако не ни трябва ключовете
for value in d.values():
    print(value)

# "Atanas"
# 76
# "Sofia

# Функция items - връща двойка от ключ и стойност
for key, value in items:
    print(key, value)
# "name" "Atanas"
# "age" 76
# "city" "Sofia"

# Премахване на елемент по ключ
d.pop("name")

# Премахване на последният ключ и стойност
d.popitem()
```

<!-- ПРИМЕРИ:НАЧАЛО (генерирано от tools/sync_examples.py - не редактирай ръчно) -->

## Примерни програми

Кодът е в [`examples/03-while-loop-and-dictionary/`](./examples/03-while-loop-and-dictionary/) — пусни го с `python3 examples/03-while-loop-and-dictionary/<име>.py`.
Виж го ред по ред, с променливите и изхода на всяка стъпка, във [визуализатора](./visualizer.html).

### 1. Сума на цифрите на число
*класически while цикъл*

```python
# Сума на цифрите на число - класически while цикъл
number = 4729
rest = number
digit_sum = 0
count = 0

while rest > 0:
    digit = rest % 10      # последната цифра
    rest = rest // 10      # // е целочислено деление - маха последната цифра
    digit_sum += digit
    count += 1
    print("цифра:", digit, "остава:", rest)

print("Числото", number, "има", count, "цифри")
print("Сума на цифрите:", digit_sum)
```

Изход:
```
цифра: 9 остава: 472
цифра: 2 остава: 47
цифра: 7 остава: 4
цифра: 4 остава: 0
Числото 4729 има 4 цифри
Сума на цифрите: 22
```

### 2. Броене на думи
*dictionary като ключ -> стойност*

```python
# Броене на думи - dictionary като ключ -> стойност
text = "cat dog cat bird dog cat"
words = text.split()          # split разделя низа по интервалите в списък
print("Думи:", words)

counts = {}                   # празен dictionary

for word in words:
    if word in counts:        # in проверява дали ключът съществува
        counts[word] += 1
    else:
        counts[word] = 1
    print(word, "->", counts)

print("Резултат:", counts)

for key, value in counts.items():    # items връща двойка ключ, стойност
    print(key, "се среща", value, "пъти")

print("Само стойностите:", list(counts.values()))
```

Изход:
```
Думи: ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']
cat -> {'cat': 1}
dog -> {'cat': 1, 'dog': 1}
cat -> {'cat': 2, 'dog': 1}
bird -> {'cat': 2, 'dog': 1, 'bird': 1}
dog -> {'cat': 2, 'dog': 2, 'bird': 1}
cat -> {'cat': 3, 'dog': 2, 'bird': 1}
Резултат: {'cat': 3, 'dog': 2, 'bird': 1}
cat се среща 3 пъти
dog се среща 2 пъти
bird се среща 1 пъти
Само стойностите: [3, 2, 1]
```

### 3. Телефонен указател
*обработка на команди с while, break и continue*

```python
# Телефонен указател - обработка на команди с while, break и continue
phonebook = {"Ivan": "0888123456", "Mira": "0899777888"}
commands = ["get Ivan", "add Ogi 0877000111", "get Ogi", "del Mira", "bad", "stop", "get Ivan"]

i = 0
while i < len(commands):
    command = commands[i]
    i += 1
    parts = command.split()
    action = parts[0]

    if action == "stop":
        print("Край на работата")
        break                         # излизаме напълно от цикъла

    if action == "get":
        print(parts[1], "->", phonebook.get(parts[1], "няма такъв"))
    elif action == "add":
        phonebook[parts[1]] = parts[2]
        print("Добавен:", parts[1])
    elif action == "del":
        removed = phonebook.pop(parts[1])
        print("Изтрит:", parts[1], removed)
    else:
        print("Непозната команда:", action)
        continue                      # връщаме се на началото на цикъла

    print("  указател:", phonebook)

print("Финален указател:", phonebook)
```

Изход:
```
Ivan -> 0888123456
  указател: {'Ivan': '0888123456', 'Mira': '0899777888'}
Добавен: Ogi
  указател: {'Ivan': '0888123456', 'Mira': '0899777888', 'Ogi': '0877000111'}
Ogi -> 0877000111
  указател: {'Ivan': '0888123456', 'Mira': '0899777888', 'Ogi': '0877000111'}
Изтрит: Mira 0899777888
  указател: {'Ivan': '0888123456', 'Ogi': '0877000111'}
Непозната команда: bad
Край на работата
Финален указател: {'Ivan': '0888123456', 'Ogi': '0877000111'}
```

<!-- ПРИМЕРИ:КРАЙ -->
