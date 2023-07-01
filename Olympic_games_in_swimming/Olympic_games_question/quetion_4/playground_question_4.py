# import libraries
import matplotlib.pyplot as plt
import pandas as pd
from textwrap import wrap
#plt.style.use(['unhcrpyplotstyle','dotplot'])
import numpy as np
import matplotlib.pyplot as plt


# Generate sample data
np.random.seed(0)
x = np.random.randn(25)
y = np.random.randint(1, 33, size=25)

# Define the threshold for color differentiationrn, di
threshold = 12


# Assign colors based on the y-values
colors = np.where(y <= threshold, 'silver', 'navy')

# Create the dot plot
plt.scatter(x, y, c=colors)

# Customize the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Dot Plot with Color Differentiation')

# Show the plot
plt.show()







