# import libraries
import matplotlib.pyplot as plt
import pandas as pd
from textwrap import wrap
#plt.style.use(['unhcrpyplotstyle','dotplot'])
import numpy as np
import matplotlib.pyplot as plt

#
# # Generate sample data
# np.random.seed(0)
# x = np.random.randn(25)
# y = np.random.randint(1, 33, size=25)
#
# # Define the threshold for color differentiationrn, di
# threshold = 12
#
#
# # Assign colors based on the y-values
# colors = np.where(y <= threshold, 'silver', 'navy')
#
# # Create the dot plot
# plt.scatter(x, y, c=colors)
#
# # Customize the plot
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Dot Plot with Color Differentiation')
#
# # Show the plot
# plt.show()


# Create some example data
x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 6, 4]

# Create the plot
plt.plot(x, y)

# Add the horizontal line from x=5 to x=10
plt.axhline(y=5, xmin=0.5, xmax=0.8, color='blue')

# Set the x-axis limits
plt.xlim(0, 10)

# Show the plot
plt.show()





