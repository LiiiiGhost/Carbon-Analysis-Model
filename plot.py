import json
import matplotlib.pyplot as plt

# load json file
with open('data.json', 'r') as f:
    data = json.load(f)

# extract 'date' and 'value' data
dates = [item['date'] for item in data]
values = [item['value'] for item in data]

# Plot the graph
plt.plot(dates, values)
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
