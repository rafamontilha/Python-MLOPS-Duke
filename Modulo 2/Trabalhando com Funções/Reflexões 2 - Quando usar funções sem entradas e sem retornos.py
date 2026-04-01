#Reflexões 2 - Quando usar funções sem entradas e sem retornos

#Função sem entradas e sem retornos

#1. Funções de Configuração/Inicialização

def inicializar_conexao_bd():
    """Configura conexão global com banco - sem entrada, sem retorno"""
    global conexao_db
    conexao_db = conectar_postgresql()
    print("Conexão estabelecida")

def resetar_configuracoes():
    """Reset para configurações padrão"""
    config.host = "localhost"
    config.porta = 5432
    config.debug = False

#2. Funções de Logging/Monitoramento

def registrar_inicio_processamento():
    """Registra timestamp de início"""
    with open("log.txt", "a") as f:
        f.write(f"Processamento iniciado: {datetime.now()}\n")

def enviar_heartbeat():
    """Envia sinal de vida para monitoramento"""
    requests.post("http://monitor.bgc.com/heartbeat")

#3. Funções de Limpeza/Manutenção

def limpar_arquivos_temporarios():
    """Remove arquivos temp sem precisar de parâmetros"""
    import os, glob
    for arquivo in glob.glob("/tmp/bgc_*.tmp"):
        os.remove(arquivo)

def vacuum_database():
    """Otimiza banco de dados periodicamente"""
    cursor.execute("VACUUM ANALYZE;")