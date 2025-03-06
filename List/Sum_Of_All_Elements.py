list1 = list()
n = int(input("Enter the Size of an List: "))
for i in range(0,n):
    list1.append(int(input(f"Enter the Element {i}: ")))

sum = 0
for x in list1:
    sum += x

print(f"The Sum of Element of List is: {sum}")