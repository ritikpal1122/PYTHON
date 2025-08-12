# __init__ in  the class definition used for initializing the object of the class
# # is a special method that is automatically called when an object of the class is created.
# # It is used to initialize the attributes of the class.

class new_one:
    # the args in init method are parameters that are passed when creating an object of the class.
    def __init__(self , name, age):
        self.name = name
        self.age = age
    # here self is a reference to the current instance of the class
 
    def  display(self):
        print("Age is: ", self.age)
        print("Name is: ", self.name)
# Example of creating an object of the class new_one
 
com1 = new_one( "123" , 12)  # Output: This is a new class with __init__ method
 # Output: This is a new class with __init__ method

com1.display()  # Output: Age is: 12, Name is: 123


# objects is the instance of the class new_one


# in the Real World example 

# A clss is Design of anything like a car, bike, etc.
# and a object is the actual thing that we use like a car, bike, etc.