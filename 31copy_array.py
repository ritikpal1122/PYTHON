# Copy of Array into another array
from numpy import *

arr1 = array([1, 2, 3, 4, 5])
arr2  = array([6, 7, 8, 9, 10])
# add arr1 and arr2
arr3 = arr1 + arr2
print(arr3)


# we can perform sin cos and tan operations on the array
# other Operations 
# sum 
# mean
# max
# min
# std
# var
print("Sum of arr1: ", sum(arr1))
print("Mean of arr1: ", mean(arr1))
print("Max of arr1: ", max(arr1))
print("Min of arr1: ", min(arr1))
print("Standard Deviation of arr1: ", std(arr1))
print("Variance of arr1: ", var(arr1))
# we can perform mathematical operations on the array
print("Sine of arr1: ", sin(arr1))
print("Cosine of arr1: ", cos(arr1))
print("Tangent of arr1: ", tan(arr1))
# we can perform logical operations on the array
print("Logical AND of arr1 and arr2: ", logical_and(arr1, arr2))
print("Logical OR of arr1 and arr2: ", logical_or(arr1, arr2))
# we can perform comparison operations on the array
print("Comparison of arr1 and arr2: ", arr1 > arr2)
# we can perform bitwise operations on the array    
print("Bitwise AND of arr1 and arr2: ", bitwise_and(arr1, arr2))
print("Bitwise OR of arr1 and arr2: ", bitwise_or(arr1, arr2))
# we can perform arithmetic operations on the array

# concatenate two arrays
arr4 = concatenate((arr1, arr2))
print("Concatenated Array: ", arr4)
# stack two arrays vertically
arr5 = vstack((arr1, arr2))
print("Vertically Stacked Array: ")
print(arr5)
# stack two arrays horizontally
arr6 = hstack((arr1, arr2))
print("Horizontally Stacked Array: ")
print(arr6)
# copy an array

arr3  = arr1
print("Copied Array: ")
print(arr3)

print("Original Array: ")
print(id(arr1) , id(arr3))  # Check if both arrays point to the same memory location

