list1 = list()
s = int(input("Enter the Start Number for the Range: "))
e = int(input("Enter the End Number for the Range: "))

try:
    for i in range(s, e+1):
        list1.append(i)


    list2 = list()
    for j in list1:
        if j > 0:
            list2.append(j)

    print(list2)

except Exception:
    print("Something Error Occured")