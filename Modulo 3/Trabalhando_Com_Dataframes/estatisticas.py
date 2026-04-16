import pandas as pd

wine_data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv')

# Write your code below
residual_sugar_mean = wine_data['residual sugar'].mean()
fixed_acidity_mode = wine_data['fixed acidity'].mode()[0]
described_data = wine_data.describe()

# Testing the result
print(f"Residual sugar mean: {residual_sugar_mean}")
print(f"Fixed acidity mode: {fixed_acidity_mode}")
print(described_data)

