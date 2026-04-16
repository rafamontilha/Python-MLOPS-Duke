import pandas as pd

countries_data = {'country' : ['Thailand', 'Philippines', 'Monaco', 'Malta', 'Sweden', 'Paraguay', 'Latvia'], 'continent' : ['Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'South America', 'Europe'], 'capital':['Bangkok', 'Manila', 'Monaco', 'Valletta', 'Stockholm', 'Asuncion', 'Riga']}
countries = pd.DataFrame(countries_data)
print(countries)

print(countries.iloc[0])
print(countries.iloc[2])