#exemplo de função
def double(x):
    """Doubles a number"""
    return x * 2

print(double(5)) # Prints 10

#função com argumentos

def full_name(first, last):
    return first + " " + last

print(full_name("John", "Doe")) # Prints John Doe

#Argumentos da variável

def sum_all(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(sum_all(1, 2, 3)) # Prints 6

#Gerador

#counter generator
def counter(start=0):
    n = start
    while True:
       yield n
       n += 1

for i in counter(5):
    if i > 10:
        break 
    print(i)

#Infinite Fibonacci sequence generator
def fib():
    a, b = 0, 1
    while True:
       yield a 
       a, b = b, a + b
       
for n in fib():
   if n > 10:
     break  
   print(n)

#Expressão do gerador: Sintaxe mais compacta, como as compreensões de lista para 
#geração preguiçosa em linha, usa () em vez de []
#Generator expression to get squares

nums = (x**2 for x in range(10))
print(list(nums))

#Sequência infinita: Os geradores podem ser infinitamente recursivos/iterativos
#para modelar fluxos de dados

# Infinite random attack sequence
import random

attacks = ["kimura", "armbar", "triangle"] 

def lazy_random_attacks():
    """Lazily yield random attacks forever"""
    
    while True:
        attack = random.choice(attacks)
        print("Yielding attack") 
        yield attack
        
generator = lazy_random_attacks()

for _ in range(5):
    print(next(generator))

#Os pontos principais:

#Laço While para iterar para sempre

#Usa yield para produzir preguiçosamente um ataque de cada vez

#A execução é suspensa após cada yield até que next() seja chamado novamente