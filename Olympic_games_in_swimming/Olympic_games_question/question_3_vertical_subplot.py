import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# **************************************************************************************************************
# Function  name: prepering_the_data_for_vertical_subplots
# input:
# return value: Converting  the values to seconds with two decimal place
# ****************************************************************************************************************
def prepering_the_data_for_vertical_subplots(mini_df_year):

    # # Dealing with the column 'Rank' and 'Year'
    mini_df_year['Rank'] = mini_df_year['Rank'].apply(lambda x:int(x))
    mini_df_year['Year'] = mini_df_year['Year'].apply(lambda x:int(x))
    print('*')
    my_df = pd.DataFrame({'Team': [],
                          'Year': [],
                          'Stroke': [],
                          'Gender': [],
                          'Rank': [],
                          'Time_results': [],
                          'Location':[]})

    men_df_each_year = pd.DataFrame()  # Initialize an empty dataframe for men
    women_df_each_year = pd.DataFrame()  # Initialize an empty dataframe for women


# Dealing with the "Result" column - Define a lambda function to convert the time format
    convert_time = lambda x: ':'.join(x.split(':')[-2:])[:-3]

    # Apply the lambda function to the 'Time_results' column
    mini_df_year['Time_results'] = mini_df_year['Results'].apply(convert_time)

    gender_type = ['Men','Women']
    # Retrieving the data after  3 constraints:
    for gender in gender_type :
        mini_df_year_gender = mini_df_year.loc[(mini_df_year["Relay?"] == 1) & #Relay means 'Medley' or 'Freestyle'
                                                      (mini_df_year['Gender'] == gender) &
                                                      (mini_df_year['Distance (in meters)'] == '4x100')]

        # Another filter - 3 first place
        first_3_places = [1, 2, 3]

        final_medals_table = mini_df_year_gender[mini_df_year_gender['Rank'].isin(first_3_places)]
        print('*')
        relevent_fields = ['Team','Year','Stroke','Gender','Rank','Time_results', 'Location']
        final_medals_table = final_medals_table.loc[:,relevent_fields]


        if gender == 'Men':
            men_df_each_year = pd.concat([men_df_each_year, final_medals_table], axis=0)
        else:
            women_df_each_year = pd.concat([women_df_each_year, final_medals_table], axis=0)

    print('*')

    return  men_df_each_year,women_df_each_year

