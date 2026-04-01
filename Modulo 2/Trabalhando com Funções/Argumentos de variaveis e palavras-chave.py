#esta função pode receber 0 ou mais argumentos, dependendo de como é chamada

def family_members(*members):
    for member in members:
        print(member)

family_members("Alice", "Bob", "Charlie") # Prints Alice, Bob, Charlie

family_members() # No output, but no error either

#variaveis com palavras-chave

#definir função que aceita 0 ou mais argumentos de palavras-chave

def stats (**kwargs):
    for key, value in kwargs.items():
       # print(f"{key}: {value}")
        print(key, "--->", value)

stats(name="Alice", age=30, city="New York")

stats(speed=100, active=True, score=95.5)

#porque é variavel, podemos passar nenhum argumento

results = stats() # No output, but no error either
print("Results is", results) #Results is None