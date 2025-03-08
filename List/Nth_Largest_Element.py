# Input : [4, 5, 1, 2, 9]
#         N = 2
# Output :  [9, 5]
#
# Input : [81, 52, 45, 10, 3, 2, 96]
#         N = 3
# Output : [81, 96, 52]


list1 = list()
k = int(input("Enter the No Of Elements you want: "))
n = int(input("Enter the Size of a List: "))

for i in range(0, n):
    list1.append(int(input(f"Enter the Element {i}: ")))

# Initialize list2 with minimum possible values
list2 = [float('-inf')] * k

# Logic to find top k elements
for a in list1:
    for b in range(0, k):
        if a > list2[b]:
            list2.insert(b, a)  # Insert the new element at the correct position
            list2.pop()         # Remove the last element to maintain the size
            break

print(list2)
