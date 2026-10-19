# Броене на думи - dictionary като ключ -> стойност
text = "cat dog cat bird dog cat"
words = text.split()          # split разделя низа по интервалите в списък
print("Думи:", words)

counts = {}                   # празен dictionary

for word in words:
    if word in counts:        # in проверява дали ключът съществува
        counts[word] += 1
    else:
        counts[word] = 1
    print(word, "->", counts)

print("Резултат:", counts)

for key, value in counts.items():    # items връща двойка ключ, стойност
    print(key, "се среща", value, "пъти")

print("Само стойностите:", list(counts.values()))
