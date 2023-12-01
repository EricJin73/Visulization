"""
Created on Sun Nov 12 19:09:22 2023

@author: Jinyu
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.size"] = 14
plt.rcParams["font.sans-serif"] = 'Times New Roman'
plt.rcParams["font.weight"] = 'bold'

# Data input
data = pd.read_excel(r'data_example.xlsx')

# Convert to polar coodinates
N = 12
enddata = 2*np.pi
theta = np.linspace(0, enddata, N, endpoint=False)
radii_a = data['a']
radii_b = data['b']
radii_c = data['c']
width = enddata / N
alpha = 1
#colors = plt.cm.viridis_r(radii / 36)

# Draw
fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111, projection='polar')
bars_c = ax.bar(theta, radii_c, width=width, bottom=0.0, color='#0051A3', alpha=alpha, edgecolor='#0051A3', label='c')
bars_b = ax.bar(theta, radii_b, width=width, bottom=0.0, color='#0191C6', alpha=alpha, edgecolor='#0191C6', label='b')
bars_a = ax.bar(theta, radii_a, width=width, bottom=0.0, color='#67BFC1', alpha=alpha, edgecolor='#67BFC1', label='a')

# Remove grids
ax.spines['polar'].set_visible(False)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(False)

# Set direction
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

# Set legend
#ax.legend(loc='upper right', frameon=True, edgecolor='black')

# Picture output
plt.tight_layout()
plt.show()
