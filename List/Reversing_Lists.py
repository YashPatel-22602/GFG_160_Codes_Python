list1 = list()
n = int(input("Enter the Size of an List: "))
for i in range(0,n):
    list1.append(int(input(f"Enter the Element {i}: ")))

#Method 1
list1.reverse()
print(list1)

#Method 2
print(list1[:])