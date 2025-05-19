# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Meezan Bank"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
if __name__ == "__main__":
    user1 = Bank()
    user2 = Bank()
    user3 = Bank()
    
    print(f"initial bank name:")
    print(f"User 1: {user1.bank_name}")
    print(f"User 2: {user2.bank_name}")
    print(f"User 3: {user3.bank_name}") 
    
    Bank.change_bank_name("Habib Bank")
    print(f"\nBank name after change:")
    print(f"User 1: {user1.bank_name}")
    print(f"User 2: {user2.bank_name}")
    print(f"User 3: {user3.bank_name}") 