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
    # df = pd.read_csv('/home/shay_diy/PycharmProjects/Olympic_games/data/Olympic_Swimming.csv')
    print('*')

    im = image.imread('C:\Users\Gil\PycharmProjects\Olympic_games_in_swimming_1\Olympic_games_in_swimming\Olympic_games_question\question_1\Cleveland_dot_plot_AUS.jpg')

    fig, ax = plt.subplots()
    ax.grid()
    #ax.plot('Year','earnings ($ million)',data=lebron_james)
    ax.set_title("LeBron James earnings in US$(millions)")
    fig.figimage(im, 60, 40,cmap='ocean', alpha=.2)
    plt.show()
    plt.figimage(im, xo=1000, yo=135)



    #img = plt.imread("C:\Users\Gil\PycharmProjects\Olympic_games_in_swimming_1\Olympic_games_in_swimming\Olympic_games_question\question_7\swimming_pool_image.png")
    print('*')
