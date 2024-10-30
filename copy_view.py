import numpy as np 

np1 = np.array([1,2,3,4,5,6,7,8,9])

# print(np1)
'''
np2 = np1.view()
print(f'Origianl NP1 {np1}')
print(f'Origianl NP2 {np2}')

np1[0] = 41
print(f'Changed NP1 {np1}')
print(f'Origianl NP2 {np2}')
'''
# Create a copy
np2 = np1.copy()
print(f'Origianl NP1 {np1}')
print(f'Origianl NP2 {np2}')

np2[0] = 41
print(f'Changed NP1 {np1}')
print(f'Origianl NP2 {np2}')


