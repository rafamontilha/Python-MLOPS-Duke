import pandas as pd

cars_data = {
    'Marca': ['Toyota', 'Honda', 'Ford', 'Chevrolet'],
    'Modelo': ['Camry', 'Civic', 'Focus', 'Silverado'],
    'Ano': [2020, 2019, 2021, 2020]
}

relaciona_carros = pd.DataFrame(cars_data)
print(relaciona_carros)
relaciona_carros = relaciona_carros.drop(columns=['Ano'])
print(relaciona_carros)