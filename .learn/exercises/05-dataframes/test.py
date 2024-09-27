import pandas as pd 
#. Three-dimensional array of [Brand, Model, Color] values 
data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]

# Create the DataFrame and name the columns
df = pd.DataFrame(data, columns= ['Brand', 'Model', 'Color'])

# Print the DataFrame 
print(df)