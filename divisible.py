num = [0, 2, 3, 35, 33, 49, 25, 42, 48, 54, 60]

result = []

for i in num:
    if (i % 7 == 0) and (i % 5 != 0):
        result.append(i)

print(result)
