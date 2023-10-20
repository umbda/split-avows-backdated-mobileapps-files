import pandas as pd

# Load the CSV file into a DataFrame
input_csv = 'input.csv'
df = pd.read_csv(input_csv)

# Assuming the date column is named 'date_column' in the CSV file
date_column = 'date_column'

# Group the DataFrame by the date column
grouped = df.groupby(date_column)

# Iterate through the groups and save each group to a separate CSV file
for name, group in grouped:
    output_csv = f'output_{name}.csv'
    group.to_csv(output_csv, index=False)