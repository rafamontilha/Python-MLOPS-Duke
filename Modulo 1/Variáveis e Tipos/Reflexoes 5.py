# ❌ PROBLEMA: Captura genérica trata tudo igual
def carregar_config_modelo(caminho):
    try:
        with open(caminho) as f:
            config = json.load(f)
        return config['model_params']
    
    except Exception as e:  # ❌ Muito genérico!
        print(f"Erro ao carregar config: {e}")
        return {"learning_rate": 0.01}  # Usa padrão SEMPRE
        # ❌ Mas e se o arquivo EXISTE mas está corrompido?
        # ❌ E se o problema foi falta de permissão?
        # ❌ E se foi erro de memória?

# ✅ SOLUÇÃO: Captura específica permite tratamento adequado
def carregar_config_modelo(caminho):
    try:
        with open(caminho) as f:
            config = json.load(f)
        return config['model_params']
    
    except FileNotFoundError:
        # ✅ Arquivo não existe → usa padrão (OK)
        print(f"Config não encontrada, usando padrão")
        return {"learning_rate": 0.01}
    
    except PermissionError:
        # ✅ Sem permissão → ERRO GRAVE, precisa corrigir
        print(f"❌ ERRO: Sem permissão para ler {caminho}")
        raise  # Re-lança - não pode continuar
    
    except json.JSONDecodeError as e:
        # ✅ JSON inválido → tenta recuperar ou pede ajuda
        print(f"❌ JSON corrompido em {caminho}: {e}")
        # Poderia tentar backup ou alertar admin
        raise
    
    except KeyError:
        # ✅ Estrutura errada → config existe mas está incompleta
        print(f"⚠️ Config incompleta - falta 'model_params'")
        return {"learning_rate": 0.01}
    
    except MemoryError:
        # ✅ Sem memória → problema do sistema, não do código
        print(f"❌ CRÍTICO: Sem memória ao carregar {caminho}")
        # Enviar alerta para ops
        raise