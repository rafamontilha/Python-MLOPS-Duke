# ❌ Criando variáveis desnecessárias
dados_brutos = carregar_dados()
dados_limpos = limpar(dados_brutos)
dados_normalizados = normalizar(dados_limpos)
dados_transformados = transformar(dados_normalizados)

# ✅ Reatribuindo (melhor para memória)
dados = carregar_dados()
dados = limpar(dados)
dados = normalizar(dados)
dados = transformar(dados)

# Pipeline de processamento de features
features = dados_brutos

for transformacao in pipeline_transformacoes:
    features = transformacao.aplicar(features)  # Reatribui a cada iteração
    
# Ao final, features contém o resultado final

#Acumuladores em loops
# ✅ Reatribuição clara do propósito
total = 0
for valor in valores:
    total += valor  # Reatribuindo para acumular
    
media = total / len(valores)  # Nova variável com novo propósito

#Quando criar novas variáveis?
#Quando precisa comparar estados intermediários

# MLOps: Comparar modelo antes e depois do retreino
modelo_atual = carregar_modelo("producao")
modelo_novo = treinar_modelo(novos_dados)

# Precisa dos dois para comparar métricas
metrica_atual = avaliar(modelo_atual, dados_validacao)
metrica_novo = avaliar(modelo_novo, dados_validacao)

if metrica_novo > metrica_atual:
    deploy(modelo_novo)

#quando valores tem significados distintos

# ❌ Confuso - reutiliza demais
result = consultar_api_receita(cnpj)
result = processar_resposta(result)
result = salvar_database(result)

# ✅ Claro - cada variável tem significado
dados_receita = consultar_api_receita(cnpj)
empresa_processada = processar_resposta(dados_receita)
id_registro = salvar_database(empresa_processada)

#Debugging e Logging

# ✅ Manter variáveis intermediárias facilita debug
dados_brutos = carregar_csv("importacoes.csv")
print(f"Linhas carregadas: {len(dados_brutos)}")

dados_validados = validar_schema(dados_brutos)
print(f"Linhas válidas: {len(dados_validados)}")

dados_enriquecidos = adicionar_features(dados_validados)
print(f"Features adicionadas: {dados_enriquecidos.columns}")

#Casos específicos de MLOPS

#Pipeline de features - Reatribuir
def pipeline_features(df):
    """Transformações em sequência - reatribui"""
    df = remover_outliers(df)
    df = normalizar_valores(df)
    df = criar_features_derivadas(df)
    return df

#Métricas de modelo - Criar novas
def avaliar_modelo(modelo, dados):
    """Diferentes métricas - variáveis separadas"""
    y_pred = modelo.predict(dados.X)
    
    accuracy = calcular_accuracy(dados.y, y_pred)
    precision = calcular_precision(dados.y, y_pred)
    recall = calcular_recall(dados.y, y_pred)
    f1 = calcular_f1(dados.y, y_pred)
    
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }

#Versionamento de dados - Criar novas
# MLOps: manter versões diferentes
dados_v1 = carregar_dados("2024-01")
dados_v2 = carregar_dados("2024-02")

# Treinar modelo em cada versão para comparar
modelo_v1 = treinar(dados_v1)
modelo_v2 = treinar(dados_v2)

