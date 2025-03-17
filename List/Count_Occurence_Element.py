a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

n = int(input("Enter the Number to be find: "))
count = 0
for i in a:
    if i == n:
        count += 1

if count == 0:
    print("Number not Found")
else:
    print(f"The Number has Occured {count} times")