# Статистика с *args - неограничен брой позиционни аргументи
def stats(*args):
    if len(args) == 0:
        return 0, 0, 0            # функция може да върне няколко стойности
    total = 0
    biggest = args[0]
    for number in args:
        total += number
        if number > biggest:
            biggest = number
    return total, total / len(args), biggest


s, avg, mx = stats(5, 6, 9, 1)    # разпакетваме трите върнати стойности
print("сума:", s, "средно:", avg, "макс:", mx)

print(stats(10))
print(stats())
