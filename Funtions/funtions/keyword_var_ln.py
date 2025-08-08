def person(name, **data): #here kwarg is used to pass additional information
    
    """
   - > Keyworded Variable Length Arguments
    Function to display person's name and additional information.
    :param name: Name of the person
    :param data: Additional information as keyword arguments
    """
    print("Name:", name)
    print("Additional Information:", data)
    # lets see i want to print the data in a formatted way
    for key, value in data.items():
        print(f"{key.capitalize()}: {value}")
    
person (name="Ritik", age=25, city="Delhi")



def new_person(name, **new_data):
    """
    Function to display person's name and additional information.
    :param name: Name of the person
    :param new_data: Additional information as keyword arguments
    """
    print("Name:", name)
    print("Additional Information:", new_data)
    # print everything one by one 
    for key, value in new_data.items():
        print(f"{key.capitalize()}: {value}")
    
# lets see i want to print the data in a formatted way
new_person(name="Ritik", age=25, city="Delhi", country="India")