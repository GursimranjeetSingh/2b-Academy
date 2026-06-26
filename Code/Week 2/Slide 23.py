class Account:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._balance = balance     # Protected (_)
        self.__pin = 1234           # Private (__)
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"✅ Deposited ₹{amount}")
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"✅ Withdrew ₹{amount}")
        else:
            print("❌ Insufficient balance!")
    def get_balance(self):
        return self._balance  # Controlled access

acc = Account('Alice', 5000)
acc.deposit(1000)
acc.withdraw(7000)  # ❌ Insufficient balance!
print(acc.get_balance())  # 6000
# acc.__pin  # AttributeError! Private attribute.