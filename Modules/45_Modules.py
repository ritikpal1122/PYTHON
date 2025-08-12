
# Modules 

# A module is a file containing Python code that can define functions, classes, and variables. It can also include runnable code. Modules allow you to logically organize your Python code and reuse it across different programs.
# You can import modules into your Python scripts to use the functions and classes defined in them.
# Python has a rich standard library of modules that provide various functionalities, such as file I/O, networking, and data manipulation.
# To create a module, simply create a Python file with a .py extension and define your functions, classes, or variables in it. You can then import this module into other Python scripts using the import statement.

from cal import add 

a = 10
b = 20
result = add(a, b)
print(f"The sum of {a} and {b} is: {result}")