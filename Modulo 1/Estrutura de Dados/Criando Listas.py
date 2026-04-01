#criamos uma lista vazia
minha_lista = []
minha_lista 
#criamos uma lista com alguns itens
outra_lista = [1, 2, 3, 4, 5]

#podemos acessar todos os itens de uma lista usando um loop for
for item in outra_lista:
    print(item)

#podemos usar a função for para acessar itens em uma lista usando seus índices
numbers = [10, 20, 30, 40, 50]
low_numbers = [n for n in numbers if n < 30] #list comprehension para criar nova lista
print(low_numbers) # [10, 20]