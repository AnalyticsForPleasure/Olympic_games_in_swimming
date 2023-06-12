import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import numpy as np

# **************************************************************************************************************
# Function  name: preparing_the_data_for_the_line_plot
# input:
# return value:
# ****************************************************************************************************************
def preparing_the_data_for_the_line_plot(df):
    filter_df_by_team_and_year = df.loc[:, ['Year', 'Team']]
    filter_df_by_team_and_year.sort_values(by='Year', inplace=True, ascending=True)
    df_starting = {'Year': [],
                   'Counter Countries': []}
    list_of_countries_each_olympic = []
    list_of_years = filter_df_by_team_and_year['Year'].unique().tolist()
    for olympic_year in list_of_years:
        number_of_countries_in_a_game = filter_df_by_team_and_year[filter_df_by_team_and_year['Year'] == olympic_year]

        result = number_of_countries_in_a_game.drop_duplicates()
        number_of_counties = result.shape[0]
        print('*')
        list_of_countries_each_olympic.append(number_of_counties)
        print('*')
        list_of_years
    df_starting = {'Year taken the Olympic Game': list_of_years,
                   'Counter Countries': list_of_countries_each_olympic}

    print('*')
    final_table = pd.DataFrame(df_starting,
                               columns=['Year taken the Olympic Game', 'Counter Countries'])
    print('*')

    return final_table

# **************************************************************************************************************
# Function  name: creating_advance_line_chart
# input:
# return value: Converting  the values to seconds with two decimal place
# ****************************************************************************************************************
def creating_advance_line_chart(table_input):
    print('*')
    fig, ax = plt.subplots()
    # figure list(res.loc[:, 'player_weight'])
    x_values =list(table_input.loc[:,'Year taken the Olympic Game'])   # 'x_values' line represents X- axis values
    y_values =  list(table_input.loc[:,'Counter Countries'])  #'y_values' line represents y- axis values

    plt.style.use('ggplot') # this time we add this labrary
    plt.plot(x_values,
             y_values,
             color = 'dodgerblue',
             linestyle = 'solid',
             linewidth = 4,
             mfc='none',
             marker='.',
             markersize = 24,
             label = 'Alice',
             markeredgecolor='black')
    # adding rectangle
    plt.axvspan(1927,1929,color='lightgray')#, ymin = 0  ,ymax =0.45 ,alpha=0.2 )
    plt.axvspan(1963,1965,color='lightgray') #, ymin = 1  ,ymax =0.25, alpha=0.2 )
    plt.axvspan(2015,2017,color='lightgray' )#, ymin = 0.0  ,ymax =0.95 , alpha=0.2 )

    # i = 1.0
    # j = 0.25
    # plt.annotate(multiple_entrepreneur[i], (-0.05 + i, multiple_entrepreneur[i] + j))
    first_string = 'Summer Games 1928 - Amsterdam'
    second_string = 'Summer Games 1964 - Tokyo'
    second_string = 'Summer Games 2016 - Rio'

    ax.text(1927.2, 17.5, first_string , rotation=270, va='center' ,fontsize=10 , color='navy' ,weight='bold') # navy
    ax.text(1963.2, 31, second_string , rotation=270, va='center' ,fontsize=10 , color='navy' ,weight='bold') # navy
    ax.text(2015.5, 16.5, second_string , rotation=270, va='center' ,fontsize=10 , color='navy' ,weight='bold') # navy







    plt.title('The distribution of medals won over the years by different teams' ,fontsize=26, weight='bold',fontname='Franklin Gothic Medium Cond')
    plt.xlabel('Years of the Summer Olympic', fontsize=14,fontweight='bold',fontname='Franklin Gothic Medium Cond')
    plt.ylabel('Number of countries teams', fontsize=14,fontweight='bold',fontname='Franklin Gothic Medium Cond')
    plt.xticks(x_values)
    plt.legend()
    plt.show()

if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('Data/Olympic_Swimming_1912to2020.csv')
    print('*')

    result = preparing_the_data_for_the_line_plot(df)
    creating_advance_line_chart (result)

    print('*')





