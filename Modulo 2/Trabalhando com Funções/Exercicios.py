#Escreva uma função para converter temperaturas de Fahrenheit para Celsius.

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius
#Exemplo de uso
temp_f = 100
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F is equal to {temp_c:.2f}°C")  # Output: 100°F is equal to 37.78°C

#Crie uma função que imprima alguma saída com base na entrada.

def sobrenome_completo(nome, sobrenome):
    print(f"O nome completo é: {nome} {sobrenome}")

sobrenome_completo("Maria", "Silva")  # Output: O nome completo é: Maria Silva

#Defina uma função que retorne um número aleatório.

import random
def numero_aleatorio(inicio, fim):
    return random.randint(inicio, fim)
#Exemplo de uso
print(numero_aleatorio(1, 100))  # Output: A random number between

#Implemente uma função que calcule a área de várias formas dependendo dos argumentos.

def calcular_area(forma, **kwargs):
    if forma == "retangulo":
        return kwargs.get("largura", 0) * kwargs.get("altura", 0)
    elif forma == "circulo":
        import math
        raio = kwargs.get("raio", 0)
        return math.pi * (raio ** 2)
    elif forma == "triangulo":
        return 0.5 * kwargs.get("base", 0) * kwargs.get("altura", 0)
    elif forma == "quadrado":
        return kwargs.get("lado", 0) ** 2
    elif forma == "trapezio":
        return 0.5 * (kwargs.get("base_maior", 0) + kwargs.get("base_menor", 0)) * kwargs.get("altura", 0)
    elif forma == "losango":
        return 0.5 * kwargs.get("diagonal_maior", 0) * kwargs.get("diagonal_menor", 0)
    else:
        return "Forma desconhecida"

#Exemplo de uso
print(calcular_area("retangulo", largura=5, altura=10))  # Output: 50
print(calcular_area("circulo", raio=7))  # Output: 153.93804002589985
print(calcular_area("triangulo", base=10, altura=5))  # Output: 25.0
print(calcular_area("quadrado", lado=4))  # Output: 16
print(calcular_area("trapezio", base_maior=10, base_menor=5, altura=4))  # Output: 30.0
print(calcular_area("losango", diagonal_maior=8, diagonal_menor=6))  # Output: 24.0


#Escreva uma função de saudação reutilizável que receba uma entrada de nome.

def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo(a)!"
#Exemplo de uso
print(saudacao("Carlos"))  # Output: Olá, Carlos! Bem-vindo(a)!

#Usar uma expressão de gerador para calcular a soma dos quadrados de 1 a 100 aqui calculo soma a soma
calcula_soma = 0
def soma_quadrados():
    x = 1
    while x <= 100:
        soma_quadrados = sum(i**2 for i in range(1, x + 1))
        yield soma_quadrados
        x += 1


calcula_soma = soma_quadrados()

print(next(calcula_soma))  # Output: 328350

#for _ in range(100):
#    print(f"Soma até o momento: {next(calcula_soma)}")  # Output: 328350 (same result since it's a generator that yields the same sum)

try:
    contador = 0
    while contador < 101:  # Mostra apenas primeiros 5
        resultado = next(calcula_soma)
        print(f"Soma dos quadrados 1 a {contador + 1}: {resultado}")
        contador += 1
except StopIteration:
    print("Não há mais valores!")

#Implemente um gerador que pegue uma lista e faça um loop sobre ela em ordem inversa

def gerador_inverso(lista):
    for i in range(len(lista) - 1, -1, -1):
        yield lista[i] 
#Exemplo de uso

minha_lista = [1, 2, 3, 4, 5]  
for item in gerador_inverso(minha_lista):
    print(item, end=' ')  # Output: 5 4 3 2 1
