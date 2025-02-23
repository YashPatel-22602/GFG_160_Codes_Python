# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153
#
# Input : 120
# Output : No
# 120 is not a Armstrong number.
# 1*1*1 + 2*2*2 + 0*0*0 = 9
import math

# n = str(input("Enter the Number: "))

# using the for loop
# res = 0
# for i in n:
#     res += int(i) ** len(n)

# if int(n) == res:
#     print("The Number Entered is an Amstrong Number")
# else:
#     print("The Number Entered is not an Amstrong Number")

# Using the remainder and division

n = int(input("Enter the Number: "))

num = n
numDigits = 0
sum = 0

# Find number of digits in num
while n > 0:
    n //= 10
    numDigits += 1

n = num

# Calculate sum of digits raised to the power of numDigits
while n > 0:
    digit = n % 10
    sum += math.pow(digit, numDigits)
    n //= 10

if sum == num:
    print("The Number Entered is an Amstrong Number")
else:
    print("The Number Entered is not an Amstrong Number")