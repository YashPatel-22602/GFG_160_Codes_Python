list1 = list()
n = int(input("Enter the Size of an List: "))
for i in range(0,n):
    list1.append(int(input(f"Enter the Element {i}: ")))

biggest = list1[0]
for i in list1:
    if i > biggest:
        biggest = i

print(f"The Smallest Number in the List is {biggest}")