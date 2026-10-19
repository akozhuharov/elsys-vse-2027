# Профил с **kwargs - и функция, която вика друга функция
def initials(full_name):
    parts = full_name.split()
    letters = ""
    for part in parts:
        letters += part[0]        # първата буква на всяка дума
    return letters


def profile(full_name, **kwargs):
    print("Име:", full_name)
    print("Инициали:", initials(full_name))   # извикваме другата функция
    for key, value in kwargs.items():
        print(" ", key, "=", value)
    return len(kwargs)


count = profile("Atanas Kozhuharov", city="Sofia", age=16, grade=9)
print("Допълнителни полета:", count)

profile("Ivan Ivanov")            # kwargs може да е празен
