#crie uma hierarquia de classes para diferentes veículos

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car = Vehicle("Toyota", "Corolla")
print(f"Vehicle: {car.make} {car.model}")

#defina um método que receba argumentos regulares e argumentos de palavra-chave

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self, *args, **kwargs):
        print(f"Vehicle: {self.make} {self.model}")
        print("Additional Info:")
        for arg in args:
            print(f"- {arg}")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

carro = Vehicle("Honda", "Civic")
carro.display_info("Sedan", "2020", color="Red", mileage="30,000 km")

#Imprimir todos os atributos de uma instância da classe veículo

print(vars(Vehicle("Ford", "Mustang")))

#criar classe sem métodos e criar uma instância dessa classe

class EmptyClass:
    pass

instance = EmptyClass()
print(instance)