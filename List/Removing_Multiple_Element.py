def removingElement(list1,num):
    list1.remove(num)
    return list1

try:
    list1 = list()
    s = int(input("Enter the Size of a List: "))

    for i in range(0, s):
        list1.append(int(input(f"Enter the Element {i+1}: ")))

    n = 1
    while n != 2:
        print("Press 1 for Removing Element")
        print("Press 2 for Exit")
        n = int(input("Enter the Menu Number: "))
        if n == 1:
            num = int(input("Enter the Number to removed:"))
            res = removingElement(list1,num)
            print(list1)
        elif n == 2:
            print("Thank you for using \U0001f600")
        else:
            print("Enter the Valid Input")

except Exception:
    print("Something Error Occurred")