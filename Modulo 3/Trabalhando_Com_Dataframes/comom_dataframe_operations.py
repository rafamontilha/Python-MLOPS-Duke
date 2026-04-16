#Você recebe um DataFrame chamado wine_data.
#Obtenha o comprimento desse DataFrame antes de remover os valores nulos e atribua o resultado à variável length_before.
#Remova as linhas com valores nulos e armazene o DataFrame resultante em wine_data.
#Obtenha o comprimento de wine_data após remover os valores nulos e atribua o resultado à variável length_after.

import pandas as pd

wine_data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine_with_nan.csv')

length_before = len(wine_data)

wine_data = wine_data.dropna()

length_after = len(wine_data)

print(length_before)
print(length_after)