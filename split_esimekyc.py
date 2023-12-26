import pandas as pd
from datetime import datetime, timedelta

# Load the CSV file into a DataFrame
input_csv = 'dailyesim_ekyc_20231129_20231219.csv'
df = pd.read_csv(input_csv, dtype=object)

# Extract the day from the 'Timestamp' column
df['day'] = pd.to_datetime(df['Ekyc Timestamp']).dt.date

# Group the DataFrame by the day column
grouped = df.groupby('day')

# Iterate through the groups and save each group to a separate CSV file
for date, group in grouped:
    # Add 1 day to the date
    new_date = date + timedelta(days=1)
    # Convert date back to string
    new_date_str = new_date.strftime('%Y%m%d')
    output_csv = f'dailyesim_ekyc_{new_date_str}999999.csv' ####update parameter here too!
    group = group.drop('day', axis=1)
    group.to_csv(output_csv, index=False, quoting=1)