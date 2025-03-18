import numpy as np

l = [1, 2, 3, 4]

#Method 1 :-  Using For Loop

sum1 = []

for i in range(0,len(l)):
    if i == 0:
        sum1.append(l[i])
    else:
        sum1.append(l[i] + sum1[i-1])

print(sum1)


#Method 2  :- Using Numpy
cumulative_sum = np.cumsum(l)

print(cumulative_sum)