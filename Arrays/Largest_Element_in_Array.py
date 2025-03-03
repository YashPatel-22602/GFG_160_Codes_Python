# Input : arr[] = {10, 20, 4}
# Output : 20
# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100

arr = []
n = int(input("Enter the Number for the Size of Array: "))
for i in range(0,n):
    arr.append(int(input(f"Enter the Element {i}: ")))


largest = 0
for i in arr:
    if largest < i:
        largest = i

print(largest)


max1 = max(arr)