a = [1, 2, 3, 1, 2, 4, 5, 6, 5]

s = set()
d = []
for i in a:
    if i in s:
        d.append(i)
    else:
        s.add(i)
print(d)