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
