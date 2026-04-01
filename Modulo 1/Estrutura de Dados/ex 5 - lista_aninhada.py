# Lista ANINHADA (nested):
#lista_aninhada = [1, [2, 3], [4, [5, 6]], [[[7]], 8], 9]

# Lista PLANA (flat) que queremos:
#lista_plana = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Versão Básica

# Caso simples: apenas 1 nível
lista_simples = [[1, 2], [3, 4], [5, 6]]

# Solução 1: Loop simples
resultado = []
for sublista in lista_simples:
    for item in sublista:
        resultado.append(item)

print(resultado)
# [1, 2, 3, 4, 5, 6]

# Solução 2: List comprehension (mais Pythônico)
resultado = [item for sublista in lista_simples for item in sublista]
print(resultado)
# [1, 2, 3, 4, 5, 6]

#versão recursiva

def achatar_lista(lista):
    """
    Achata lista profundamente aninhada usando RECURSÃO.
    
    Args:
        lista: lista com qualquer nível de aninhamento
    
    Returns:
        lista plana
    """
    resultado = []
    
    for item in lista:
        # Se o item é uma lista, chama a função novamente (RECURSÃO)
        if isinstance(item, list):
            resultado.extend(achatar_lista(item))  # ← Recursão aqui!
        else:
            resultado.append(item)
    
    return resultado


# ===== TESTAR =====

# Teste 1: Lista simples
lista1 = [1, 2, 3]
print(f"Original: {lista1}")
print(f"Plana:    {achatar_lista(lista1)}")
print()

# Teste 2: Um nível
lista2 = [[1, 2], [3, 4], [5]]
print(f"Original: {lista2}")
print(f"Plana:    {achatar_lista(lista2)}")
print()

# Teste 3: Múltiplos níveis
lista3 = [1, [2, 3], [4, [5, 6]], [[[7]], 8], 9]
print(f"Original: {lista3}")
print(f"Plana:    {achatar_lista(lista3)}")
print()

# Teste 4: Muito aninhada
lista4 = [[[[[1]]], 2], 3, [4, [5, [6, [7]]]]]
print(f"Original: {lista4}")
print(f"Plana:    {achatar_lista(lista4)}")
