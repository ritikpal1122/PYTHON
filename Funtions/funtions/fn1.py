# Funtion are the first step to code Reusability They Allow you to define a Resuable block of Code that can be used 
# multiple times in your program


"""
Rule is Function body should be indented with 4 spaces.
"""

# Creating a Funtion 
def hello():
    print("Hello, World!")
   
# Calling the function 
hello()

# Passing the Args to a Function

def greet(name,age):
    print(f"Hello, {name}! You are {age} years old.")
# Calling the function with arguments
greet("Ritik", 25)

# Like this you Can Send Many Agruments to a Function seperated by Commas

# Types Of Arguments
# 1. Positional Arguments
def add(a, b):
    return a + b
# Calling the function with positional arguments
result = add(5, 10)
print(f"The sum is: {result}")
# 2. Keyword Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")
# Calling the function with keyword arguments
introduce(age=30, name="Ritik")