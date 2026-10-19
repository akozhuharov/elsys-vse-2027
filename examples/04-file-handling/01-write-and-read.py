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
