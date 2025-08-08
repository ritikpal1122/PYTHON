def update(a):
    x = 8 # local variable
    print("Inside function:")
    print("Local variable x:", x)
    
    
a =10 # global variable
update(a)
print("Outside function:") 
print("Global variable a:", a)


#example of paas by value
# In Python, integers are immutable, so when you pass an integer to a function,
# you are passing a reference to the value, not the value itself.
def modify_value(x):
    x = 20  # This modifies the local copy of x, not the global variable
    print("Inside function, modified x:", x)    

x = 10  # Global variable
modify_value(x)
print("Outside function, original x:", x)  # This will still print 10
#example of pass by reference
# In Python, mutable objects like lists can be modified in place,
# which can give the appearance of pass by reference.
def modify_list(lst):
    lst.append(4)  # This modifies the list in place
    print("Inside function, modified list:", lst)
lst = [1, 2, 3]  # Global list
modify_list(lst)
print("Outside function, original list:", lst)  # This will print [1, 2, 3, 4]
