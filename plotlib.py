import numpy as np
import matplotlib.pyplot as plt

# Initial values
n_values = []
alpha_values = []
m = 100  # initial table size
alpha_H = 0.75  # high load factor threshold

n = 70  # initial number of elements
n_max = 2000  # maximum value of n to plot

# Track how n and alpha change as n increases and m resizes
while n <= n_max:
    # Calculate load factor
    alpha = n / m
    n_values.append(n)
    alpha_values.append(alpha)
    
    # Check if we need to resize the table
    if alpha > alpha_H:
        m = n / .375  # double the table size after exceeding alpha_H
    
    n += 1  # increment number of elements

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, alpha_values, label=r'alpha(n)')
plt.axhline(y=alpha_H, color='r', linestyle='--', label=r'alpha_H = 0.75')
plt.xlabel('n (Number of Elements)')
plt.ylabel('alpha (Load Factor)')
plt.title('Load Factor alpha as a Function of Number of Elements n')
plt.legend()
plt.grid(True)
plt.show()
