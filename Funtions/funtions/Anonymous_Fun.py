## Anonymous functions are functions that are defined without a name.
# They are also known as lambda functions in Python.


def square(x):
    return x * x

result = square(5)
print(result)  # Output: 25


# Example of an anonymous function using lambda
square_anonymous = lambda x: x * x
result_anonymous = square_anonymous(5)



new_fun = lambda x: x * x
result_new_fun = new_fun(1)

# we can pass anything but should ony be one expression
print(result_anonymous)  # Output: 25
print(result_new_fun)  # Output: 1
# Example of an anonymous function with multiple arguments