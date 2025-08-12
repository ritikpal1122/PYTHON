

a = 5

b ="tiya"

# a + b  # this will give an error because we cannot add int and str
# but we can overload the + operator to add int and str

print(a+b)

# magic methods are used to overload the operators in python
class MyInt:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, MyInt):
            return MyInt(self.value + other.value)
        return NotImplemented
    
    def __str__(self):
        return str(self.value)