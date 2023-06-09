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
# Function  name: prepering_the_data_pf_the_swimmers_who_won_a_olymplic_world_record
# input:
# return value:
# ****************************************************************************************************************
def prepering_the_data_pf_the_swimmers_who_won_a_olymplic_world_record(final_clean_table):

    final_men_table = final_clean_table.loc[ (final_clean_table['Gender'] == 'Men')]
    final_women_table = final_clean_table.loc[ (final_clean_table['Gender'] == 'Women')]

    final_men_table.sort_values(by = 'Year', inplace=True, ascending=True)
    final_women_table.sort_values(by = 'Year', inplace=True, ascending=True)
    print('*')

    world_olympic_record = pd.DataFrame({'Location':[],
                                         'Distance (in meters)':[],
                                         'Stroke':[],
                                         'Team':[],
                                         'Athlete':[],
                                         'Results':[],
                                         'Results (In seconds)':[]})

    groupby_stroke = final_men_table.groupby("Stroke")
    for swimming_style_men, mini_df_style_men in groupby_stroke:
        print(swimming_style_men)
        print(mini_df_style_men)
        grooupby_distance = mini_df_style_men.groupby("Distance (in meters)")
        for type_distance_men, mini_df_distance_men in grooupby_distance:
            print(type_distance_men)
            print(mini_df_distance_men)
            print('*')

            final_medals_table = mini_df_distance_men[mini_df_distance_men['Rank'] == 1]
            final_medals_table.sort_values(by = 'Year', inplace=True, ascending=True)
            res = final_medals_table.reset_index()



            current_min = float('inf')

            for value in res['Results (In seconds)'][::1]:

                # The next row give us the min value  between the 'value' between the 'current_min'
                current_min = min(value, current_min)
                # The next row gives us info about current olympic record in a specific field
                current_Olympic_record = res[res['Results (In seconds)'] == current_min][['Location','Distance (in meters)', 'Stroke','Team','Athlete', 'Results','Results (In seconds)']]

                # Concatenate all the broken records together for the same field :
                world_olympic_record = pd.concat([world_olympic_record, current_Olympic_record], axis=0)
            print('*')
            men_world_breaker_holder= world_olympic_record['Athlete'].value_counts()

    Top_men_world_breaker_holder = men_world_breaker_holder.head(n=10)
    print('*')
    return Top_men_world_breaker_holder


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    #df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Olympic_games/data/Olympic_Swimming.csv')
    print('*')

    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]
    final_clean_table['Results (In seconds)'] = final_clean_table['Results'].apply(convert_time_to_seconds)


    print('*')

    column_headers = list(final_clean_table.columns.values)

    prepering_the_data_pf_the_swimmers_who_won_a_olymplic_world_record(final_clean_table)
    print('*')
