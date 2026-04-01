#usando plan asserção para testar o código
def teste_soma():
    assert 1 + 1 == 2, "Teste de soma falhou"
    assert 2 + 2 == 4, "Teste de soma falhou"
    assert 3 + 3 == 6, "Teste de soma falhou"

#escrevendo classes de teste
class TesteMultiplicacao:
    

    def setup(self):
        print("Configuração do teste")
        self.calculator = Calculator()
    
    def teardown(self):
        print("Limpeza após o teste")
        del self.calculator

    def teste_multiplicacao(self):
        assert 2 * 3 == 6, "Teste de multiplicação falhou"
        assert 4 * 5 == 20, "Teste de multiplicação falhou"
        assert 6 * 7 == 42, "Teste de multiplicação falhou"
    

#testando parametros usando pytest

import pytest
@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (10, 20, 15),
        (20, 30, 25),
        (5, 5, 5)
    ])
def teste_media(num1, num2, expected):
    assert (num1 + num2) / 2 == expected, "Teste de média falhou"