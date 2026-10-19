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
