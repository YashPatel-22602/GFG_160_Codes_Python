list1 = list()
n = int(input("Enter the Size of an List: "))
for i in range(0,n):
    list1.append(int(input(f"Enter the Element {i}: ")))

list1[0],list1[n-1] = list1[n-1],list1[0]

print(list1)