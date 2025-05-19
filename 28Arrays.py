# array in python 
# array is a data structure that can hold multiple values of the same type
# it is a collection of items stored at contiguous memory locations
# it is used to store multiple values in a single variable
# it is used to store data of same type
# it is used to store data of different types
# it can be expanded or shrunk as needed

#type code for array 
# array('typecode', [values])
# b - signed char
# B - unsigned char
# u - unicode character
# h - signed short
# H - unsigned short
# i - signed int
# I - unsigned int
# l - signed long
# L - unsigned long
# q - signed long long
# Q - unsigned long long
# f - float
# d - double
from array import *
val = array('i', [1, 2, 3, 4, 5])
val[0] = 10 # change the first element to 10
val.reverse()
val.append( 6) # append 6 to the array


print(val)

for i in val:
    print(i, end=" ")
print()

newArr = array(val.typecode, (a*2 for a in val))
print(newArr)