# **************************************************************************************************************
# Function  name: creating_advance_line_chart
# input:
# return value: Converting  the values to seconds with two decimal place
# ****************************************************************************************************************
def plotting_subplot_for_freestyle_vs_medley_relay(men_df_year,women_df_year):

    print('*')


    subtitle_year= men_df_year.loc[:,'Year'].unique()
    subtitle_location = men_df_year.loc[:,'Location'].unique()
    print(subtitle_year)

    styles_of_swimming = ['Medley', 'Freestyle']
    for swimming_style in styles_of_swimming:
        for gender, df_year in [('Men', men_df_year), ('Women', women_df_year)]:
            mini_df_style = df_year[df_year['Stroke'] == swimming_style]
            print('*')
            # In order to retrieve the name of the teams that won the medals, we need to "reset_index" the table
            mini_df_style = mini_df_style.reset_index()
            team_gold_annotation = mini_df_style.loc[0, 'Team']
            time_gold_result = mini_df_style.loc[0, 'Time_results']

            team_silver_annotation = mini_df_style.loc[1, 'Team']
            time_silver_result = mini_df_style.loc[1, 'Time_results']

            team_bronze_annotation = mini_df_style.loc[2, 'Team']
            time_bronze_result = mini_df_style.loc[2, 'Time_results']


            subplot_names = ['Men - Medley','Women - Medley','Men - Freestyle','Women - Freestyle']
            print('*')


            plt.figure(figsize=[14, 10])
            #Set one size for all subplots
            fig, all_4_axis = plt.subplots(nrows=1, ncols=4, sharey=True,  figsize=(16,4))  # 4 plots
            # Set individual sizes for specific subplots
            #fig, all_4_axis = plt.subplots(nrows=1, ncols=4,  gridspec_kw={'width_ratios': [16, 4]})

            #plt.style.use('ggplot')

            # Iterate over subplots and plot horizontal bars
            # for ax, val in zip(all_4_axis, values):
            #     ax.barh(categories, [val] * 4, height=0.1)  # Adjust the height parameter as desired

            for index,plot_name in zip(np.arange(0,4,1),subplot_names):
                all_4_axis[index].set_title(plot_name, fontsize=14, fontname='Franklin Gothic Medium Cond', color = 'gray')


            all_4_axis[0].barh(['Gold.', 'Silver.', 'Bronze Medal.'], [time_gold_result, time_silver_result, time_bronze_result], color=['cornflowerblue', 'darkblue', 'steelblue'],height  = 0.5)
            all_4_axis[1].barh(['Gold.', 'Silver.', 'Bronze Medal.'], [time_gold_result, time_silver_result, time_bronze_result], color=['cornflowerblue', 'darkblue', 'steelblue'],height = 0.5)
            all_4_axis[2].barh(['Gold.', 'Silver.', 'Bronze Medal.'], [time_gold_result, time_silver_result, time_bronze_result], color=['cornflowerblue', 'darkblue', 'steelblue'],height = 0.5)
            all_4_axis[3].barh(['Gold.', 'Silver.', 'Bronze Medal.'], [time_gold_result, time_silver_result, time_bronze_result], color=['cornflowerblue', 'darkblue', 'steelblue'],height = 0.5)



        shifting_y_axis = 0.9


        #for n in np.arange(len(mini_df_style)):
        # Teams names - first 3 places :

        # Men - 'Freestyle'
        all_4_axis[0].text(x=1, y=1.9,s= 'USA', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[0].text(x=1, y=0.9, s='FRA', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[0].text(x=1, y=-0.05, s='CAD', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        # Men - 'Medley'
        all_4_axis[2].text(x=1, y=1.9,s= 'USA', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[2].text(x=1, y=0.9, s='FRA', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[2].text(x=1, y=-0.05, s='CAD', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')

        # Women - 'Freestyle'
        all_4_axis[1].text(x=1, y=1.9,s= 'ISR', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[1].text(x=1, y=0.9, s='USA', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[1].text(x=1, y=-0.05, s='BRZ', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        # Women - 'Medley'
        all_4_axis[3].text(x=1, y=1.9,s= 'ISR', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[3].text(x=1, y=0.9, s='CAN', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[3].text(x=1, y=-0.05, s='BRZ', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')



        all_4_axis[0].text(x=9, y=1.4,s= '04:39.200', ha='left', va='bottom', fontsize=10, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[0].text(x=9, y=0.9, s='04:42.200', ha='left', va='bottom', fontsize=10, alpha=1, rotation=0, color='w',weight='bold')
        all_4_axis[0].text(x=9, y=-0.1, s='04:43.700', ha='left', va='bottom', fontsize=10, alpha=1, rotation=0, color='w',weight='bold')
        print('*')

        # SUBTITLE
        plt.title(f'Year {subtitle_year}  at {subtitle_location}' ,fontweight="bold", loc='left', fontsize=14,fontname='Franklin Gothic Medium Cond', x=-4.30, y=1, style='italic' )






    plt.xlabel('Time', fontsize=18)
    plt.xticks(fontsize=10)


    # TITLE
    plt.suptitle('Comparing the evolution of freestyle and medley relay events throughout the years', x=0.53, y=1, ha='center', fontsize=25,fontname='Franklin Gothic Medium Cond', color = 'lightseagreen' )


    #f'Year {subtitle_year}  at {subtitle_location}'
    # plt.savefig('2BarPlot.png')
    plt.show()





if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../Data/Olympic_Swimming_1912to2020.csv')

    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]


    # I have added the list of years hard coded because not every year we have had both gender two kinds of stroke : 'Medley' & 'Freestyle'
    years_list = [1964,1968,1972,1984,1988,1992,1996,2000,2004,2008,2012,2016]

    for olympic_year in years_list :
        mini_df_year = final_clean_table[final_clean_table['Year'] == olympic_year]
        men_df_each_year , women_df_each_year  = prepering_the_data_for_vertical_subplots(mini_df_year)
        plotting_subplot_for_freestyle_vs_medley_relay(men_df_each_year , women_df_each_year)
        print('*')

