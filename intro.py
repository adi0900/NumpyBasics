import numpy as np

list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1[0])
list2 = ["John", '41', 1, 2, 3, 4, 5 , True]
print(list2)

#Numpy - Numerical Python
# ndarray - N-dimensional array

np1 = np.array([1, 2, 3, 4, 5])
print(np1)
print(np1[0])
print(np1.shape)

# Range
np2 = np.arange(10)
print(np2)

# step
np3 = np.arange(0, 10, 2)
print(np3)

# zeros
np4 = np.zeros(10)
print(np4)

# multiple dimensions 
np5 = np.zeros((2,10))
print(np5)

#Full
np6 = np.full((10), 6)
print(np6)

# Multiple dimensions Full
np7 = np.full((2,10), 6)
print(np7)

# python to numpy
df = [1, 2, 3, 4, 5]
np8 = np.array(df)
print(np8)

print(np8[0])

