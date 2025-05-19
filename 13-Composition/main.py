#13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine has started.")
        
class Car:
    def __init__(self):
        self.engine = Engine() # Composition
        
    def start_car(self):
            self.engine.start() # Accessing Engine's method via Car class
            
if __name__ =="__main__":
    my_car = Car()
    my_car.start_car() # Output: Engine started.