#Defina uma função simples que imprima uma mensagem

from timeit import timeit


def minha_funcao():
    print("Olá, esta é a minha função!")
#Chame a função para ver a mensagem
minha_funcao()

#Escreva uma função que aceite dois argumentos e os imprima

def imprimir_argumentos(arg1, arg2):
    print(f"Argumento 1: {arg1}")
    print(f"Argumento 2: {arg2}")

#Chame a função com dois argumentos
imprimir_argumentos("Olá", "Mundo")

#Use argumentos posicionais e chame sua função

def posicional_arguments(arg1,arg2):
    print(f"Seja bem-vindo, {arg1} {arg2}!")

posicional_arguments("Rafael", "Montilha")

#Definir valores padrão para os argumentos em uma função

def saudacao(nome="Visitante"):
    print(f"Olá, {nome}! Bem-vindo ao nosso site.")
#Chame a função sem argumentos para usar o valor padrão
saudacao()

#Aplicar um decorador para cronometrar uma função

import time
from functools import wraps

def cronometrar(func):
    """Decorador simples para medir tempo de execução"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Marca início
        inicio = time.time()
        
        # Executa a função
        resultado = func(*args, **kwargs)
        
        # Calcula tempo decorrido
        tempo_execucao = time.time() - inicio
        
        # Exibe resultado
        print(f"{func.__name__} executou em {tempo_execucao:.2f} segundos")
        
        return resultado
    return wrapper

# Aplicando o decorador
@cronometrar
def calcular_fibonacci(n):
    """Função que vamos cronometrar"""
    if n <= 1:
        return n
    return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

@cronometrar
def operacao_simples():
    """Outra função para testar"""
    time.sleep(2)  # Simula operação de 2 segundos
    return "Operação concluída"

# Testando
print("=== Teste 1 ===")
resultado1 = calcular_fibonacci(3)
print(f"Fibonacci(3) = {resultado1}")

print("\n=== Teste 2 ===")
resultado2 = operacao_simples()
print(f"Resultado: {resultado2}")

#outro caso de decorador

def randomized_speed_attack_decorator(function):
    """Randomizes the speed of attacks"""

    import time
    import random

    def wrapper_func(*args, **kwargs):
        sleep_time = random.randint(0,3)
        print(f"Attacking after {sleep_time} seconds")
        time.sleep(sleep_time)
        return function(*args, **kwargs)
    return wrapper_func

@randomized_speed_attack_decorator
def lazy_return_random_attacks():
    """Yield attacks each time"""
    import random
    attacks = {"kimura": "upper_body",
           "straight_ankle_lock":"lower_body",
           "arm_triangle":"upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body"}
    while True:
        random_attack = random.choices(list(attacks.keys()))
        yield random_attack

for _ in range(5):
    print(next(lazy_return_random_attacks()))

#Criar uma closure que conte as chamadas de função

def criar_contador():
    # Variável no escopo da função externa
    count = 0
    
    def incrementar():
        nonlocal count  # Acessa variável do escopo externo
        count += 1
        return count
    
    return incrementar  # Retorna função interna

# A função externa já terminou, mas a interna "lembra" de count
contador = criar_contador()
print(contador())  # 1
print(contador())  # 2  
print(contador())  # 3

# count ainda está "viva" dentro da função!

#Passar uma função como argumento para outra função

def executar_operacao(operacao, a, b):
    """Executa uma operação matemática passada como função"""
    return operacao(a, b)

def somar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y 
# Usando a função de ordem superior
resultado_soma = executar_operacao(somar, 5, 3)
resultado_multiplicacao = executar_operacao(multiplicar, 5, 3)
print(f"Soma: {resultado_soma}")  # Soma: 8
print(f"Multiplicação: {resultado_multiplicacao}")  # Multiplicação: 15

#Aplicar uma função personalizada a uma coluna do Pandas DataFrame

import pandas as pd

# Imagine dados de exportação da BGC
dados_exportacao = {
    'empresa': ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D'],
    'cnpj': ['12345678000101', '98765432000199', '11111111000188', '22222222000177'],
    'valor_fob': [100000, 250000, 500000, 750000],
    'destino': ['Estados Unidos', 'China', 'Argentina', 'Alemanha'],
    'ncm': ['01012100', '02030400', '03041100', '04051200']
}

# Criando DataFrame - como uma "super planilha"
df = pd.DataFrame(dados_exportacao)
print(df)
# Acessar colunas
print(df['empresa'])           # Uma coluna específica
print(df[['empresa', 'valor_fob']])  # Múltiplas colunas

# Acessar linhas
print(df.iloc[0])              # Primeira linha por índice
print(df.loc[0, 'empresa'])    # Célula específica

# Informações básicas
print(df.shape)                # (4, 5) - 4 linhas, 5 colunas
print(df.columns)              # ['empresa', 'cnpj', 'valor_fob', ...]
print(df.info())               # Tipos de dados e informações gerais

# Estatísticas descritivas
print(df['valor_fob'].mean())      # Valor FOB médio
print(df['valor_fob'].sum())       # Valor FOB total
print(df.describe())               # Estatísticas de todas colunas numéricas

# Filtros
empresas_grandes = df[df['valor_fob'] > 300000]
print(empresas_grandes)

# Ordenação
df_ordenado = df.sort_values('valor_fob', ascending=False)
print(df_ordenado)

def calcular_imposto_exportacao(valor_fob):
    """Função personalizada para calcular imposto"""
    if valor_fob < 200000:
        return valor_fob * 0.10  # 10% para valores menores
    elif valor_fob < 500000:
        return valor_fob * 0.15  # 15% para valores médios
    else:
        return valor_fob * 0.20  # 20% para valores altos

# Aplicando função à coluna valor_fob
df['imposto'] = df['valor_fob'].apply(calcular_imposto_exportacao)
print(df[['empresa', 'valor_fob', 'imposto']])

#Crie um decorador que registre os argumentos da função

def registrar_argumentos(func):
    """Decorador para registrar argumentos de função"""
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__} com args: {args} e kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@registrar_argumentos
def exemplo_funcao(a, b, c=None):
    """Função de exemplo para testar o decorador"""
    return a + b if c is None else a + b + c
# Testando a função decorada
resultado1 = exemplo_funcao(1, 2)
resultado2 = exemplo_funcao(1, 2, c=3)
print(f"Resultado 1: {resultado1}")  # Resultado 1: 3
print(f"Resultado 2: {resultado2}")  # Resultado 2: 6

#Faça o curry de uma função para especializar um auxiliar de registro

def curry_registrar(prefixo):
    """Curry para criar um decorador de registro com prefixo personalizado"""
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"{prefixo} - Chamando {func.__name__} com args: {args} e kwargs: {kwargs}")
            return func(*args, **kwargs)
        return wrapper
    return decorador
# Criando um decorador especializado
registrar_com_prefixo = curry_registrar("LOG")
@registrar_com_prefixo
def funcao_de_teste(x, y):
    """Função de teste para o decorador curried"""
    return x * y
# Testando a função decorada
resultado = funcao_de_teste(4, 5)
print(f"Resultado: {resultado}")  # Resultado: 20

#Escreva uma função lambda de uma linha que eleva números ao quadrado

quadrado = lambda x: x ** 2
print(quadrado(5))  # Prints 25


#Aplicar uma função de arredondamento a colunas numéricas em um DataFrame

# Criando um DataFrame de exemplo

import pandas as pd
dados = { 'valor_fob': [123456.789, 987654.321, 555555.555]}
df = pd.DataFrame(dados)
# Arredondando valores da coluna 'valor_fob'
df['valor_fob_arredondado'] = df['valor_fob'].apply(lambda x: round(x, 2))

print(df) # Imprime o DataFrame com a nova coluna arredondada