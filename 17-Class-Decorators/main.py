#17. Class Decorators
#Assignment:
#Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# Class decorator definition
def add_greeting(cls):
    # Define the new method
    def greet(self):
        return "Hello from Decorator!"
    
    # Add greet method to the class
    cls.greet = greet
    return cls

# Apply the decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create object of Person
p = Person("Azlan Shah")

# Call the added greet() method
print(p.greet())
