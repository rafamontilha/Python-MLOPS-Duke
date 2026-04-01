# class with two methods

class Budget:

    def __init__(self, budget):
        self.budget = budget

    def expense(self, amount):
        self.budget = self.budget - amount
        print(f"Budget left: {self.budget}")
        
budget = Budget(100)
# spend a few and get a report
budget.expense(23)
budget.expense(45)

class Budget:

    def __init__(self, budget):
        self.budget = budget

    def expense(self, amount):
        self.budget = self.budget - amount
        self.report()
        
    def report(self):
        print(f"Budget left: {self.budget}")

# code works just like before, but it is more organized!
april_budget = Budget(400)
april_budget.expense(34)

# methods can change the internal state of the instance
print("Current budget variable:", april_budget.budget)

# method can take arguments and keyword arguments as well
# a method can call another method. Let's add another method to do the reporting
class Budget:

    def __init__(self, budget):
        self.budget = budget

    def expense(self, amount):
        self.budget = self.budget - amount
        self.report()
        
    def report(self, currency="$"):
        print(f"Budget left: {currency}{self.budget}")

may_budget = Budget(23)
may_budget.report()
may_budget.report("PER $")