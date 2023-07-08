import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import PIL
import matplotlib.image as image


# The number of  time each team to broke the olympic record over the years

list_of_teams_names =['USA','AUS','GBR','JPN','GER','CAN','GDR','HUN']

#  Do_like_here :  https://parulpandey.com/2020/08/04/advanced-plots-in-matplotlib%E2%80%8A-%E2%80%8Apart-1/
if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')

    print('*')

####################################################################################################################################################################

# Reading image using imread
image = plt.imread("C:/Users/Gil/PycharmProjects/Olympic_games_in_swimming_1/Olympic_games_in_swimming/Data/swimming_pool_photo.png")

# Create a sample dataset
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'earnings ($ million)': [100, 150, 200, 180, 220]}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

ax.grid()
ax.barh('Year', 'earnings ($ million)', data=df,color ='black')  # Use barh for horizontal bar plot

ax.set_xlabel('Earnings ($ million)')
ax.set_ylabel('Swimming Teams')

ax.set_title("LeBron James earnings in US$ (millions)")
fig.figimage(image, 50, 50, cmap='ocean', alpha=0.55)
plt.show()

# Displaying the read image
plt.imshow(image)