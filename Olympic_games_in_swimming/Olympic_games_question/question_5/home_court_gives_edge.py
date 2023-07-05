import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# **************************************************************************************************************
# Function  name:
# input: How home field advantage gives O;ympic hpst countries an Edge?
# return value:
# ****************************************************************************************************************


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    # df = pd.read_csv('/home/shay_diy/PycharmProjects/Olympic_games/data/Olympic_Swimming.csv')
    print('*')

    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]




