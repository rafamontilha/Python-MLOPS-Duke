#função definida com argumentos necessários

def square(number):
    return number ** 2

print(square(4)) # Prints 16

#não é possível chamar uma função sem os argumentos necessários

square() #TypeError: missing 1 required positional argument: 'number'

#existem funções com argumentos opcionais, que possuem um valor padrão

int() # Prints 0

#mas podemos usar argumentos também, o que a torna flexível

int("18") # Prints 18

# um argumento opcional usa uma "palavra chave como argumento"

def greet(full_name="Rafa Montilha"):
    print("Hello, " + full_name + "!")

greet()
greet("Superman") # Hello, Superman!

#argumentos sempre vem antes de palavras chave

def formal_greeting(first_name, title="Dr."):
    print("Hello, " + title + " " + first_name + "!")

formal_greeting() #TypeError: formal_greeting() missing 1 required positional argument: 'first_name'
formal_greeting("John") # Hello, Dr. John!



