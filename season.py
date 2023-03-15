import json
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

def main():
    with open("new_UKI_DAI_DataEngineering_Discovery.json") as file:
        data = json.load(file)
        
    df = pd.DataFrame(data)
    df.set_index("date", inplace=True)
    df.index = pd.to_datetime(df.index)
    df = df.resample("D").mean()
    
    result = seasonal_decompose(df["value"], model="multiplicative")
    
    plt.figure(figsize=(10, 8))
    result.seasonal.plot()
    plt.title("Seasonality")
    plt.show()
    
    if np.abs(result.seasonal).mean() > 6 * np.abs(result.seasonal).std():
        seasonal_dates = df.loc[result.seasonal.abs() > 6 * result.seasonal.abs().std()].index.strftime("%Y-%m-%d %H:%M:%S").tolist()
        seasonal_values = df.loc[result.seasonal.abs() > 6 * result.seasonal.abs().std()]["value"].values.tolist()
        seasonal_data = [{"date": date, "value": value} for date, value in zip(seasonal_dates, seasonal_values)]
        with open("seasonal_data.json", "w") as file:
            json.dump(seasonal_data, file)
        print("Seasonality detected and saved to seasonal_data.json")
        print("Seasonality dates:", seasonal_dates)
        period = len(result.seasonal) / result.seasonal.abs().argmax()
        print("Seasonality period: {:.2f} days".format(period))
    else:
        print("No seasonality detected")

if __name__ == '__main__':
    main()
