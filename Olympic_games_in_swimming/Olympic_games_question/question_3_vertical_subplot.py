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

    my_df = pd.DataFrame({'Team': [],
                          'Year': [],
                          'Stroke': [],
                          'Gender': [],
                          'Rank': [],
                          'Time_results': [], })

    # Dealing with the "Result" column - Define a lambda function to convert the time format
    convert_time = lambda x: ':'.join(x.split(':')[-2:])[:-3]

    # Apply the lambda function to the 'Time_results' column
    final_clean_table['Time_results'] = final_clean_table['Results'].apply(convert_time)

    gender_type = ['Men','Women']

    # Retrieving the data after  3 constraints:
    for gender in gender_type :
        final_table_by_gender = final_clean_table.loc[(final_clean_table["Relay?"] == 1) &
                                                      (final_clean_table['Gender'] == gender) &
                                                      (final_clean_table['Distance (in meters)'] == '4x100')]
        print('*')

        # I have added the list of years hard coded because - we are willing to present the two kinds of stroke : 'Medley' & 'Freestyle'
        years_list = [1964,1968,1972,1984,1988,1992,1996,2000,2004,2008,2012,2016]
        for olympic_year in years_list :

            mini_df_gender_year = final_table_by_gender[final_table_by_gender['Year'] == olympic_year] # men started only in 1960
            print('*')

            styles_of_swimming = ['Medley','Freestyle']
            for swimming_style in styles_of_swimming:

                mini_df_gender_year_style = mini_df_gender_year[mini_df_gender_year['Stroke'] == swimming_style ]
                print(mini_df_gender_year_style)

                first_3_places = [1, 2, 3]


                final_medals_table = mini_df_gender_year_style[mini_df_gender_year_style['Rank'].isin(first_3_places)]
                print('*')

            # relevent fields for the table
            relevent_fields = ['Team','Year','Stroke','Gender','Rank','Time_results']
            final_medals_table = final_medals_table.loc[:,relevent_fields]
            print('*')
            my_df = pd.concat([my_df, final_medals_table], axis=0)
            print('*')
            # in order to retrieve the name co the teams q countries how won the medals, we need to "reset_index" the table
            # final_medals_table = final_medals_table.reset_index()
            # final_medals_table
            # gold_annotation = final_medals_table.loc[1, 'Team']
            # time_gold_result = final_medals_table.loc[1, 'Time_results']
            #
            # silver_annotation = final_medals_table.loc[2, 'Team']
            # time_silver_result = final_medals_table.loc[2, 'Time_results']
            #
            # bronze_annotation = final_medals_table.loc[3, 'Team']
            # time_bronze_result = final_medals_table.loc[3, 'Time_results']

        print('*')



    return  my_df

# **************************************************************************************************************
# Function  name: creating_advance_line_chart
# input:
# return value: Converting  the values to seconds with two decimal place
# ****************************************************************************************************************
# def plotting_subplot_for_freestyle_vs_medley_relay():
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
    #plotting_subplot_for_freestyle_vs_medley_relay()
    print('*')




