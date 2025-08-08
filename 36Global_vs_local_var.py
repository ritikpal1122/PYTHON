# Global vs Local Variables
# Global variables are defined outside of any function and can be accessed from anywhere in the code.
# Local variables are defined within a function and can only be accessed within that function.

a = 10  # Global variable

def my_function():
    a= 20  # Local variable
    b = 5  # Local variable
    print("Inside function:")
    print("Global variable a:", a)
    print("Local variable b:", b)
    a = 10
    print("Modified local variable a:", a)
    
my_function()