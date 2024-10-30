import numpy as np 

# 1-D
np1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)

# 2-D
np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(np2)
print(np2.shape)

# Reshape
np4=np1.reshape(3,4)
print(np4)
print(np4.shape)

# 3-D
np3=np.array([[[1,2,3,4,5],[6,7,8,9,0],[10,11,12,13,14]]])
print(np3)
print(np3.shape)

# Flatten 1-D
np5=np3.reshape(-1)
print(np5)
print(np5.shape)