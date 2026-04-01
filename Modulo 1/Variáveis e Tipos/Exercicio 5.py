try:
    # Operação intensa que pode causar diferentes erros
    result = 14 / 0  # Vai causar ZeroDivisionError
    result = result + "100"  # Esta linha nunca executa
    
except ZeroDivisionError:
    print("⚠️ Divisão por zero detectada! Usando valor padrão.")
    result = 14 / 2
    
except TypeError as error:
    print(f"⚠️ Erro de tipo: {error}")
    result = 0

print(f"Resultado final: {result}")
