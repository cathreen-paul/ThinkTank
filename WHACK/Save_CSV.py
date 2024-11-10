import pandas as pd 
import json

# Load JSON data from file
with open('data.json') as f:
    data = json.load(f)

# Extract the 'data' field which contains the array of records
df = pd.DataFrame(data['data'])

# Specify the columns order you want in the CSV
columns = ['name', 'city', 'learning_style', 'class', 'proficiency_level']

# Ensure the dataframe has the desired column order
df = df[columns]

# Convert the DataFrame to CSV
df.to_csv('output.csv', index=False)

