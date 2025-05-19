#12. Static Methods
#Assignment:
#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter():
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
if __name__ == "__main__":
    print("fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(0))  # Output: 32.
    print("fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(100))  # Output: 212.
    