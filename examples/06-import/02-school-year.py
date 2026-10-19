# Броене на дни - модул datetime
from datetime import date, timedelta    # включваме само нужните класове

today = date(2026, 10, 19)       # за истинската дата: date.today()
end_of_year = date(2027, 6, 30)

left = end_of_year - today               # разликата е timedelta обект
print("Остават дни до края:", left.days)
print("Остават седмици:", left.days // 7)

print("Днес е ден", today.day, "от месец", today.month)

next_week = today + timedelta(days=7)    # добавяме време
print("След седмица:", next_week)

if today.weekday() < 5:                  # 0 = понеделник, 6 = неделя
    print("Работен ден е")
else:
    print("Почивен ден е")
