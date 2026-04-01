#Causar e tratar um TypeError ao concatenar os tipos de dados errados
try:
    result = "Hello" + 5
except TypeError as error:
    print(f"Erro de tipo: {error}")
    print(f"💡 Correção: converta o número para string")
    result = "Hello" + str(5)
    print(f"✅ Resultado correto: {result}")