#função básica e simples
def simples():
    print("Hello, World!")
simples() # Prints Hello, World!    

#cuidado com funções que não retornam valores
result = simples()
print("O valor do Resultado é:", result) #O valor do Resultado é: None

#se precisar de valor de um retorno de função siga o exemplo abaixo

def produzir():
    return "Produto produzido"

result = produzir()
print("O valor do Resultado é:", result) #O valor do Resultado é: Produto produzido

