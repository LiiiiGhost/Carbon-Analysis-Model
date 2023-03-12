import pandas as pd
from statsmodels.tsa.stattools import adfuller

def get_d_value (past_emissions):
    # Convert the data to a DataFrame
    data = pd.DataFrame(past_emissions)

    # Convert the JSON data to a DataFrame
    df = pd.DataFrame(data)

    # Convert the 'date' column to date format and set it as the index
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    # Function to calculate the difference order
    def difference_order(series):
        result = adfuller(series)
        difference_order = 0
        while result[1] < 0.05:
            difference_order += 1
            series = series.diff().dropna()
            result = adfuller(series)
        return difference_order

    # Calculate the difference order
    difference_order = difference_order(df['value'])
    return difference_order

'''
print("The difference order is:", difference_order)
'''