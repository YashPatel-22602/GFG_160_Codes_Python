# A = P(1 + R/100) t
# Compound Interest = A – P

# Where,
# A is amount
# P is the principal amount
# R is the rate and
# T is the time span


# Input:
# Enter the principal amount: 3000
# Enter rate of interest: 5
# Enter time in years: 3
# Output:
# Compound interest is 472.875


p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time duration: "))

# Using the Power Function
# a = (pow((1 + r/100), t))
# ci = (a - p)
# print("Compound Interest: ", "%.2f" % ci)


# Using the for loop

a =p
for i in range(t):
    a = a * (1 + r/100)
ci = a - p
print("Compound Interest: ", "%.2f" % ci)
