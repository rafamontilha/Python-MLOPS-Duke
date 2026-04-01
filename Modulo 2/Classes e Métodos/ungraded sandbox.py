#Termos-chave do Ungraded Lab Sandbox

#Objeto: uma instância de uma classe
# Class 
class UFC:  
    pass

# Object
ufc = UFC()

#Atributo: variáveis vinculadas a um objeto

class Fighter:
    def __init__(self):
        self.name = "Conor McGregor"  # Attribute 

fighter = Fighter()
print(fighter.name)

#Método: Funções definidas em uma classe

class Fighter:
    def trash_talk(self):# Method
        print("I'm the best!")

fighter = Fighter()
fighter.trash_talk()

#Herança: A classe filha herda da classe pai

class Athlete:
    pass

class Fighter(Athlete):# Inheritance 
    pass

#Exemplo de código Python:  Herança simples
# Create a simple Competitor class
class Competitor:

  def __init__(self, name, age, weight):
    self.name = name 
    self.age = age
    self.weight = weight
 
 # Method Prints competitors stats           
  def print_stats(self):
    print(f"{self.name} is {self.age} years old and weighs {self.weight} pounds.")

# Create a Fighter class that inherits from Competitor
class Fighter(Competitor):
  pass

fighter = Fighter("Conor McGregor", 32, 170) 
fighter.print_stats()

#Exemplo de código Python:  Usando herança
# Example using inheritance 

class UFC:

  def weight_class(self, weight):
      # Maps weight to weight class
      return "Lightweight"  

# Fighter class inherits from UFC
class Fighter(UFC):

  def __init__(self, name):
    self.name = name
  
  def print_name(self):
    print(self.name)

fighter = Fighter("Khabib")  
print(fighter.weight_class(155)) 
fighter.print_name()