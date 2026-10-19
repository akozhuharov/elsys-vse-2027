# Съветник за облекло - типове данни, математика и if/elif/else
temperature = 12.5          # float - температура в градуси
is_raining = True           # bool - дали вали
city = "Sofia"              # str - име на града

feels_like = temperature - 3     # вятърът "отнема" 3 градуса
print(city, "- усеща се като", feels_like)

if feels_like < 0:
    print("Зимно яке и шапка")
elif feels_like < 15:
    print("Яке")
else:
    print("Тениска")

if is_raining:
    print("Вземи чадър!")
