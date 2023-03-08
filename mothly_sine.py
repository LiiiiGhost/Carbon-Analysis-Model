import json
import pandas as pd
import numpy as np

# Define function to create Sine wave data
def create_sine_wave(length, amplitude, period):
    x = np.arange(length)
    y = amplitude * np.sin(2 * np.pi * x / period)
    return y

# Define start and end dates
start_date = '2022-06-01'
end_date = '2022-12-31'

# Create date range
date_range = pd.date_range(start_date, end_date)

# Define Sine wave parameters
amplitude = 50
period = 30

# Generate Sine wave data for each month
data = []
for month in range(6, 13):
    # Filter dates for current month
    dates = [d for d in date_range if d.month == month]
    # Generate Sine wave data
    values = create_sine_wave(len(dates), amplitude, period)
    # Scale values to range [100, 200]
    values = (values - np.min(values)) / (np.max(values) - np.min(values)) * 100 + 100
    # Add date-value pairs to data list
    for date, value in zip(dates, values):
        data.append({'date': date.strftime('%Y-%m-%d'), 'value': round(value, 2)})

# Write data to JSON file
with open('monthly_sine_carbon_emissions.json', 'w') as f:
    json.dump(data, f)
