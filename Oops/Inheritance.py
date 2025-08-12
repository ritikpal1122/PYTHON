

# inheritabce is the process of acquiring the properties and behaviors of another class

# copying the properties and behaviors of another class is called inheritance

# A super class
# B  sub class



class A:
    def Feature1 (self):
        print("Feature 1 is working")
    
    def Feature1 (self):
        print("Feature 2 is working")
        
# in this if im invoking feature 1 then why it printing 2nd one?

        
class B(A):
    # B is inheriting from A
    # so B will have all the features of A
    def Feature3 (self):
        print("Feature 3 is working")
    def Feature4 (self):
        print("Feature 4 is working")
        
class C(B):
    # C is inheriting from B
    # so C will have all the features of B and A
    def Feature5 (self):
        print("Feature 5 is working")
        
# Example usage
b = B()
b.Feature1()  # Output: Feature 1 is working

c = C()
c.Feature1()  # Output: Feature 1 is working