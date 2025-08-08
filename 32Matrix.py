# matrix in python 

from numpy import * ;


arr1 =  array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# to get the size of the array 
print(arr1.size)
# to get the shape of the array
print(arr1.shape)
    
# convert 3D array to 1D array
arr2 = arr1.flatten()
print(arr2)
# to get the size of the array