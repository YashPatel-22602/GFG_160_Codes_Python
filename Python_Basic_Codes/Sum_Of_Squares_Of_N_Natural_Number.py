# Input : N = 4
# Output : 30
# 12 + 22 + 32 + 42
# = 1 + 4 + 9 + 16
# = 30
#
# Input : N = 5
# Output : 55

n = int(input("Enter the Number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i*i
    i += 1
print(sum)

# Method 2
sum1 = 0
for i in range(1,n+1):
    sum1 = sum1 + i**2

print(sum1)

# Method 3
print(n * (n + 1) * (2 * n + 1) // 6)
