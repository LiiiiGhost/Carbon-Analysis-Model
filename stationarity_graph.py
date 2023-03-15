import numpy as np
import matplotlib.pyplot as plt

# Generate stationary data
np.random.seed(0)
stationary_data = np.random.normal(loc=0, scale=1, size=1000)
for i in range(1, 1000):
    stationary_data[i] += 0.95 * stationary_data[i-1]

# Generate non-stationary data
np.random.seed(1)
nonstationary_data = np.cumsum(np.random.normal(loc=0, scale=1, size=1000))

# Plot the data
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(stationary_data, color='green', label='Stationary Data')
ax.plot(nonstationary_data, color='blue', label='Non-Stationary Data')

# Set y-axis label
ax.set_ylabel('Value')

# Set the legend with a larger font size
ax.legend(fontsize='large')

plt.show()
