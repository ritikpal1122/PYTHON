from numpy import *

# Create a 1D array
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([1, 2, 3, 4, 5],int) # Specify the data type as int
arr3 = array([1, 2, 3, 4, 5],float) # Specify the data type as float
arr4 = array([1, 2, 3, 4, 5],complex) # Specify the data type as complex
arr5 = array([1, 2, 3, 4, 5],bool) # Specify the data type as bool
print("1D Array: ", arr1)
print("1D Array with int type: ", arr2)
print("1D Array with float type: ", arr3)
print("1D Array with complex type: ", arr4)
print("1D Array with bool type: ", arr5) 


# using metthod linspace to create an array with evenly spaced values

arr = linspace(0, 10, 5) # Start at 0, end at 10, with 5 evenly spaced values
print("Array with evenly spaced values: ", arr) 

# use zeros method 
arr_zeros = zeros(5) # Create an array of 5 zeros
print("Array of zeros: ", arr_zeros)
# use ones method
arr_ones = ones(5) # Create an array of 5 ones
print("Array of ones: ", arr_ones)