from account import acc


class Checking(acc.Account):
    """This class is a checking account"""

    type = "checking"

    def __init__(self, filepath, fee):
        acc.Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking("balance.txt", fee=1)
checking.transfer(110)
print(checking.balance)
print(checking.__doc__)
