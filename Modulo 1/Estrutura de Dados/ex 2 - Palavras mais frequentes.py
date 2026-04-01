arquivo = r"C:\Users\rafae\OneDrive\Documentos\Projetos\Python-MLOPS\UDP_Maturity_Checklist_Resumo.txt"

def palavras_mais_frequentes_com_sets(arquivo, top_n=10):
    with open(arquivo, 'r', encoding='utf-8') as f:
        texto = f.read().lower()
        palavras = texto.split()
        
        # 1. Usar SET para encontrar palavras ÚNICAS
        palavras_unicas = set(palavras)
        print(f"📊 Total de palavras: {len(palavras)}")
        print(f"🔤 Palavras únicas: {len(palavras_unicas)}\n")
        
        # 2. Para cada palavra única do SET, contar frequência na lista original
        frequencia = {}
        for palavra in palavras_unicas:  # ← Iterando sobre o SET
            contagem = palavras.count(palavra)
            if contagem > 1:  # Só palavras que aparecem mais de uma vez
                frequencia[palavra] = contagem
        
        # 3. Ordenar e retornar top N
        top_palavras = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)[:top_n]
        return top_palavras

# Executar
resultado = palavras_mais_frequentes_com_sets(arquivo, top_n=10)

print("🔥 TOP 10 PALAVRAS MAIS FREQUENTES (usando sets):\n")
for i, (palavra, contagem) in enumerate(resultado, 1):
    print(f"{i:2d}. {palavra:20s} → {contagem:3d} vezes")