try:
    list1 = list()
    n = int(input("Enter the Size of a List: "))

    for i in range(0, n):
        list1.append(int(input(f"Enter the Element {i+1}: ")))

    list2 = list()
    for j in list1:
        if j < 0:
            list2.append(j)

    print(list2)

except Exception:
    print("Something Error Occured")