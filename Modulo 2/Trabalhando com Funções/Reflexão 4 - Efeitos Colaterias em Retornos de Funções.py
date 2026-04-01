#Efeitos Colaterais - Definição Técnica
# FUNÇÃO PURA - sem side effects
def calcular_imposto(valor):
    return valor * 0.15

# FUNÇÃO COM SIDE EFFECTS - modifica estado externo
contador_global = 0

def calcular_imposto_com_side_effect(valor):
    global contador_global
    contador_global += 1           # Side effect 1: modifica variável global
    log_file.write(f"Cálculo: {valor}")  # Side effect 2: escreve arquivo
    send_notification()            # Side effect 3: envia notificação
    return valor * 0.15

#Problemas dos Side Effects
#1. Imprevisibilidade

# Função "inocente" que causa chaos
def processar_exportacao(dados):
    """Parece só processar, mas..."""
    resultado = dados['valor'] * 1.2
    
    # Side effects ocultos
    database.delete_all_records()     # 😱 Apaga tudo!
    enviar_email_ceo("Processamento completo")  # 😱 Spam no CEO!
    time.sleep(60)                    # 😱 Trava aplicação!
    
    return resultado

# Usar essa função é perigoso - você não sabe o que vai acontecer

#2. Dificuldade de Teste

# Impossível testar isoladamente
def calcular_score_cliente(cliente_id):
    score = 0.8  # cálculo simples
    
    # Side effects que quebram testes
    DATABASE.update_last_access(cliente_id)  # Modifica BD
    CACHE.invalidate(cliente_id)             # Limpa cache
    AUDIT_LOG.record_access(cliente_id)      # Cria log
    
    return score

# Como testar? Precisa de BD, cache, sistema de audit...

#3. Concorrência Problemática
# Variável global compartilhada
total_processado = 0

def processar_lote(dados):
    global total_processado
    resultado = calcular_metricas(dados)
    total_processado += len(dados)  # Race condition!
    return resultado

# Em ambiente multi-thread, total_processado fica inconsistente

#4.  Valores Padrão Silenciosos

# Problema que você identificou
def converter_preco(valor_string):
    try:
        return float(valor_string)
    except:
        return 0.0  # Valor padrão silencioso - PERIGOSO!

# Uso perigoso
preco = converter_preco("abc")  # Retorna 0.0 silenciosamente
if preco > 100:                 # Lógica quebrada
    aplicar_desconto()

# Melhor abordagem - explicit errors
def converter_preco_seguro(valor_string):
    try:
        return float(valor_string)
    except ValueError as e:
        raise ValueError(f"Preço inválido: {valor_string}") from e
    



