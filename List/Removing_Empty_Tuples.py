a = [(1, 2), (), (3, 4), (), (5,)]


#Method 1 :- Using List Comprehension
res = [t for t in a if t]
print(res)


#Method 2  :- Using Filter
res1 = list(filter(None,a))
print(res1)


#Method 3  :- Using for Loop
res2 = []
for s in a:
    if s:
        res2.append(s)
print(res2)