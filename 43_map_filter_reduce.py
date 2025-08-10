# map - A function that applies a given function to all items in an iterable (like a list) and returns a new iterable with the results.
# filter - A function that filters items in an iterable based on a given function that returns True or False.
# reduce - A function that applies a rolling computation to sequential pairs of values in an iterable, reducing it to a single value.

# Filter Exaple 



nums  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




# Using filter to get even numbers
def is_even(n):
    return n % 2 == 0
# filter takes two arguments: a function and an iterable.
even_nums= list (filter(is_even, nums))



# Using filter to get odd numbers
def is_odd(n):
    return n % 2 != 0

odd_nums  = list(filter(is_odd, nums))


# using lambda functions with filter
even_nums_lambda = list(filter(lambda n: n % 2 == 0, nums))
odd_nums_lambda = list(filter(lambda n: n % 2 != 0, nums))
# Output the results    
print("Even numbers: lambda ", even_nums_lambda)
print("Odd numbers: lambda", odd_nums_lambda)


print("Even numbers:", even_nums)  # Output: [2, 4, 6, 8, 10]
print("Odd numbers:", odd_nums)  # Output: [1, 3, 5, 7, 9]



# Map Example
# map takes two arguments: a function and an iterable.
def square(n):
    return n * n
# Using map to square each number in the list
squared_nums = list(map(square, nums))
# Using map with a lambda function

doubled_nums = list(map(lambda n: n + 2, nums))

print("Squared numbers:", squared_nums)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("Doubled numbers:", doubled_nums)  # Output: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]