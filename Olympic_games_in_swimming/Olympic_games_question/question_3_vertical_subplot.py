import matplotlib.pyplot as plt
import pandas as pd

# **************************************************************************************************************
# Function  name: prepering_the_data_for_vertical_subplots
# input:
# return value: Converting  the values to seconds with two decimal place
# ****************************************************************************************************************
def prepering_the_data_for_vertical_subplots(df):
    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]
    # Retrieving the 2 data for male & female separately - after 3 constraints:
    final_table_male = final_clean_table.loc[
        (final_clean_table["Relay?"] == 1) & (final_clean_table['Gender'] == 'Men') & (
                final_clean_table['Distance (in meters)'] == '4x100')]
    final_table_female = final_clean_table.loc[
        (final_clean_table["Relay?"] == 1) & (final_clean_table['Gender'] == 'Women') & (
                final_clean_table['Distance (in meters)'] == '4x100')]
    print('*')
    final_table_female_sorted = final_table_female['Year'].unique().tolist()
    sorted_years_list = sorted(final_table_female_sorted, reverse=False)
    print('*')
    for olympic_year in sorted_years_list:
        # mini_df_men = final_table_male[final_table_male['Year'] == olympic_year] # men started only in 1960
        mini_df_women = final_table_female[final_table_female['Year'] == olympic_year]
        first_3_places = [1, 2, 3]
        final_women_table = mini_df_women[mini_df_women['Rank'].isin(first_3_places)]
        final_women_table = final_women_table.reset_index()

        gold_annotation = final_women_table.loc[1, 'Team']
        silver_annotation = final_women_table.loc[2, 'Team']
        bronze_annotation = final_women_table.loc[3, 'Team']
        print('*')


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

    all_4_axis[0].barh(['Bronze', 'Silver', 'Gold'], [2026493, 710887, 476658], color='Gray')  # width
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

    prepering_the_data_for_vertical_subplots(df)
    # plotting_subplot_for_freestyle_vs_medley_relay()
    print('*')


