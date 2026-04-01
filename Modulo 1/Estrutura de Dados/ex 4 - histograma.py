# Texto de exemplo
texto = """
Python é uma linguagem incrível. Python é fácil de aprender.
Programar em Python é divertido. Python tem muitas bibliotecas.
"""

print("📊 HISTOGRAMA DE PALAVRAS\n")
print("=" * 60)

# 1. Limpar e separar palavras
palavras = texto.lower().split()

# 2. Contar frequências usando DICIONÁRIO
frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

# 3. Criar histograma visual
for palavra, contagem in frequencia.items():
    # Criar barra: cada █ representa 1 ocorrência
    barra = '█' * contagem
    print(f"{palavra:15s} {barra} ({contagem})")

print("=" * 60)