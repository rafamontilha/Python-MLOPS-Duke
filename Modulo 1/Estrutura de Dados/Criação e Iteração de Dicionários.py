#instanciando um dicionário vazio
import os


meu_dicionario = {}
meu_dicionario

#incrementando o dicionário com chaves e valores
meu_dicionario={'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
meu_dicionario

#com o método dict()

meu_dicionario = dict()
meu_dicionario

#com dict() e passando lista de tuplas
meu_dicionario = dict([('nome', 'Maria'), ('idade', 25), ('cidade', 'Rio de Janeiro')])
dict(meu_dicionario)

#dict com palavras-chave
meu_dicionario = dict(nome='Carlos', idade=32, cidade='Belo Horizonte')
meu_dicionario

#loop para iterar sobre chaves e valores de um dicionário   

contact_informations = {'nome': 'Ana', 'telefone': '123456789', 'email': 'ana@email.com'}

#retornar apenas keys
for key in contact_informations.keys():
    print(key)

#retornar apenas values
for value in contact_informations.values():
    print(value)

#retornar keys e values
for key, value in contact_informations.items():
    print(f'{key}: {value}')

#tuplas servem apenas para leitura, não podem ser modificadas
my_tuple = ('primeiro', 'segundo', 'terceiro')
print("Primeiro item da tupla é %s" % my_tuple.index('primeiro')) #primeiro
print(my_tuple[-1]) #terceiro
for iten in my_tuple:
    print(iten)

#descobrindo méttodos disponiveis em uma tupla
for method in dir(tuple):
    if method.startswith('_'):
       continue
    print(method)

#criando sets com chaves únicas

unique = set()
unique.add('SFO')
unique

unique.add('LAX')
unique.add('SFO') #não é adicionado, pois já existe
unique.add('ORD')
unique
    
directories = ['Documents', 'Music', 'Desktop', 'Downloads', 'Pictures', 'Movies']
for directory in directories:
 print(directory)

for item in os.listdir('.'):
    if os.path.isdir(item):
        print(item)