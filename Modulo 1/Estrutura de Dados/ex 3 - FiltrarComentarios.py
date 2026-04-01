# Lista de comentários
comentarios = [
    "Esse produto é muito bom!",
    "Que droga de atendimento",
    "Adorei a compra, recomendo",
    "Isso é uma porcaria completa"
]

# SET de palavrões (busca mais rápida!)
palavroes = {"droga", "porcaria", "idiota", "burro", "merda"}

print("🔍 VERIFICANDO COMENTÁRIOS (COM SETS)...\n")

for comentario in comentarios:
    # Pegar todas as palavras do comentário
    palavras_comentario = comentario.lower().split()
    
    # Converter para SET
    palavras_set = set(palavras_comentario)
    
    # INTERSEÇÃO: palavras do comentário QUE ESTÃO no set de palavrões
    palavroes_encontrados = palavras_set & palavroes  # ← Operação de SET!
    
    if palavroes_encontrados:
        print(f"❌ BLOQUEADO: '{comentario}'")
        print(f"   Palavrões: {palavroes_encontrados}\n")
    else:
        print(f"✅ APROVADO: '{comentario}'\n")

#outra forma

def filtrar_comentarios(comentarios, palavroes):
    """
    Filtra comentários que contêm palavrões.
    
    Args:
        comentarios: lista de strings com comentários
        palavroes: lista ou set de palavrões
    
    Returns:
        tupla com (comentários_aprovados, comentários_bloqueados)
    """
    # Garantir que palavrões é um set (mais eficiente)
    palavroes_set = set(palavroes)
    
    comentarios_aprovados = []
    comentarios_bloqueados = []
    
    for comentario in comentarios:
        # Pegar palavras do comentário
        palavras = comentario.lower().split()
        palavras_set = set(palavras)
        
        # Verificar se tem palavrão (interseção)
        if palavras_set & palavroes_set:
            comentarios_bloqueados.append(comentario)
        else:
            comentarios_aprovados.append(comentario)
    
    return comentarios_aprovados, comentarios_bloqueados


# ===== USAR A FUNÇÃO =====

comentarios = [
    "Esse produto é muito bom!",
    "Que droga de atendimento",
    "Adorei a compra, recomendo",
    "Isso é uma porcaria completa",
    "Entrega rápida e qualidade excelente"
]

palavroes = ["droga", "porcaria", "idiota", "burro"]

# Filtrar
aprovados, bloqueados = filtrar_comentarios(comentarios, palavroes)

# Mostrar resultados
print(f"📊 ESTATÍSTICAS:")
print(f"   Total de comentários: {len(comentarios)}")
print(f"   ✅ Aprovados: {len(aprovados)}")
print(f"   ❌ Bloqueados: {len(bloqueados)}\n")

print("✅ COMENTÁRIOS APROVADOS:")
for comentario in aprovados:
    print(f"   • {comentario}")

print("\n❌ COMENTÁRIOS BLOQUEADOS:")
for comentario in bloqueados:
    print(f"   • {comentario}")
