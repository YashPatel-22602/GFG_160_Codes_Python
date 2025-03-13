try:
    a = [[1, 2], [], [3, 4], [], [5]]
    for b in a:
        if len(b) == 0:
            a.remove(b)

    print(a)
except Exception:
    print("Something error Occured")