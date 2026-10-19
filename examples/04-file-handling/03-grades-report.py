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
