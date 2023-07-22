import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Step 1: Prepare the bar chart data and labels
data = [10, 12, 15, 14, 12, 18]
#labels = ['Bar 1', 'Bar 2', 'Bar 3', 'Bar 4', 'Bar 5', 'Bar 6']
x = [0,1, 2, 3, 4, 5]

# Step 2: Prepare the small images (Replace 'image1.png', 'image2.png', and 'image3.png' with your actual image file paths)
image_paths = ['beijig_2008.png', 'london_2012.png', 'sydney_2000.png','stockholm_1956.png','tokyo_2020.png','los_angeles_1984.png']
images = [plt.imread(path) for path in image_paths]

plt.figure(facecolor='gainsboro')
# Step 3: Create the bar chart
#plt.bar(range(len(data)), data, tick_label=labels)

# Step 4: Add the images under each bar
for i, image in enumerate(images):
    imagebox = OffsetImage(image, zoom=0.45)  # Adjust the 'zoom' parameter to scale the image size
    ab = AnnotationBbox(imagebox, (i, 0), xybox=(0, -60), xycoords='data', boxcoords="offset points", frameon=False)
    plt.gca().add_artist(ab)



fontdict_input = {'fontsize': 16, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'White'}
#bar plot
plt.bar(x, height = data, width = 0.6)

# Set the title and labels for the chart
plt.title("Number of medals with home court advantage",fontsize=21,weight='bold', fontname='Franklin Gothic Medium Cond')
#plt.xlabel("Home Court")
plt.ylabel("Values")


# Show the plot
plt.show()




