# Input: k = 2, n = 3
# Output: 9, 3rd multiple of 2 in Fibonacci Series is 34 that appears at position 9.
#
# Input: k = 4, n = 5
# Output: 30, 5th multiple of 4 in Fibonacci Series is 832040 which appears at position 30.




k = int(input("Enter the Number: "))
n = int(input("Ener the Number of Multiple: "))
a,b = 0 ,1
multiple = 0
term = 0
while multiple < n:
    a,b = b,a+b
    term += 1
    if b % k == 0:
        multiple += 1

print(f"{n} multiple of {k} in Fibonacci Series is {b} that appears at position {term + 1}.")
print(term + 1)