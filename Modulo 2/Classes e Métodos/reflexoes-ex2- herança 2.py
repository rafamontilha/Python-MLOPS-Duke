# CLASSE PAI (Base) - código reutilizável
class EmpresaBase:
    """Classe base com funcionalidades comuns a todas empresas"""
    
    def __init__(self, nome, cnpj, setor):
        self.nome = nome
        self.cnpj = cnpj
        self.setor = setor
        self.operacoes = []
    
    def adicionar_operacao(self, operacao):
        """Método comum - todas empresas fazem operações"""
        self.operacoes.append(operacao)
    
    def calcular_total_operacoes(self):
        """Método comum - todas calculam totais"""
        return sum(op['valor'] for op in self.operacoes)
    
    def gerar_relatorio_basico(self):
        """Método comum - todas geram relatórios básicos"""
        return {
            'empresa': self.nome,
            'cnpj': self.cnpj,
            'setor': self.setor,
            'total_operacoes': len(self.operacoes),
            'valor_total': self.calcular_total_operacoes()
        }

# CLASSE FILHA 1 - Herda tudo da pai + especializa
class EmpresaExportadora(EmpresaBase):
    """Especializada em exportações - HERDA de EmpresaBase"""
    
    def __init__(self, nome, cnpj, setor):
        super().__init__(nome, cnpj, setor)  # Chama construtor da classe pai
        self.paises_destino = set()
    
    def exportar(self, valor_fob, destino, ncm):
        """Método específico de exportação"""
        # Usa método herdado da classe pai
        self.adicionar_operacao({
            'tipo': 'exportacao',
            'valor': valor_fob,
            'destino': destino,
            'ncm': ncm
        })
        self.paises_destino.add(destino)
    
    def calcular_imposto_exportacao(self):
        """Método específico - só exportadoras precisam"""
        total = self.calcular_total_operacoes()  # Método herdado!
        return total * 0.15
    
    def gerar_relatorio_exportacao(self):
        """Relatório especializado"""
        relatorio = self.gerar_relatorio_basico()  # Usa método herdado!
        relatorio.update({
            'tipo': 'Exportadora',
            'paises_destino': list(self.paises_destino),
            'imposto_devido': self.calcular_imposto_exportacao()
        })
        return relatorio

# CLASSE FILHA 2 - Herda mesma base + outra especialização
class EmpresaImportadora(EmpresaBase):
    """Especializada em importações - HERDA de EmpresaBase"""
    
    def __init__(self, nome, cnpj, setor):
        super().__init__(nome, cnpj, setor)  # Mesmo código da pai reutilizado!
        self.fornecedores = set()
    
    def importar(self, valor_cif, origem, categoria):
        """Método específico de importação"""
        # Reutiliza método da classe pai
        self.adicionar_operacao({
            'tipo': 'importacao',
            'valor': valor_cif,
            'origem': origem,
            'categoria': categoria
        })
        self.fornecedores.add(origem)
    
    def calcular_impostos_importacao(self):
        """Método específico - só importadoras precisam"""
        total = self.calcular_total_operacoes()  # Método herdado!
        return total * 0.30  # II + IPI + PIS/COFINS
    
    def gerar_relatorio_importacao(self):
        """Relatório especializado"""
        relatorio = self.gerar_relatorio_basico()  # Reutiliza código da pai!
        relatorio.update({
            'tipo': 'Importadora',
            'fornecedores': list(self.fornecedores),
            'impostos_pagos': self.calcular_impostos_importacao()
        })
        return relatorio

# CLASSE FILHA 3 - Herda de EmpresaBase + combina funcionalidades
class TradingCompany(EmpresaBase):
    """Faz importação E exportação - HERDA base + combina"""
    
    def __init__(self, nome, cnpj, setor):
        super().__init__(nome, cnpj, setor)
        self.paises_destino = set()
        self.fornecedores = set()
    
    def operacao_triangular(self, valor, origem, destino, produto):
        """Operação específica - trading companies fazem triangulação"""
        self.adicionar_operacao({  # Método herdado!
            'tipo': 'triangular',
            'valor': valor,
            'origem': origem,
            'destino': destino,
            'produto': produto
        })
        self.fornecedores.add(origem)
        self.paises_destino.add(destino)
    
    def calcular_margem_trading(self):
        """Método específico de trading"""
        total = self.calcular_total_operacoes()  # Herdado!
        return total * 0.05  # Margem típica 5%
    
# Criando instâncias - todas herdam funcionalidades básicas
exportadora = EmpresaExportadora("Soja Brasil", "11111111000111", "Agro")
importadora = EmpresaImportadora("Import Tech", "22222222000222", "Tecnologia")
trading = TradingCompany("Global Trade", "33333333000333", "Trading")

# REUTILIZAÇÃO: Todas usam métodos da classe pai
exportadora.exportar(1000000, "China", "12345678")
importadora.importar(500000, "Alemanha", "Maquinário")
trading.operacao_triangular(2000000, "Brasil", "Angola", "Açúcar")

# REUTILIZAÇÃO: Todas geram relatório usando código base
print("=== RELATÓRIOS (código reutilizado) ===")
print(exportadora.gerar_relatorio_exportacao())
print(importadora.gerar_relatorio_importacao())
print(trading.gerar_relatorio_basico())  # Pode usar o básico também!

# ESPECIALIZAÇÃO: Cada uma tem métodos únicos
print(f"Imposto exportação: ${exportadora.calcular_imposto_exportacao():,.2f}")
print(f"Impostos importação: ${importadora.calcular_impostos_importacao():,.2f}")
print(f"Margem trading: ${trading.calcular_margem_trading():,.2f}")