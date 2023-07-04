import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# **************************************************************************************************************
# Function  name: convert_time_to_seconds ( Examples  '1:59.06' -> 119.06 , '00:01:53.410000' -> 113.41 )
# input: Define a custom function to convert time in minutes to seconds
# return value: Converting  the values to seconds with two decimal place
# ****************************************************************************************************************
# Define a custom function to convert time in minutes to seconds
def convert_time_to_seconds(time_str):
    parts = time_str.split(':')
    if len(parts) == 1:  # Format: 'mm.ss'
        minutes = 0
        try:
            seconds = float(parts[0])
        except ValueError:
            return None  # Invalid seconds format
    elif len(parts) == 2:  # Format: 'm:ss'
        try:
            minutes = int(parts[0])
            seconds = float(parts[1])
        except ValueError:
            return None  # Invalid minutes or seconds format
    elif len(parts) == 3:  # Format: 'hh:mm:ss'
        try:
            minutes = int(parts[1])
            seconds = float(parts[2])
        except ValueError:
            return None  # Invalid minutes or seconds format
    else:
        return None  # Invalid format
    return minutes * 60 + seconds

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
                          'Location':[],
                          'Results (In seconds)': []})

    men_df_each_year = pd.DataFrame()  # Initialize an empty dataframe for men
    women_df_each_year = pd.DataFrame()  # Initialize an empty dataframe for women
    df_each_year = pd.DataFrame()

    # Dealing with the "Result" column - Define a lambda function to convert the time format
    convert_time = lambda x: ':'.join(x.split(':')[-2:])[:-3]

    # Apply the lambda function to the 'Time_results' column - for the annotation values
    mini_df_year['Time_results'] = mini_df_year['Results'].apply(convert_time)
    print('*')
    gender_type = ['Men','Women']
    # Retrieving the data after  3 constraints:
    for gender in gender_type :
        mini_df_year_gender = mini_df_year.loc[(mini_df_year["Relay?"] == 1) & #Relay means 'Medley' or 'Freestyle'
                                               (mini_df_year['Gender'] == gender) &
                                               (mini_df_year['Distance (in meters)'] == '4x100')]

        # Another filter - 3 first place
        first_3_places = [1, 2, 3]
        final_medals_table = mini_df_year_gender[mini_df_year_gender['Rank'].isin(first_3_places)]

        # Apply the conversion function to the 'time' column    # '1:59.06'  ->119.06 , '00:01:53.410000' -> 113.41
        final_medals_table['Results (In seconds)'] = final_medals_table['Results'].apply(convert_time_to_seconds)
        final_medals_table['Results (In seconds)'] = final_medals_table['Results (In seconds)'].apply(lambda x: int(x))

        print('*')
        relevent_fields = ['Team','Year','Stroke','Gender','Rank','Time_results', 'Location','Results (In seconds)']
        final_medals_table = final_medals_table.loc[:,relevent_fields]

        df_each_year = pd.concat([df_each_year, final_medals_table], axis=0)

        if gender == 'Men':
            men_df_each_year = pd.concat([men_df_each_year, final_medals_table], axis=0)
        else:
            women_df_each_year = pd.concat([women_df_each_year, final_medals_table], axis=0)

    print('*')


    return  df_each_year, men_df_each_year, women_df_each_year

