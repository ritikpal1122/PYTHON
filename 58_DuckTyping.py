# Duck typing is a concept in Python where the type or class of an object is less important than the methods it defines or the way it behaves.




x= 10

x = "Ritik"

# In duck typing, if an object behaves like a certain type (i.e., it has the required methods or properties),
def  greet(name):
    print(f"Hello, {name}")
    
greet(x)



class MyEditor:
     def execute(self):
         print(f"Executing text : Ritik Pal hu ye")



class MyImageEditor:
   def new(self,ide):
       ide.execute()
       
# This allows for flexibility in the code, as it can work with any object that has the required methods,
# regardless of its actual type.
ide = MyEditor()


image_editor = MyImageEditor()
image_editor.new(ide)  # Output: Executing text: