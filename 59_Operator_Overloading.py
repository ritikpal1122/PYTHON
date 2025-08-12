

# a = 5

# b ="tiya"

# a + b  # this will give an error because we cannot add int and str
# but we can overload the + operator to add int and str

# print(a+b)

# magic methods are used to overload the operators in python
class MyInt:
    def __init__(self, m1 , m2):
        self.m1 = m1
        self.m2 = m2
    
    # heere we are overloading the + operator
    def __add__(self, other):
        m1  = self.m1 + other.m1
        m2  = self.m2 + other.m2
    
        return MyInt(m1, m2)
    
    def __str__(self):
        return f"MyInt(m1={self.m1}, m2={self.m2})"
# Example usage
a = MyInt(5 ,9)
b  = MyInt(10 , 1)
c = a + b


 # This will use the overloaded __add__ method
print(c)  # Output: 10