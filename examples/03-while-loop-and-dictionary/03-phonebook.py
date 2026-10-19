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
