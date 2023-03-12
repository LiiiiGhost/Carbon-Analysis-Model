import json
import pandas as pd
import numpy as np
import random

# Set up date range
start_date = '2021-01-01'
end_date = '2023-03-09'
dates = pd.date_range(start_date, end_date, freq='D')

# Create increasing trend for the first 1.5 years
end_date1 = pd.Timestamp('2022-06-17')
trend1 = np.linspace(106.4, 150, dates.get_loc(end_date1) + 1)
trend1 += np.random.uniform(-5, 5, trend1.shape)

# Create decreasing trend for the next 6 months
start_date2 = pd.Timestamp('2022-06-18')
end_date2 = pd.Timestamp('2022-12-21')
trend2 = np.linspace(150, 120, dates.get_loc(end_date2) - dates.get_loc(start_date2) + 1)
trend2 += np.random.uniform(-5, 5, trend2.shape)

# Create increasing trend for the last 2.5 months
start_date3 = pd.Timestamp('2022-12-22')
trend3 = np.linspace(120, 130, len(dates[dates.get_loc(start_date3):]))
trend3 += np.random.uniform(-2, 2, trend3.shape)

# Concatenate the trends
trends = np.concatenate([trend1, trend2, trend3])

# Create DataFrame
df = pd.DataFrame({'date': dates, 'value': trends})
df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Convert DataFrame to list of dictionaries
data = df.to_dict('records')

# Save data to JSON file
with open('carbon_emissions.json', 'w') as f:
    json.dump(data, f)
