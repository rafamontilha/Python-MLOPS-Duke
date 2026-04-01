
#Capture um ZeroDivisionError para imprimir uma mensagem de erro amigável


try:
    #some intense operation that causes an error
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    result = num1 / num2
    print(f"O resultado da divisão é: {result}")
    
except ZeroDivisionError as error:
    print(f"Que pena! tivemos um problema {error}")
    #result = 14 / 2
print(result)
