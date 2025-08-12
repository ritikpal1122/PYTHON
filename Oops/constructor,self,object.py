# the size of object decides how many variables it can hold
# the size of object is determined by the number of attributes it has

# who allocate size of object -> Depeds upon number of variables and size of that variable 

# thats our Constructor that allocates the size of object


class  Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print("Constructor called. Object size allocated.")
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
    
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated to: {self.salary}")
    
    def compare_salary(self, other_employee):
        if self.salary > other_employee.salary:
            print(f"{self.name} has a higher salary than {other_employee.name}.")
        elif self.salary < other_employee.salary:
            print(f"{self.name} has a lower salary than {other_employee.name}.")
        else:
            print(f"{self.name} and {other_employee.name} have the same salary.")
# This code demonstrates the use of a constructor in a class to allocate memory for an object.
# It defines an Employee class with attributes for name, age, and salary.
# Creating an object of the Employee class
emp1 = Employee("Ritik", 25, 50000)  # Constructor called. Object size allocated.

emp1.display()  # Output: Name: Ritik, Age: 25, Salary: 50000
emp1.update_salary(60000)  # Output: Salary updated to: 60000
emp1.display()  # Output: Name: Ritik, Age: 25, Salary: 60000
# Creating another object of the Employee class
emp2 = Employee("Rohan", 30, 55000)  # Constructor called. Object size allocated.
emp2.display()  # Output: Name: Rohan, Age: 30, Salary: 55000
emp1.compare_salary(emp2)  # Output: Ritik has a lower salary than Rohan.
# This code illustrates how constructors are used to initialize object attributes and allocate memory for the object.
# It also shows how to define methods for displaying information, updating attributes, and comparing objects.
# The constructor is responsible for setting up the initial state of the object when it is created.
# The size of the object is determined by the number of attributes it has and their data types.

# compare
# compare is a method that is used to compare two objects of the same class.


emp1.compare_salary(emp2)  # Output: Ritik has a lower salary than Rohan.