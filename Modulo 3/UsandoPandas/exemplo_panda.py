import pandas as pd

#exemplo com lista de listas
dados = [[4, 5, 6], [7, 8, 9], [10, 11, 12]]

colunas = ['A', 'B', 'C']

index = ['Segunda', 'Terça', 'Quarta']

df = pd.DataFrame(data=dados, index=index, columns=colunas)
print(df)