# variables in class 
# there are two types of variables in class
# 1. instance variables
# 2. class (static) variables



# example of instance variable
class MyClass:
    def __init__(self):
        self.instance_var = "I am an instance variable"
    def display_instance_var(self):
        print(self.instance_var)


# example of class variable
class MyClassWithClassVar:
    class_var = "I am a class variable"
    
    def display_class_var(self):
        print(MyClassWithClassVar.class_var)
# Example usage
obj1 = MyClass()
obj1.display_instance_var()  # Output: I am an instance variable
obj2 = MyClassWithClassVar()
obj2.display_class_var()  # Output: I am a class variable
# Example of accessing class variable from instance
obj3 = MyClassWithClassVar()
print(obj3.class_var)  # Output: I am a class variable