import random
import json
from datetime import datetime, timedelta

start_date = datetime(2022, 2, 7)
end_date = datetime(2022, 2, 9)
current_date = start_date
data = []




# Generate random data and corresponding time
while current_date <= end_date:
    data.append({'date': current_date.strftime("%Y-%m-%d %H:%M:%S"), 'value': random.random()})
    current_date += timedelta(minutes=1)

# Save data to a JSON file
with open("data.json", "w") as f:
    json.dump(data, f)
