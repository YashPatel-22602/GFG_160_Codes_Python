# Area = pi * r2
# For example, if r = 5, the area is calculated as Area = 3.14159 × 5² = 78.53975.
import math

import numpy

r = int(input("Enter the Radius: "))

# using standard pi value
# pi = 3.14
# area = pi * r * r
# print("The Area of the Circle is: ",area)

# Using math.pi
# math module provides the constant math.pi, representing the value of π (pi) with high precision.
# area = math.pi * (r ** 2)
# print("The Area of the Circle is: ","%.2f"%area)


# Using math.pow()
# math.pow() function is optimized for power calculations, making it more readable when dealing with complex exponents.

# area = math.pi * (pow(r,2))
# print("The Area of the Circle is: ","%.2f"%area)


# Using numpy.pi
# numpy library is designed for high-performance numerical computations and numpy.pi provides a precise value of π.

area = numpy.pi * (r ** 2)
print("The Area of the Circle is: ","%.2f"%area)
