import numpy as np 

# Slicing 
np1 = np.array([1,2,3,4,5,6,7,8,9])

print(np1[1:5])

print(np1[3:])

print(np1[-3:-1])

print(np1[1:5])

print(np1[1:5:2])

print(np1[::2])
print(np1[::3])

np2=np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(np2[1,2])
print(np2[0:1, 1:3])
print(np2[0:2, 1:3])
