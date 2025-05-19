#19. callable() and __call__()
#Assignment:
#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.


class Multiplier:
        def __init__(self, factor):
            self.factor = factor  # factor to multiply by

        def __call__(self, value): # method to make the object callable
            return self.factor * value

#  object 
m = Multiplier(4)

#  object call
print(m(10))  # Output: 40

#  callable() test 
print(callable(m))  # Output: True
