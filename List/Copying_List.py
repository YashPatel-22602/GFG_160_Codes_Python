a = [1,2,3,4,5]

#Method 1
b = a.copy()
print(b)

#Method 2
c = list()
for i in a:
    c.append(i)

print(c)

#Method 3
d = a[:]
print(d)

#Method 4
e = list(a)
print(e)