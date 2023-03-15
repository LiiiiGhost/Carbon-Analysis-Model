import matplotlib.pyplot as plt
import numpy as np

# Generate data for case 1
x = np.linspace(0, 1, 101)
A1 = np.sin(2 * np.pi * x) + 1
B1 = -A1 + 2

# Generate data for case 2
A2 = np.sin(2 * np.pi * x) + 1
B2 = -A2 + 3

# Create two subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Plot case 1
axs[0].plot(x, A1, color='red')
axs[0].plot(x, B1, color='green')
axs[0].set_title('Case 1: correlation coefficient +1')
axs[0].set_ylabel("Amplitude")

# Plot case 2
axs[1].plot(x, A2, color='red')
axs[1].plot(x, B2, color='green')
axs[1].set_title('Case 2: correlation coefficient -1')
axs[1].set_ylabel("Amplitude")

# Show the plots
plt.show()
