#18. Property Decorators: @property, @setter, and @deleter
#Assignment:
#Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

        
class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    # Getter method
    @property
    def price(self):
        return self._price

    # Setter method
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

    # Deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

#  object create 
p = Product(100)

#  price 
print(p.price)  # Output: 100

#  price update 
p.price = 150
print(p.price)  # Output: 150

#  price (negative) 
p.price = -50  # Output: Price cannot be negative.

#  price delete 
del p.price
# print(p.price)  # This will raise an AttributeError since _price has been deleted.

            