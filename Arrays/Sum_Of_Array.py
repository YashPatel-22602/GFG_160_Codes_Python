# Input : arr[] = {1, 2, 3}
# Output : 6
# Explanation: 1 + 2 + 3 = 6

arr = []
n = int(input("Enter the Number for the Size of Array: "))
for i in range(0,n):
    arr.append(int(input(f"Enter the Element {i}: ")))

sum = 0
for j in arr:
    sum += j

print("The Sum of Array is: ",sum)