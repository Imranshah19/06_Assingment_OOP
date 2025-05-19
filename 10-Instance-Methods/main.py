#10. Instance Methods
#Assignment:
#Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name  # instance variable
        self.breed = breed # instance variable
        
     # instance method   
    def bark(self):
        print(f"{self.name} is barking!")
        
if __name__ == "__main__":
    # creating an object instance of Dog
    my_dog = Dog("Tommy", "Labrador")
    # Calling the instance method
    my_dog.bark()
        