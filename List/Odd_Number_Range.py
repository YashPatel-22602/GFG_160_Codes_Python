list1 = list()
s = int(input("Enter the Start Number for the Range: "))
e = int(input("Enter the End Number for the Range: "))

try:
    for i in range(s, e+1):
        list1.append(i)

    list2 = list()
    for j in range(0,len(list1)):
        if list1[j] % 2 != 0:   # Check if the number is even
            list2.append(list1[j])

    print(f"The List of all the Odd Numbers in the list is: {list2}")

except ValueError:
    print("Invalid input! Please enter only integer values.")
except IndexError:
    print("Index error occurred! Please check your loop logic.")