"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class Salary(Employee):
    def __init__(self,name, salary):
        super().__init__(name)
        self.salary = salary
    def get_pay(self):
        return self.salary
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.get_pay()}.  Their total pay is {self.get_pay()}."

class Contract(Salary):
    def __init__(self, name, salary, hours):
        super().__init__(name, salary)
        self.hours = hours
    def get_pay(self):
        return self.salary * self.hours
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.salary}/hour.  Their total pay is {self.get_pay()}.'

class MonthlySalary(Salary):
    def __init__(self, name, salary, contracts, perContract):
        super().__init__(name, salary)
        self.contracts = contracts
        self.perContract = perContract
    def get_pay(self):
        fix = super().get_pay()
        commission = self.contracts * self.perContract
        return fix + commission
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.perContract}/contract.  Their total pay is {self.get_pay()}.'

class HourlySalary(Contract):
    def __init__(self, name, salary, hours, contracts, perContract):
        super().__init__(name, salary, hours)
        self.contracts = contracts
        self.perContract = perContract
    def get_pay(self):
        fix = super().get_pay()
        commission = self.contracts * self.perContract
        return fix + commission
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a commission for {self.contracts} contract(s) at {self.perContract}/contract.  Their total pay is {self.get_pay()}.'

class MSBonusCommission(Salary):
    def __init__(self, name, salary, bonusCommission):
        super().__init__(name, salary)
        self.bonusCommission = bonusCommission
    def get_pay(self):
        return self.bonusCommission + self.salary
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonusCommission}.  Their total pay is {self.get_pay()}.'

class CBonusCommission(Contract):
    def __init__(self, name, salary, hours, bonusCommission):
        super().__init__(name, salary, hours)
        self.bonusCommission = bonusCommission
    def get_pay(self):
        con = super().get_pay()
        return con + self.bonusCommission
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a bonus commission of {self.bonusCommission}.  Their total pay is {self.get_pay()}.'
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Contract('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlySalary('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlySalary('Jan', 25, 150, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MSBonusCommission('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = CBonusCommission('Ariel', 30, 120, 600)
