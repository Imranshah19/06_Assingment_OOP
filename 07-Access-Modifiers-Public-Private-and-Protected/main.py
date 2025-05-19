#7. Access Modifiers: Public, Private, and Protected
#Assignment:
#Create a class Employee with:
#a public variable name,
#a protected variable _salary, and
#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable
        
if __name__ == "__main__":
    emp = Employee("Azlan", 500000, "123-45-6789")
    # Accessing public variable
    print("Public Variable (name):", emp.name)
    # Protected variable
    print("Protected Variable (salary):", emp._salary)
    # Private variable
    try:
        print("Private Variable (security no):", emp.__ssn)
    except AttributeError as e:
        print("Error accessing private variable (__ssn):", e)
    