# map - A function that applies a given function to all items in an iterable (like a list) and returns a new iterable with the results.
# filter - A function that filters items in an iterable based on a given function that returns True or False.
# reduce - A function that applies a rolling computation to sequential pairs of values in an iterable, reducing it to a single value.

# Filter Exaple 

from functools import reduce



nums  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




# Using filter to get even numbers
#filter is a built-in function that filters elements from an iterable based on a function that returns True or False.
# It returns an iterator that produces the filtered elements.
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
# map does not return a list, it returns a map object, which is an iterator.

def square(n):
    return n * n
# Using map to square each number in the list
squared_nums = list(map(square, nums))
# Using map with a lambda function

doubled_nums = list(map(lambda n: n + 2, nums))

print("Squared numbers:", squared_nums)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("Doubled numbers:", doubled_nums)  # Output: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]



# Reduce Example
# reduce takes two arguments: a function and an iterable.
# reduce does not return a list, it returns a single value.

def add(x, y):
    return x + y
# Using reduce to sum all numbers in the list
sum_of_nums = reduce(add, nums)
# Using reduce with a lambda function
sum_of_nums_lambda = reduce(lambda x, y: x + y, nums)
print("Sum of numbers:", sum_of_nums)  # Output: 55
print("Sum of numbers: lambda", sum_of_nums_lambda)  # Output: 55

# we can normally perform addition on list then why  we need reduce
# The reduce function is useful when we want to perform a cumulative operation on the elements of an iterable.


nums = [1, 2, 3, 4, 5]
# Using reduce to multiply all numbers in the list
def multiply(x, y):
    return x * y
product_of_nums = reduce(multiply, nums)

# multi ply all normal way
product_of_nums_normal = 1
for num in nums:
    product_of_nums_normal *= num
print("Product of numbers:", product_of_nums)  # Output: 120




# Real World Example 

# map 

# gettin json data and apply filter 
import json
# Sample JSON data  
json_data= '''
[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
'''
# Parse JSON data
new_data = json.loads(json_data)
# Using map to extract names from the JSON data

#using map  to get names iwhout lambda
def get_name(x):
    return x['name']
names = map(get_name, new_data)
# Convert map object to list
names_list = list(names)
print("Names:", names_list)  # Output: ['Alice', 'Bob', 'Charlie']

names = list(map(lambda person: person['name'], new_data))
print("Names:", names)  # Output: ['Alice', 'Bob', 'Charlie']




new_json = '''
[
    {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
]
'''

def get_name (x):
    return x['name']
# Parse new JSON data
new_data = json.loads(new_json)
# Using map to extract names from the new JSON data
names = map(get_name, new_data)
# Convert map object to list

names_list = list(names)
print("Names from new JSON:", names_list)  # Output: ['Alice']