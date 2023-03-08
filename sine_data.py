import json
import numpy as np
import pandas as pd

# Generate date range
start_date = '2017-01-01'
end_date = '2022-12-31'
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Generate sine wave data
amplitude = 50
period = 365
offset = 150
sine_data = amplitude * np.sin(2 * np.pi / period * np.arange(len(date_range))) + offset
sine_data = np.clip(sine_data, 100, 200) # Clip values between 100-200

# Create dataframe and store as JSON
df = pd.DataFrame({'date': date_range, 'value': sine_data})
df['date'] = df['date'].dt.strftime('%Y-%m-%d')
json_data = df.to_dict('records')

with open('sine_carbon_emissions.json', 'w') as f:
    json.dump(json_data, f)
