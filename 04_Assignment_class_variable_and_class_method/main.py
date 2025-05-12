class Bank:
    # Class variable
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Create instances of Bank
account1 = Bank("Nida")
account2 = Bank("Alisha")

# Display info before changing the bank name
print("Before changing bank name:")
account1.display_info()
account2.display_info()

# Change the bank name using the class method
Bank.change_bank_name("Super Bank")

# Display info after changing the bank name
print("\nAfter changing bank name:")
account1.display_info()
account2.display_info()
