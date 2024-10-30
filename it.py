import numpy as np
'''
np1 = np.array([1,2,3,4,5])
for x in np1:
    print(x)

np2 = np.array([[1,2,3,4,5],[6,7,8,9,0]])
for x in np2:
    #print(x)
    for y in x:
        print(y)
        
np3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for x in np3:
    for y in x:
        for z in y:
            print(z)
            '''
            
# use np.nditer()

np3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for x in np.nditer(np3):
    print(x)