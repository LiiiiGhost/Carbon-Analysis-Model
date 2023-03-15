import numpy as np
import pandas as pd
import json

def generate_random_data(num_rows, start_date, end_date):
    dates = pd.date_range(start_date, end_date)
    values = np.random.randn(len(dates))
    data = {"date": dates.strftime("%Y-%m-%d").tolist(), "value": values.tolist()}
    with open("random_data.json", "w") as file:
        json.dump(data, file)
    print("Random data generated and saved to random_data.json")

if __name__ == '__main__':
    generate_random_data(1000, "2022-01-01", "2022-12-31")