# **************************************************************************************************************
# Function  name: creating_advance_line_chart
# input:
# return value: Converting  the values to seconds with two decimal place
# ****************************************************************************************************************
def plotting_subplot_for_freestyle_vs_medley_relay(df_each_year, men_df_year, women_df_year):

    print('*')
    categories = ['Gold', 'silver', 'Bronze']

    men_medley = list(df_each_year.loc[(mini_df_year["Gender"] == 'Men')&(mini_df_year['Stroke'] == 'Medley')]['Results (In seconds)'])#['Time_results'])
    women_medley = list(df_each_year.loc[(mini_df_year["Gender"] == 'Women')&(mini_df_year['Stroke'] == 'Medley')]['Results (In seconds)'])#['Time_results'])
    men_Freestyle = list(df_each_year.loc[(mini_df_year["Gender"] == 'Men')&(mini_df_year['Stroke'] == 'Freestyle')]['Results (In seconds)'])#['Time_results'])
    women_Freestyle = list(df_each_year.loc[(mini_df_year["Gender"] == 'Women')&(mini_df_year['Stroke'] == 'Freestyle')]['Results (In seconds)'])#['Time_results'])

    gender = ['Men','Women']
    styles_of_swimming = ['Freestyle', 'Medley'] # ['Men - Medley','Women - Medley','Men - Freestyle','Women - Freestyle']


    for swimmer_gender in gender:
        relevant_table = df_each_year[df_each_year['Gender'] == swimmer_gender]
        print(relevant_table)
        print('*')
        for swimming_style in styles_of_swimming:
            mini_df_style = relevant_table[relevant_table['Stroke'] == swimming_style]
            print(mini_df_style)

            # for gender, df_year in [('Men', men_df_year), ('Women', women_df_year)]:
            #     mini_df_style = df_year[df_year['Stroke'] == swimming_style]
            #     print('*')
            # In order to retrieve the name of the teams that won the medals, we need to "reset_index" the table
            # mini_df_style = mini_df_style.reset_index()
            # team_gold_annotation = mini_df_style.loc[0, 'Team']
            # time_gold_result_annotation = mini_df_style.loc[0, 'Time_results']

            plt.figure(figsize=[14, 10])

            #Set one size for all subplots
            fig, all_4_axis = plt.subplots(nrows=1, ncols=4, sharey=True,  figsize=(16,4))  # 4 plots
            print('*')

            # # Iterate over the axes and plot the bars
            # for ax in all_4_axis:
            #     ax.bar(categories, values, width=0.5)  # Adjust the width parameter as desired

            for i, ax in enumerate(all_4_axis):
                if i == 0:
                    values = men_medley
                elif i == 1:
                    values = women_medley
                elif i == 2:
                    values = men_Freestyle
                elif i == 3:
                    values = women_Freestyle

                ax.barh(categories, values)
                ax.set_xlim(180, 320)  # The scale will start at 180 seconds and will ends at 320 seconds
                print('*')
                # Add values over the bars - annotation in each subplot
                for j, v in enumerate(values):
                    ax.text(v + 0.5, j, str(v), color='Black', va='center')
                    #ax.bar(categories, values, width=0.5)

                # Teams names - first 3 places :
                teams_name_annotation = list(mini_df_style.loc[:, 'Team'])
                list_of_subplot = list(range(0, 4))
                time_res_annotation = list(mini_df_style.loc[:, 'Time_results'])
                fontdict_input = {'fontsize': 12, 'weight': 'heavy', 'alpha': 0.9, 'color': 'white'} # 'ha': 'left'
                print('*')


                # Here below the annotation for the "Team" +  'Time_results' as '04:39.200'
                for subplot_number in list_of_subplot :  #TODO: find out why the subplot number is not changing during the outer loop
                    # print(subplot_number)
                    # print('*')
                    for index, (team_name, time_zone) in enumerate(zip(teams_name_annotation, time_res_annotation)):
                        print('*')

                        all_4_axis[subplot_number].text(x=13, y=1.9-index ,s= team_name ,  va='bottom',fontdict=fontdict_input)
                        all_4_axis[subplot_number].text(x=14, y=1.65-index ,s= time_zone, ha='left', va='bottom' ,style='italic',fontsize='9',  fontdict=fontdict_input)
                        #all_4_axis[subplot_number].text(x=14, y=1.65-index ,s= '04:39.200', ha='left', va='bottom' ,style='italic',fontsize='9',  fontdict=fontdict_input)
                        #all_4_axis[subplot_number].bar(categories, values, width=0.4)


                print('*')

        # SUBTITLE ( lines 194 - 201 )
        years_list = [1964,1968,1972,1984,1988,1992,1996,2000,2004,2008,2012,2016]
        location_list=['Tokyo','City','Munich','Angeles','Seoul','Barcelona','Atlanta','Sydney','Athens','Beijing','London','Rio']
        # Reverse the list of years and location :
        years_list = years_list[::-1]
        location_list = location_list[::-1]

        for subtitle_year,subtitle_location in zip(years_list,location_list ):
            plt.title(f'{subtitle_location} - {subtitle_year} \nOlympic Games' ,fontweight="bold", loc='left', fontsize=14,fontname='Franklin Gothic Medium Cond', x=-3.80, y=1, style='italic', color = 'navy' )


    # Adding for each subplot a title: ( lines 200-204 )
    subplot_names = ['Men - Medley','Women - Medley','Men - Freestyle','Women - Freestyle']
    for title_subplot in subplot_names :
        print(title_subplot)
    for index,plot_name in zip(np.arange(0,4,1),subplot_names):
        all_4_axis[index].set_title(plot_name, fontsize=14, fontname='Franklin Gothic Medium Cond', color = 'gray')
        #all_4_axis[subplot_number].bar(x_values, y_values, width=bar_width)


        # SUBTITLE ( lines 194 - 201 )
        years_list = [1964, 1968, 1972, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
        location_list = ['Tokyo', 'City', 'Munich', 'Angeles', 'Seoul', 'Barcelona', 'Atlanta', 'Sydney', 'Athens',
                         'Beijing', 'London', 'Rio']
        # Reverse the list of years and location :
        years_list = years_list[::-1]
        location_list = location_list[::-1]

    #ax.set_xlabel('time (In seconds)')
    fig.text(0.5, 0.04, "Results (In seconds)", ha="center", va="center",weight='bold',style='italic',fontname='Franklin Gothic Medium Cond',fontsize=14)


    # Set labels and title for each subplot
    #ax.set_ylabel('Categories')
    plt.xticks(fontsize=9)

    # TITLE
    plt.suptitle('Comparing the evolution of freestyle and medley relay events throughout the years', x=0.53, y=1, ha='center', fontsize=25,fontname='Franklin Gothic Medium Cond', color = 'lightseagreen' )

    # plt.savefig('2BarPlot.png')
    plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    #df = pd.read_csv('/home/shay_diy/PycharmProjects/Olympic_games/data/Olympic_Swimming.csv')

    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]


    # I have added the list of years hard coded because not every year we have had both gender two kinds of stroke : 'Medley' & 'Freestyle'
    years_list = [1964,1968,1972,1984,1988,1992,1996,2000,2004,2008,2012,2016]

    for olympic_year in years_list :
        mini_df_year = final_clean_table[final_clean_table['Year'] == olympic_year]
        df_each_year, men_df_each_year, women_df_each_year= prepering_the_data_for_vertical_subplots(mini_df_year)
        plotting_subplot_for_freestyle_vs_medley_relay(df_each_year, men_df_each_year , women_df_each_year)
        print('*')



        # #need to add:
        # my_list = [[men_medley], [women_medley], [men_Freestyle],[women_Freestyle]]
        #
        # for sublist in my_list:
        #     for item in sublist:
        #         print(item)


        ## need to add to the cheatsheet :
        # styles_of_swimming = ['Medley', 'Freestyle'] # ['Men - Medley','Women - Medley','Men - Freestyle','Women - Freestyle']
        # for swimming_style in styles_of_swimming:

        #removed from the script
        # team_annotation = mini_df_style.loc[:, 'Team']
        #
        # team_silver_annotation = mini_df_style.loc[1, 'Team']
        # time_silver_result_annotation = mini_df_style.loc[1, 'Time_results']
        #
        # team_bronze_annotation = mini_df_style.loc[2, 'Team']
        # time_bronze_result_annotation = mini_df_style.loc[2, 'Time_results']

        #fastest_time = df_each_year.loc[:, 'Results (In seconds)'].min()
        #slowest_time = df_each_year.loc[:, 'Results (In seconds)'].max()

        #x_values = np.arange(fastest_time, slowest_time, 6)

        # Men - 'Freestyle'
        # all_4_axis[0].text(x=2.5, y=0.9, s='FRA', ha='left', va='bottom', fontdict=fontdict_input)
        # all_4_axis[0].text(x=2.5, y=0.9, s='FRA', ha='left', va='bottom', fontdict=fontdict_input)
        # all_4_axis[0].text(x=2.5, y=-0.05, s='CAD', ha='left', va='bottom', fontdict=fontdict_input)
        # print('*')
        # Men - 'Medley' - working
        # all_4_axis[2].text(x=2, y=1.9,s= 'USA', ha='left', fontdict=fontdict_input)
        # all_4_axis[2].text(x=2, y=0.9, s='FRA', ha='left',fontdict=fontdict_input)
        # all_4_axis[2].text(x=2, y=-0.05, s='CAD', ha='left', fontdict=fontdict_input)

        # Women - 'Freestyle' - working ( position 0 )
        # all_4_axis[1].text(x=3, y=1.9,s= 'ISR', ha='left', va='bottom', fontdict=fontdict_input)
        # all_4_axis[1].text(x=3, y=0.9, s='USA', ha='left', va='bottom', fontdict=fontdict_input)
        # all_4_axis[1].text(x=3, y=-0.05, s='BRZ', ha='left', va='bottom', fontdict=fontdict_input)
        # # Women - 'Medley' - - working
        # all_4_axis[3].text(x=2, y=1.9,s= 'ISR', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        # all_4_axis[3].text(x=2, y=0.9, s='CAN', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
        # all_4_axis[3].text(x=2, y=-0.05, s='BRZ', ha='left', va='bottom', fontsize=12, alpha=1, rotation=0, color='w',weight='bold')
