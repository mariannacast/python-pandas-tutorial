import pandas as pd 

# Definir la serie
my_series = pd.Series([2, 4, 6, 8, 10])

# Aplicar una función para dividir cada valor por 2
result_series = my_series.apply(lambda x: x / 2)

# Imprimir el resultado
print(result_series)
