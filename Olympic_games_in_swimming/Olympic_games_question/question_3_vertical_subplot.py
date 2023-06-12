import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import numpy as np




# **************************************************************************************************************
# Function  name: creating_advance_line_chart
# input:
# return value: Converting  the values to seconds with two decimal place
# ****************************************************************************************************************
def plotting_subplot_for_freestyle_vs_medley_relay():

    plt.figure(figsize=[14, 10])
    fig, all_4_axis = plt.subplots(nrows=1, ncols=4, sharey=True)  # 4 plots
    # plt.style.use('ggplot')
    # for index in range(1,4,1):
    all_4_axis[0].set_title('Men', fontsize=14, fontname='Franklin Gothic Medium Cond')
    all_4_axis[1].set_title('Women', fontsize=14, fontname='Franklin Gothic Medium Cond')
    all_4_axis[2].set_title('Men', fontsize=14, fontname='Franklin Gothic Medium Cond')
    all_4_axis[3].set_title('Women', fontsize=14, fontname='Franklin Gothic Medium Cond')

    all_4_axis[0].barh(['Bronze', 'Silver', 'Gold'], [2026493, 710887, 476658], color='Gray') # width
    all_4_axis[1].barh(['Bronze', 'Silver', 'Gold'], [2026493, 710887, 476658], color='Gray')
    all_4_axis[2].barh(['Bronze', 'Silver', 'Gold'], [2026493, 710887, 476658], color='Gray')
    all_4_axis[3].barh(['Bronze', 'Silver', 'Gold'], [2026493, 710887, 476658], color='Gray')

    plt.xlabel('Time', fontsize=18)
    plt.xticks(fontsize=18)
    plt.suptitle('Freestyle VS Medley Relay', fontweight="bold", fontsize=25, fontname='Franklin Gothic Medium Cond')
    # plt.savefig('2BarPlot.png')
    plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../Data/Olympic_Swimming_1912to2020.csv')

    #plotting_subplot_for_freestyle_vs_medley_relay()
    print('*')

    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]

    # Retrieving the 2 data for male & female separately - after 3 constraints:
    final_table_male = final_clean_table.loc[(final_clean_table["Relay?"] == 1) & (final_clean_table['Gender'] == 'Men') & (final_clean_table['Distance (in meters)'] == '4x100')]
    final_table_female = final_clean_table.loc[(final_clean_table["Relay?"] == 1) & (final_clean_table['Gender'] == 'Women') & (final_clean_table['Distance (in meters)'] == '4x100')]
    print('*')

    final_table_female_sorted= final_table_female['Year'].unique().tolist()
    #np.sort(final_table_female_sorted, axis=-1, kind=None, order=None)

    #for olympic_year in final_table_female_sorted
