# Високосна година - логически операции and / or / not
year = 2024

divisible_by_4 = year % 4 == 0        # % дава остатък, == сравнява
divisible_by_100 = year % 100 == 0
divisible_by_400 = year % 400 == 0

print(divisible_by_4, divisible_by_100, divisible_by_400)

# Високосна е, ако се дели на 4 и НЕ се дели на 100, ИЛИ се дели на 400
is_leap = (divisible_by_4 and not divisible_by_100) or divisible_by_400
print("Високосна:", is_leap)

if is_leap:
    days = 366
else:
    days = 365

print(year, "има", days, "дни")
