import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#for index,plot_name in (range(1,4,1),subplot_names):



# Create sample DataFrame
# data = {'A': [-1.23456, 2.34567, -3.45678, 4.56789],
#         'B': [-5.6789, 6.7890, -7.8901, 8.9012]}
# df = pd.DataFrame(data)
#
# # Function to format float values with two decimal places
# def format_float(value):
#     if isinstance(value, float):
#         return f'{value:.2f}'
#     return value
#
# # Function to color negative numbers in red
# def color_negative(value):
#     color = 'red' if value < 0 else 'black'
#     return f'color: {color}'
#
# # Apply formatting and styling to the DataFrame
# styled_df = df.style.applymap(format_float).applymap(color_negative)
#
# # Display the styled DataFrame
# styled_df





# Sample data for each subplot
categories = ['Category 1', 'Category 2', 'Category 3']
values1 = [15, 10, 8]
values2 = [12, 9, 24]
values3 = [18, 7, 11]
values4 = [14, 6, 9]
print('*')
# Create a figure and an array of axes for subplots
fig, all_4_axis = plt.subplots(nrows=1, ncols=4, figsize=(12, 4))

# Iterate over each axis and plot the horizontal bar chart
for i, ax in enumerate(all_4_axis):
    if i == 0:
        values = values1
    elif i == 1:
        values = values2
    elif i == 2:
        values = values3
    elif i == 3:
        values = values4

    ax.barh(categories, values)

    # Add values over the bars - annotation
    for j, v in enumerate(values):
        ax.text(v + 0.5, j, str(v), color='black', va='center')

    # Set labels and title for each subplot
    ax.set_xlabel('Values')
    ax.set_ylabel('Categories')
    ax.set_title(f'Subplot {i+1}')

# Adjust spacing between subplots
plt.tight_layout()

# Display the plot
plt.show()