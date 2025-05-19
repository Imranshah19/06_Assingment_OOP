#14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name
        
class Department:
    def __init__(self, employee):
        self.employee = employee
        
    def show_employee(self):
        print(f"Employee in Department: {self.employee.name}")  
        
if __name__ == "__main__":
    emp = Employee("Azlan Shah")
    dept = Department(emp)
    dept.show_employee()  # Output: Employee in Department: Azlan Shah
    
    
   
    
    