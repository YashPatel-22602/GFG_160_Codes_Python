list1 = list()
n = int(input("Enter the Size of a List: "))

try:
    for i in range(0, n):
        list1.append(int(input(f"Enter the Element {i+1}: ")))

    list2 = list()
    for j in list1:
        if j % 2 != 0:   # Check if the number is odd
            list2.append(j)

    print(f"The List of all the Odd Numbers in the list is: {list2}")

except ValueError:
    print("Invalid input! Please enter only integer values.")
except IndexError:
    print("Index error occurred! Please check your loop logic.")