#Exemplo de Classe

class Vehicle:
    wheels = 4 # Class attribute
    
    def __init__(self, make, model):
        self.make = make # Instance attribute
        self.model = model
        
    def description(self): # Method
        return f"The {self.make} {self.model}"

car = Vehicle("BMW", "i3") # Instance created
print(car.wheels) # Access class attribute
print(car.description()) # Call instance method

#Exemplo de Herança

class Pet:
    def eat(self):
        print("Chomp")
        
class Dog(Pet):
    def bark(self):
        print("Bark!")
        
dog = Dog()
dog.eat() # Inherited method
dog.bark() # Dog specific method

#classe mais básica

class Basic:
    pass

basic = Basic()
print(basic)

dir(basic)

# no passado classes em python tinham "object" como superclasse, mas isso mudou com o Python 3, onde todas as classes são "new-style" e herdam implicitamente de "object". Portanto, mesmo que você não declare explicitamente a herança de "object"

class Basic (object):
    pass

#isso não é mais necessário, mas é uma prática comum em versões anteriores do Python para garantir que a classe seja um "new-style class". Em Python 3, você pode simplesmente escrever:

#No geral classes em python é bom quando agrupamos codigo e comportamento relacionados,
# quando queremos criar objetos com atributos e métodos específicos.
# Elas ajudam a organizar o código, promover a reutilização e facilitar a manutenção.

class Dog:
    is_animal = True # Class attribute

    def bark(self):
        print("Woof!")

dog = Dog()
print(dog.is_animal) # Accessing class attribute

dog.bark() # Calling method without self will raise an error
dog.is_animal

rufus = Dog()
rufus.bark() # Rufus can also bark, showing that the method is shared across instances
print(rufus.is_animal) # Rufus also has access to the class attribute

Dog.is_animal = False
print("Is rufus an animal?", rufus.is_animal) # This will reflect the change in the class attribute
print("Is dog an animal?", dog.is_animal) # This will also reflect the change in the class attribute

class Dog:

    def __init__(self):
        self.is_animal = True # This is an instance attribute, not a class attribute

dog = Dog()
dog.is_animal

rufus = Dog()
sparky = Dog()

print(rufus.is_animal) # Each instance has its own is_animal attribute
print(sparky.is_animal) # Each instance has its own is_animal attribute

rufus.is_animal = False
print("Is rufus an animal?", rufus.is_animal) # This will
print("Is sparky an animal?", sparky.is_animal) # This will still be True, showing that instance attributes are independent


class Animal:
    def __init__(self, name, legs = 4, barks =True):
        self.name = name
        self.legs = legs
        self.barks = barks

    #there is a bug!

    def info(self):
        print(f"This is an animal named {self.name} with {self.legs} legs and it {'barks' if self.barks else 'does not bark'}.")
        if self.barks:
            print("And this animal barks!")
        else:
            print("And this animal does not bark!")

bunny = Animal("buster", barks = False)
bunny.info()

print(bunny.name) # Accessing instance attribute
print(bunny.legs) # Accessing instance attribute
print(bunny.barks) # Accessing instance attribute