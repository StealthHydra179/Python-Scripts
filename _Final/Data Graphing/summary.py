# Purpose: This program compares the theoretical and experimental capacities of a battery at different temperatures.
# Theoretical capacities are calculated using the Nernst equation, integrated over a specific range, while experimental 
# capacities are derived from provided data. It visualizes the results by plotting theoretical and experimental values 
# on a graph and includes additional data on energy resistance and associated errors.

# Key Features:
# 1. **Theoretical Capacity Calculation**: Uses the scipy.integrate.quad function to compute the integral of the Nernst 
#    equation for various temperatures. The result is used to estimate the theoretical capacity.
# 2. **Experimental Data Analysis**: Includes additional data for energy resistance and error values at specific 
#    temperatures, allowing comparison with theoretical values.
# 3. **Visualization**: Uses matplotlib to create two graphs:
#    - Energy vs. Temperature (theoretical values).
#    - Energy × Resistance vs. Temperature with error bars (experimental data).

# Libraries Used:
# - numpy: For efficient numerical operations.
# - matplotlib: For creating graphs and visualizations.
# - scipy.integrate: For performing numerical integration using the quad function.

# Output: Graphs displaying theoretical energy values and experimental energy × resistance values, with error bars for clarity.


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Function to compute the integral
def integrand(r, x):
    return (1.1 - (8.314 * x) / (2 * 96485) * np.log(((0.001 + r) / (0.5 - r))**0.4599)) * 1929.7

# Function to perform the integration for a given x (temperature)
def compute_integral(x):
    result, _ = quad(integrand, 0, 0.5, args=(x,))
    return result

# Compute W for a range of x values (temperatures)
x_values = np.linspace(285, 335, 100)  # Temperature range between 285 K and 335 K
W_values = np.array([compute_integral(x) for x in x_values])

# Plot W vs. x
fig, ax1 = plt.subplots()

# Additional data for the second graph
additional_data = {
    'Temperature': [288, 293, 308, 318, 333],
    'Energy_Resistance': [4344.298947, 3572.269073, 2015.288052, 1015.608735, 275.762205],
    'Errors': [706.8, 217.2, 365.1, 192.2, 151.6]  # Error data
}

# Plot the first graph (Energy vs. Temperature)
ax1.plot(x_values, W_values, label='Energy (J)', color='green')
ax1.set_xlabel('Temperature (K)', fontsize=12)
ax1.set_ylabel('Energy (J)', color='green', fontsize=12)
ax1.tick_params(axis='y', labelcolor='green', labelsize=10)
ax1.tick_params(axis='x', labelsize=10)
ax1.set_xlim(285, 335)
ax1.ticklabel_format(useOffset=False)
ax1.set_ylim(1061.243, 1061.258)

# Plot the second graph (Energy * Resistance vs. Temperature)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.set_ylabel('Energy × Resistance (J·Ω)', color='blue', fontsize=12)  # we already handled the x-label with ax1
ax2.errorbar(additional_data['Temperature'], additional_data['Energy_Resistance'], yerr=additional_data['Errors'], xerr=3, label='Energy * Resistance (J * Ω)', color='blue', marker='o', capsize=5)
ax2.tick_params(axis='y', labelcolor='blue', labelsize=10)

# Legends
# ax1.legend(loc='upper left')
# ax2.legend(loc='upper right')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()