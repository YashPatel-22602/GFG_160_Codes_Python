# Input : P = 10000
#         R = 5
#         T = 5
# Output :2500.0
# We need to find simple interest on
# Rs. 10,000 at the rate of 5% for 5
# units of time.

p = int(input("Enter the Principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time period: "))

si = (p * r * t)/100
print("The Simple Interest is: ",si)