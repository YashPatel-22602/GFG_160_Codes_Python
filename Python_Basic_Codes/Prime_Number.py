n = int(input("Enter the Number: "))
if n < 2:
    print("Enter the Number Greater than 1")
else:
    count = 0
    for i in range(2,int(n*0.5) + 1):
        if n % i == 0:
            count += 1
    if count == 0:
        print("The Number Entered is an Prime Number")
    else:
        print("The Number Entered is not an Prime Number")
