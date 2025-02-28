n = int(input("Enter the Number: "))
a,b = 0,1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while b < n:
        a,b = b,a+b

if b != n:
    print("The Given Number is not an fibonacci Number")
else:
    print(f"The Given Number is an Fibonacci Number")
