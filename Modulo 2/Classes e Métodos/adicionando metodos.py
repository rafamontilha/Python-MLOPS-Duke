#classe com dois métodos

class Budget:

    def __init__(self, budget):
        self.budget = budget

    def expense (self, amount):
        self.budget = self.budget - amount
        self.report()

    def report(self, currency = "$"):
        print (f"Budget left: {currency}{self.budget}")
    

budget = Budget(100)

budget.expense(23)
budget.expense(45)

april_budget = Budget(400)
april_budget.expense(34)

print("Current budget variable:", april_budget.budget)

may_budget = Budget(500)
may_budget.expense(50)
may_budget.report("PER $")
