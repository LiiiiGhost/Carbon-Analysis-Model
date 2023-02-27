import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

# Read data
with open('upward_trend.json', 'r') as f:
    data = json.load(f)

# Extract data
df = pd.DataFrame(data)
df = df[['date', 'value']]

# Convert date column to timestamp
df['date'] = pd.to_datetime(df['date'])

# Set timestamp as index
df.set_index('date', inplace=True)

# Fill missing values with previous day's data
df.fillna(method='ffill', inplace=True)

# Normalize data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df)

# Define function to create training data
def create_train_data(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i+look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

# Create training data
look_back = 30
X_train, Y_train = create_train_data(scaled_data, look_back)

# Reshape input data to 3D
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Create LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Train model
model.fit(X_train, Y_train, epochs=100, batch_size=32)

# Predict daily data for next 6 months
last_date = df.index[-1]
prediction_dates = pd.date_range(last_date, periods=180, freq='D')
prediction_data = np.empty((180, 1))
prediction_data[0:look_back] = scaled_data[-look_back:]

for i in range(look_back, 180):
    x_input = prediction_data[(i-look_back):i, 0]
    x_input = np.reshape(x_input, (1, look_back, 1))
    yhat = model.predict(x_input)
    prediction_data[i] = yhat

# Inverse normalization
prediction_data = scaler.inverse_transform(prediction_data)

# Generate dates and values for predictions
predictions = pd.DataFrame(prediction_data, index=prediction_dates, columns=['value'])

# Calculate RMSE
train = df.iloc[:-180]
test = df.iloc[-180:]
test['predictions'] = predictions
rmse = np.sqrt(np.mean((test['value'] - test['predictions'])**2))
print('RMSE:', rmse)

# Generate new JSON file to store data
predictions.reset_index(inplace=True)
predictions.rename(columns={'index': 'date'}, inplace=True)
predictions['date'] = predictions['date'].dt.strftime('%Y-%m-%d')
predictions_json = predictions.to_dict('records')

with open('co2_emissions_predictions.json', 'w') as f:
    json.dump(predictions_json, f)
