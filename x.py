import json

# Read the JSON file
with open("data.json", "r") as f:
    data = json.load(f)

# Store the data in a list of dictionaries
list = []
for item in data:
    list.append({'date': item['date'], 'value': item['value']})

