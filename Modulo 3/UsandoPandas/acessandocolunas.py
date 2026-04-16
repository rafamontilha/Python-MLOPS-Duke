import pandas as pd

cars_data = {'model': ['audi A1', 'audi A6', 'audi A4', 'audi A3','audi A1'],
          'year': [2017, 2016, 2017, 2019, 2016],
          'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol'],
          'price': [12500, 16500, 16800, 17300, 13900]}

audi_cars = pd.DataFrame(cars_data)

# Write your code below
columns = audi_cars[['model', 'year', 'price']]

# Testing the result
print(columns)