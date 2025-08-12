


class A:
    
    
    def  __init__(self):
        print("Constructor of A is called")
    
    def Feature1 (self):
        print("Feature 1 is working")
    
    def Feature1 (self):
        print("Feature 2 is working")
        
# in this if im invoking feature 1 then why it printing 2nd one?



        
class B(A):
    # B is inheriting from A
    # so B will have all the features of A
    def  __init__(self):
        super().__init__()
        print("B is init ")
    
    def Feature3 (self):
        print("Feature 3 is working")
    def Feature4 (self):
        print("Feature 4 is working")
        
# class C(A,B):
#     # C is inheriting from A and B
#     # so C will have all the features of B and A
#     def  __init__(self):
#         super().__init__()
#         print("C is init ")
        
        
a1 = B()

a1.Feature1()  # Output: Feature 2 is working





# how consteuctun behaves in inheritance
# how to user super() to call the constructor of parent class
# method resolution order (MRO) in python



#                        A        B 
#                            C        