list1 = list()
n = int(input("Enter the Size of an List: "))
for i in range(0,n):
    list1.append(int(input(f"Enter the Element {i}: ")))

smallest = list1[0]
for i in list1:
    if i < smallest:
        smallest = i

print(f"The Smallest Number in the List is {smallest}")