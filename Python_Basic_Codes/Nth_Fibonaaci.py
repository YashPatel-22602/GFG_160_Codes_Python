n = int(input("Enter the Number: "))
term = 1
a,b = 0,1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while b < n:
        a,b = b,a+b
        term += 1

if b != n:
    print("The Given Number is not an fibonacci Series")
else:
    print(f"The Given Number is {term} Term")