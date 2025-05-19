#15. Method Resolution Order (MRO) and Diamond Inheritance
#Assignment:
#Create four classes:

#A with a method show(),

#B and C that inherit from A and override show(),

#D that inherits from both B and C.

#Create an object of D and call show() to observe MRO.

        
# Base class A
class A:
    def show(self):
        print("A class method")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("B class method")

# Class C inherits from A and overrides show()
class C(A):
    def show(self):
        print("C class method")

# Class D inherits from both B and C
class D(B, C):
    pass

# Creating an object of class D
obj = D()

# Calling the show method
print("Calling obj.show():")
obj.show()

# Print the Method Resolution Order
print("\nMethod Resolution Order (MRO):")
for cls in D.__mro__:
    print(cls)
