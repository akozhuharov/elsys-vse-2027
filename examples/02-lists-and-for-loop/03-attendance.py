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
