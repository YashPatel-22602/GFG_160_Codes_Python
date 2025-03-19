a = [123, 456, 789]
res = []

for i in a:
    total = 0
    while i > 0:
        total += i % 10
        i = i // 10
    res.append(total)


print(res)