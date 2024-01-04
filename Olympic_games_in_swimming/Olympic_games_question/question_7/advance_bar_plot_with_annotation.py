import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import PIL
import matplotlib.image as image
import seaborn


def preparing_the_data(final_table):
    print('*')
    final_table_counter = final_table['Athlete'].value_counts()
    final_table_counter = final_table_counter.reset_index()
    final_table_counter.rename(columns={"Athlete": 'Athlete_Name', "count": 'Number_of_madels'},inplace=True)


    return final_table_counter


def adding_advance_bar_plot(final_table_counter, Gender_Athlete):

    plt.figure(figsize=(12, 7))
    result_table = final_table_counter["Number_of_madels"].value_counts().reset_index()
    result_table= result_table.iloc[2:7]

    #rank = result_table.argsort().argsort() # TODO: need to check it out in order to have a  gradient chart
    number_of_athletes_with_the_same_num_of_medals = list(result_table.loc[:,'count'])
    number_of_madels = list(result_table.loc[:,'Number_of_madels'])

    print('*')
    pal = sns.color_palette("Greens_d", len(number_of_madels))

    plt.bar(number_of_madels, number_of_athletes_with_the_same_num_of_medals, width=0.9, align='center', color='cyan', edgecolor='black')
    #sns.barplot(x=number_of_madels, y=number_of_athletes_with_the_same_num_of_medals, palette=np.array(pal[::-1])[rank])

    plt.savefig(f'gradient_bar_plot_{Gender_Athlete}.jpg', dpi=250, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')

    #    df = pd.read_csv('/home/shay_diy/PycharmProjects/Olympic_games/data/Olympic_Swimming.csv')

    first_3_places = [1, 2, 3]
    final_medals_table = df[df['Rank'].isin(first_3_places)]

    Gender = ['Men','Women']
    for Gender_Athlete in Gender :
        final_table = final_medals_table.loc[(final_medals_table['Gender'] == Gender_Athlete)]
        res = preparing_the_data(final_table)
        adding_advance_bar_plot(res, Gender_Athlete )
        print('*')

