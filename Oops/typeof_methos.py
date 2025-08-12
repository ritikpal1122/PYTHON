
# type of methods in python 
# There are three types of methods in Python:
# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods
class MyClass:
    # Instance Method
    def instance_method(self):
        return "This is an instance method"

    # Class Method
    @classmethod # why we use @classmethod decorator  
#    # It is used to define a method that belongs to the class rather than an instance of the class.
    def class_method(cls):
        return "This is a class method"

    # Static Method
    @staticmethod
    def static_method():
        return "This is a static method"
    
# Example usage
obj = MyClass()
print(obj.instance_method())  # Output: This is an instance method
print(MyClass.class_method())  # Output: This is a class method
print(MyClass.static_method())  # Output: This is a static method
# Accessing class method through an instance
