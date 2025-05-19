# 06_Constructors_and_Destructors
# Assignment: Constructors and Destructors
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created.")
        
    def __del__(self):
        print("Logger object destroyed.")
        
if __name__ =="__main__":
    logger1 = Logger()
    
    
    # Explicitly deleting the objects
    del logger1
    
    
    # Note: The destructor will be called automatically when the object goes out of scope or is deleted.