

# Decorators are a way to modify or enhance functions or methods without changing their code.


def div(x,y):
    if x<y: # Here we have implemented a condition to check if x is less than y its a Decorator
        x,y = y,x  # Swap if x is greater than y
    print (x / y)


div(2, 10)  # Output: 5.0

# so if this funtion in some other file we can use this decorator to modify the function without changing its code

# Modify the funciton takes a funciton as a parameter and returns a new function

def smart_fun(func):
    def inner(x, y):
        if x < y:
            x, y = y, x  # Swap if x is greater than y
        return func(x, y)
    return inner

div = smart_fun(div)
# Now we can use the modified function
div(2, 10)  # Output: 5.0