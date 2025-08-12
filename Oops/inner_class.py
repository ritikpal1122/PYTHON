# A class have variables and methiods
# but a class can also have inner classes
# example of inner class


class RitikMain:
    def __init__(self , rollNo , name):
        self.rollNo = rollNo
        self.name = "Ritik"
        # here i want to print the age of Ritik
        
        # here iam using inner class 
        # this method calls the constructor of InnerClass
        # and initializes the age variable
        # so that i can use it later
        # this is how we use inner class in python
        self.age = self.InnerClass()
    
    def show (self):
        print(self.name, self.rollNo)
    
    class InnerClass:
        def __init__(self):
            self.age = 9
        def display(self):
            print("Age is :", self.age) 


r1 = RitikMain(1, "Ritik")

r1.show()

age1  = r1.age
print(age1)  # This will raise an error because age is not initialized in InnerClass