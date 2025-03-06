list1 = list()
n = int(input("Enter the Size of an List: "))
for i in range(0,n):
    list1.append(int(input(f"Enter the Element {i}: ")))

res = 1
for x in list1:
    res *= x

print(f"The Multiply of Element of List is: {res}")