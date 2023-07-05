import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns



if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    # df = pd.read_csv('/home/shay_diy/PycharmProjects/Olympic_games/data/Olympic_Swimming.csv')
    print('*')

    img = plt.imread("C:\Users\Gil\PycharmProjects\Olympic_games_in_swimming_1\Olympic_games_in_swimming\Olympic_games_question\question_7\swimming_pool_image.png")
    print('*')
