#8. The super() Function
#Assignment:
#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# parent class
class Person:
    def __init__(self, name):
        self.name = name
        

# child class
class Teacher(Person): # inheriting from Person
    def __init__(self,name, subject):
        super().__init__(name)
        self.subject = subject
        
# display
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}") 
    
    # creating an object
if __name__ == "__main__":
    teacher = Teacher("Azlan Shah", "Math")
    teacher.display()