
import pandas as pd

countries_data = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'],
          'continent' : ['Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'South America', 'Europe'],
          'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}

countries = pd.DataFrame(countries_data)
# a linha nova adiciona uma nova coluna chamada population, e os valores são passados em uma lista
countries['population'] = [66000000, 11000000, 39000, 430000, 9955000, 7252874, 1886212]
print(countries)