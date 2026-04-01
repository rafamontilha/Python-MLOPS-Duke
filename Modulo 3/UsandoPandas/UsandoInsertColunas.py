import pandas as pd

countries_data = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'],
          'continent' : ['Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'South America', 'Europe'],
          'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}

countries = pd.DataFrame(countries_data)
# a linha nova adiciona uma nova coluna chamada population, e os valores são passados em uma lista
countries['population'] = [66000000, 11000000, 39000, 430000, 9955000, 7252874, 1886212]
# a notação abaixo permite criar uma coluna e indicar o seu indice, o nome da coluna e os valores
countries.insert(1, 'area', [513120, 300000, 2.02, 316, 450295, 406750, 64589]) 
print(countries)

#exportando o dataframe para um arquivo csv
#countries.to_html('countries.html', index=False)

#para markdown
countries.to_markdown('countries.md', index=False)