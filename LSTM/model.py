import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.callbacks import EarlyStopping

"""
This code reads carbon emissions data from a JSON file, pre-processes the data and uses it to train an LSTM model to predict future carbon emissions. The prediction results are then saved to a new JSON file.

The code performs the following steps.

    Reads the data from the JSON file and extracts the relevant columns.
    Converts the date column to a timestamp and uses it as an index.
    Interpolates the missing data to fill in the gaps in the time series.
    Normalise the data using the MinMaxScaler from the sklearn library.
    Define a function to create the training data for the LSTM model.
    Create the training data by calling the function and specifying a 90-day look-back window.
    Reshape the input data into three dimensions to fit the LSTM model.
    Define a three-layer LSTM model with 128 cells per layer and compile it using the Adam optimiser and mean error loss.
    Set early stops to prevent over-fitting.
    Train the LSTM model using the training data, a validation split of 0.1 and an early stop callback.
    Use the trained LSTM model to predict daily carbon emissions for the next 3 months.
    Reverse normalise the predictions to obtain the actual carbon emission values.
    Calculate the root mean square error between the predicted and actual carbon emission values for the test set.
    Save the predicted carbon emission values to a new JSON file.

"""

# Read data
with open('sine_carbon_emissions.json', 'r') as f:
    data = json.load(f)

# Extract data
df = pd.DataFrame(data)
df = df[['date', 'value']]

# Convert date column to timestamp
df['date'] = pd.to_datetime(df['date'])

# Set timestamp as index
df.set_index('date', inplace=True)

# Interpolate missing data
df = df.interpolate()

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
look_back = 90
train_data = scaled_data[:-90]
X_train, Y_train = create_train_data(train_data, look_back)

# Reshape input data to 3D
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

# Create LSTM model
model = Sequential()
model.add(LSTM(units=128, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(units=128, return_sequences=True))
model.add(LSTM(units=128))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Set up early stopping
early_stop = EarlyStopping(monitor='val_loss', patience=10)

# Train model
model.fit(X_train, Y_train, epochs=150, batch_size=64, validation_split=0.1, callbacks=[early_stop])

# Predict daily data for next 3 months
last_date = df.index[-1]
prediction_dates = pd.date_range(last_date, periods=90, freq='D')
prediction_data = np.empty((90, 1))
prediction_data[0:look_back] = scaled_data[-look_back:]

for i in range(look_back, 90):
    x_input = prediction_data[(i-look_back):i, 0]
    x_input = np.reshape(x_input, (1, look_back, 1))
    yhat = model.predict(x_input)
    prediction_data[i] = yhat

# Inverse normalization
prediction_data = scaler.inverse_transform(prediction_data)

# Generate dates and values for predictions
predictions = pd.DataFrame(prediction_data, index=prediction_dates, columns=['value'])

# Calculate Root Mean Square Error
train = df.iloc[:-90]
test = df.iloc[-90:]
test['predictions'] = predictions[:90]
rmse = np.sqrt(np.mean((test['value'] - test['predictions'])**2))
print('RMSE:', rmse)

# Generate new JSON file to store data
predictions.reset_index(inplace=True)
predictions.rename(columns={'index': 'date'}, inplace=True)
predictions['date'] = predictions['date'].dt.strftime('%Y-%m-%d')
predictions_json = predictions.to_dict('records')

with open('co2_emissions_predictions.json', 'w') as f:
    json.dump(predictions_json, f)
