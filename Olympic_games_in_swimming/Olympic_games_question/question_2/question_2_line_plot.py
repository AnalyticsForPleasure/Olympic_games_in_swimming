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

    fig, ax = plt.subplots(figsize=(19, 7.5))
    # figure list(res.loc[:, 'player_weight'])
    x_values =list(table_input.loc[:,'Year taken the Olympic Game'])   # 'x_values' line represents X- axis values
    y_values =  list(table_input.loc[:,'Counter Countries'])  #'y_values' line represents y- axis values

    plt.style.use('ggplot') # this time we add this labrary
    plt.plot(x_values,
             y_values,
             color = 'dodgerblue',
             linestyle = 'solid',
             linewidth = 4,
             markeredgewidth=6, # Thickest of the circle marker
             marker='o',
             markerfacecolor='none',
             markersize = 13,
             label = 'Alice',
             markeredgecolor='dodgerblue',
             )



    #plt.scatter(x,y,marker='o', facecolors='none', edgecolors='r')
    # adding rectangle
    plt.axvspan(1927,1929,color='lightgray')#, ymin = 0  ,ymax =0.45 ,alpha=0.2 )
    plt.axvspan(1963,1965,color='lightgray') #, ymin = 1  ,ymax =0.25, alpha=0.2 )
    plt.axvspan(2015,2017,color='lightgray' )#, ymin = 0.0  ,ymax =0.95 , alpha=0.2 )



    first_string = 'Summer Games 1928 - Amsterdam'
    second_string = 'Summer Games 1964 - Tokyo'
    third_string = 'Summer Games 2016 - Rio'



    ax.text(1927.2, 17.5, first_string , rotation=270, va='center' ,fontsize=10 , color='navy' ,weight='bold') # navy
    ax.text(1963.2, 31, second_string , rotation=270, va='center' ,fontsize=10 , color='navy' ,weight='bold') # navy
    ax.text(2015.5, 16.5, third_string , rotation=270, va='center' ,fontsize=10 , color='navy' ,weight='bold') # navy

    t_ending_2016 = ("From 1964 to 2016, Olympic swimming witnessed \n"
         "extraordinary performances and the emergence of\n" 
         "legendary swimmers. Don Schollander's dominance in\n"
         "1964 Mark Spitz's record-breaking seven gold medals\n" 
         "in 1972, and Michael Phelps' unprecedented 23 gold\n"
         "medals stand as highlights. Ian Thorpe, Pieter van den\n"
         "Hoogenband, and Stephanie Rice showcased their skills\n"
         "during this period. \n")

    t_ending_1964 = ("From 1928 to 1964, the Olympic swimming events\n"
              "witnessed the rise of exceptional swimmers and\n"
              "memorable moments. Johnny Weissmuller's three\n"
              "gold medals in 1928 set a precedent, while Kusuo\n"
              "Kitamura became the youngest male swimming\n"
              "champion in 1936. Dawn Fraser made her mark in 1948,\n"
              "winning multiple gold medals and setting world\n"
              "records.\n"
              "In 1964, Fraser made history as the first woman\n"
              "to win the same individual event at three\n"
              "consecutive Olympics\n")


    # Adding long text inside the chart:
    ax.text(1930, 31, t_ending_1964 , rotation=0, va='center' ,fontsize=9 , color='Gray' ,weight='bold')
    ax.text(1980, 15, t_ending_2016 , rotation=0, va='center' ,fontsize=9 , color='Gray' ,weight='bold')

    plt.title('The distribution of medals won by various teams over the years' ,fontsize=26, weight='bold',fontname='Franklin Gothic Medium Cond')
    plt.xlabel('Years of the Summer Olympic', fontsize=14,fontweight='bold',fontname='Franklin Gothic Medium Cond')
    plt.ylabel('Number of teams representing countries', fontsize=14,fontweight='bold',fontname='Franklin Gothic Medium Cond')
    plt.xticks(x_values)

    plt.savefig('line_chart.jpg',dpi=750, bbox_inches='tight')

    plt.show()

if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    print('*')

    result = preparing_the_data_for_the_line_plot(df)
    creating_advance_line_chart (result)

    print('*')





