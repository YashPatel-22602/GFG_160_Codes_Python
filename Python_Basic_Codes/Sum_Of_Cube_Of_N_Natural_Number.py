# Input: n = 5
# Output: 225
# Explanation:  13 + 23 + 33 + 43 + 53 = 225

n = int(input("Enter the Number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i*i*i
    i += 1
print(sum)

# Method 2
sum1 = 0
for i in range(1,n+1):
    sum1 = sum1 + i**3

print(sum1)

# Method 3
print(((n * (n + 1)) // 2) ** 2)
