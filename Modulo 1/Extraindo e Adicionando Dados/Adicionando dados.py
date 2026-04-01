#definindo uma lista vazia
lista_de_compras = []
lista_de_compras

#append adiciona um item ao final da lista
lista_de_compras.append('leite')
lista_de_compras.append('pão')
lista_de_compras

#similar ao append, podemos usar o insert para adicionar um item em uma posição específica
lista_de_compras.insert(0, 'manteiga')
lista_de_compras

#podemos adicionar uma lista a outra 
outras_compras = ['queijo', 'presunto']
lista_de_compras + outras_compras
lista_de_compras

#é possivel inserir uma lista dentro de outra usando append
compras_exemplo =['frutas', 'verduras']
lista_de_compras.append(compras_exemplo)
lista_de_compras

#podemos extender uma lista com o comando extend

lista_de_compras.extend(compras_exemplo)
lista_de_compras