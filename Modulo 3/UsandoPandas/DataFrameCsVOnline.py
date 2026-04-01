import pandas as pd

csv_url ="https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
df = pd.read_csv(csv_url, index_col = 0)
print(df.head(10))
