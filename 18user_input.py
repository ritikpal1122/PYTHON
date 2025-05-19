import sys
# input fun this will you the value in str format always by default
# if we want to convert it into int or float we have to do it explicitly
a=input("Enter a number a") 

# Data type: str
# Description: This code defines a variable `a` and assigns it the value of user input, which is always of type `str`.
b = input("Enter a number b")
z= int(a) + int(b)
print(z)

ch = input("Enter a character")
# Data type: str
# Description: This code defines a variable `ch` and assigns it the value of user input, which is always of type `str`.
print(ch)

#eval function  it wil evaluate the expression and give the result
# example 
result = eval(input("Enter a expression"))
print(result)

# argv it is used to take the command line arguments
# example
x = int(sys.argv[1])
y = int(sys.argv[2])
print(x+y)