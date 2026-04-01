class EmpresaExportadora:
    """Classe que representa uma empresa exportadora"""
    
    def __init__(self, nome, cnpj, setor):
        # Atributos (dados do objeto)
        self.nome = nome
        self.cnpj = cnpj
        self.setor = setor
        self.exportacoes = []
    
    def adicionar_exportacao(self, valor_fob, destino, ncm):
        """Método (comportamento do objeto)"""
        exportacao = {
            'valor_fob': valor_fob,
            'destino': destino,
            'ncm': ncm,
            'empresa': self.nome
        }
        self.exportacoes.append(exportacao)
    
    def calcular_total_exportado(self):
        """Método que calcula total exportado"""
        return sum(exp['valor_fob'] for exp in self.exportacoes)
    
    def __str__(self):
        return f"Empresa: {self.nome} (CNPJ: {self.cnpj})"

# Uso
empresa_a = EmpresaExportadora("Agro Brasil S/A", "12345678000195", "Agronegócio")
empresa_a.adicionar_exportacao(500000, "China", "01234567")
empresa_a.adicionar_exportacao(300000, "EUA", "02345678")

print(empresa_a)  # Empresa: Agro Brasil S/A (CNPJ: 12345678000195)
print(f"Total exportado: ${empresa_a.calcular_total_exportado():,.2f}")  # $800,000.00