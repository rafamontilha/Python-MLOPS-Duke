
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