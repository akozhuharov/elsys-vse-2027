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
