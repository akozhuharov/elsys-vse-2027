# Банкова сметка - класът пази и променя свое състояние
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append("+" + str(amount))
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:            # проверка преди промяната
            print("Недостатъчна сума!")
            return self.balance
        self.balance -= amount
        self.history.append("-" + str(amount))
        return self.balance

    def statement(self):
        print(self.owner, "баланс:", self.balance, self.history)


acc = BankAccount("Nasko", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(500)        # ще откаже
acc.statement()
