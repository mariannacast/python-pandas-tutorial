import pandas as pd 

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')

# solo imprimir las columnas 'Name' y 'Type 1'
print(data_frame[['Name', 'Type 1']] [0:10])