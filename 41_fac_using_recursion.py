

# factorial of number using recursion 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# lets seee how this workks 

# 5* (5-1) * (5-2) * (5-3) * (5-4)
# 5 * 4 * 3 * 2 * 1 = 120

# Test the factorial functio n
print(factorial(5))  # Output: 120
# Fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Test the fibonacci function
print(fibonacci(10))  # Output: 55 