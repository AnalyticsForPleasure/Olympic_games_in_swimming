import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# **************************************************************************************************************
# Function  name: preparing_the_data_for_the_dot_plot
# input:
# return value:
# ****************************************************************************************************************

def preparing_the_data_for_the_dot_plot(mini_df_team):
    # Retrieving -  3 first place

    # df_starting = pd.DataFrame({'olympic_year': [],
    #                             'Amount_of_medals': []})


    first_3_places = [1, 2, 3]
    final_medals_table = mini_df_team[mini_df_team['Rank'].isin(first_3_places)]
    final_medals_table.reset_index(inplace=True)
    print('*')
    list_of_number_of_medals_for_the_team = []
    grouping_by_year = final_medals_table.groupby('Year')
    for year_olympic, mini_df_year in grouping_by_year:
        print(year_olympic)
        print(mini_df_year)
        medals_specific_year = mini_df_year.shape[0]
        print('*')

        # list_of_number_of_medals_for_the_team.append()
        list_of_number_of_medals_for_the_team.append(medals_specific_year)


    print('*')
    avg_of_the_team_over_the_years = np.mean(list_of_number_of_medals_for_the_team) # In order to create the vertical line
    list_of_years = list(mini_df_team['Year'].unique())
    list_of_years = list_of_years[::-1]
    print('*')

    df_starting = {'Olympic_year': list_of_years,
                   'Amount_of_medals': list_of_number_of_medals_for_the_team}

    final_table = pd.DataFrame(df_starting,columns=['Olympic_year', 'Amount_of_medals'])
    print('*')
    return avg_of_the_team_over_the_years , final_table


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../Data/Olympic_Swimming_1912to2020.csv')
    print('*')

    # Cleaning_the_data:
    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]

    list_of_teams = ['AUS','GBR','JPN','GER','CAN','GDR','HUN'] # 'USA',
    list_of_teams = ['AUS','GBR','JPN','GER','CAN','GDR','HUN'] # 'USA',
    for team_names in list_of_teams:
        mini_df_team = final_clean_table[final_clean_table['Team'] == team_names]
        preparing_the_data_for_the_dot_plot(mini_df_team)
        print('*')