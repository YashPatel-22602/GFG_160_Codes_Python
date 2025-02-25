# Sample input = 2,7

a = int(input("Enter the Start Number: "))
b = int(input("Emter the End Number: "))

li = []

if a < 2 or b < 2:
    print("Enter a Valid Number")
else:
    for i in range(a,b+1):
        count = 0
        for j in range(2,i):
            if i % j == 0:
                count += 1
        if count == 0:
            li.append(i)
print(li)