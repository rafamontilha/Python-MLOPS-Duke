#aprendizado 1 - atribuição direta

lista_telefonica = {}
lista_telefonica["Rafael"] = {"nome": "Rafael", "telefone": "123456789"}
lista_telefonica["Mariana"] = {"nome": "Mariana", "telefone": "987654321"}



#criando lista telefonica com dicionários
lista_telefonica = {}
contato = {"nome": "Rafael", "telefone": "123456789"}
lista_telefonica["Rafael"] = contato
contato = {"nome": "Mariana", "telefone": "987654321"}
lista_telefonica["Mariana"] = contato
for nome, contato in lista_telefonica.items():
    print(f'Nome: {contato["nome"]}, Telefone: {contato["telefone"]}')


