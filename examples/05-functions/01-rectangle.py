# Площ на правоъгълник - задължителни аргументи и стойност по подразбиране
def area(width, height):          # и двата аргумента са задължителни
    return width * height


def describe(name, unit="кв.м"):  # unit има стойност по подразбиране
    return name + " " + unit


a = area(4, 5)
print("Площ:", a)

b = area(height=2, width=10)      # с имена редът няма значение
print("Площ:", b)

print(describe("20"))             # unit не е подаден -> "кв.м"
print(describe("20", "кв.км"))    # тук подаваме свой unit
