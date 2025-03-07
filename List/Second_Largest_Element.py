list1 = list()
n = int(input("Enter the Size of an List: "))
for i in range(0,n):
    list1.append(int(input(f"Enter the Element {i}: ")))

first = list1[0]
second = 0
for i in list1:
    if i < first and i > second:
        second = i
    elif i > first:
        first = i

print(f"The Second Largest Element in the List is {second}")