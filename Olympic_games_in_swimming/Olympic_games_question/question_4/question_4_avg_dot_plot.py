import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib

# **************************************************************************************************************
# Function  name: preparing_the_data_for_the_dot_plot
# input:
# return value:
# ****************************************************************************************************************

def preparing_the_data_for_the_dot_plot(mini_df_team):
    # Retrieving -  3 first place
    first_3_places = [1, 2, 3]
    final_medals_table = mini_df_team[mini_df_team['Rank'].isin(first_3_places)]
    final_medals_table.reset_index(inplace=True)
    list_of_number_of_medals_for_the_team = []
    grouping_by_year = final_medals_table.groupby('Year')
    for year_olympic, mini_df_year in grouping_by_year:
        print(year_olympic)
        print(mini_df_year)
        medals_specific_year = mini_df_year.shape[0]
        print('*')
        list_of_number_of_medals_for_the_team.append(medals_specific_year)

    print('*')
    avg_of_the_team_over_the_years = np.mean(list_of_number_of_medals_for_the_team) # In order to create the vertical line
    list_of_years = list(final_medals_table['Year'].unique())
    list_of_years = list_of_years[::-1]

    team_name = final_medals_table['Team'].unique()

    df_starting = {'Olympic_year': list_of_years,
                   'Amount_of_medals': list_of_number_of_medals_for_the_team}

    final_table = pd.DataFrame(df_starting,columns=['Olympic_year', 'Amount_of_medals'])

    return avg_of_the_team_over_the_years , final_table ,  team_name

# **************************************************************************************************************
# Function  name: creating_the_plot_chart_of_each_teams
# input:
# return value:
# ****************************************************************************************************************
def creating_the_dot_chart_of_each_teams(avg_of_the_team_over_the_years,final_table, team_name, color):

    print('*')
    sns.set_style("dark")
    plt.figure(figsize=(19, 7.5))

    max_medals_over_a_game = final_table.loc[:,'Amount_of_medals'].max()
    team_name_str = ', '.join(team_name)
    x_axis = final_table['Olympic_year'].to_numpy()
    y_axis = final_table['Amount_of_medals'].to_numpy()


    # Assign colors based on the y-values
    colors = np.where(y_axis <= avg_of_the_team_over_the_years, 'silver',color ) #'deepskyblue'
    fontdict_input2 = {'fontsize': 21, 'weight': 'heavy', 'alpha': 0.9,'fontname':'Franklin Gothic Medium Cond',  'weight':'bold' , 'style':'italic' }

    # Add the horizontal line ( we have 2 parts ) which present the avg line
    plt.hlines(avg_of_the_team_over_the_years,1912,1964,colors="gray", linestyle='dashed', linewidth=3)
    plt.hlines(avg_of_the_team_over_the_years,1972,2020,colors="gray", linestyle='dashed',  linewidth=3)

    rounded_number = round(avg_of_the_team_over_the_years, 2)

    # Annotation for the avg value at the center - horizontal line
    plt.text(x=1964, y=avg_of_the_team_over_the_years - avg_of_the_team_over_the_years * 0.07, s=f'Avg   {rounded_number}', ha='left', va='bottom', color = color ,fontdict=fontdict_input2)

# Create the dot plot
    plt.scatter(x_axis, y_axis, s= 100,  c=colors)
    plt.xticks(np.arange(1912, 2020, step=8))

    # Customize the plot
    plt.xlabel('Olympic Years',fontsize= 17,  color= 'Gray',fontname='Franklin Gothic Medium Cond')
    plt.ylabel(f'Amount of medals for the {team_name_str} team',fontsize= 17,  color= 'Gray',fontname='Franklin Gothic Medium Cond')

    fontdict_input_title = {'fontsize': 23, 'weight': 'heavy', 'alpha': 0.9, 'color': 'Navy','fontname':'Franklin Gothic Medium Cond'}
    plt.title(f"Number of time the {team_name_str} team got medals over the years", loc='left',fontdict=fontdict_input_title,  pad=20) # }

    standard_deviation_for_a_team = round(final_table.loc[:,'Amount_of_medals'].std(),2)

    position_Y_annotation = max_medals_over_a_game * 0.1
    plt.annotate(text=f'Standard \n Deviation = {standard_deviation_for_a_team}',
                 xy=(2008,position_Y_annotation),  # Point on the plot where the arrow points to
                 xytext=(2009, position_Y_annotation +1),  # Starting point of the text
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 color=color,
                 size=22,
                 fontproperties='Franklin Gothic Medium Cond')

    plt.savefig(f'dot_plot_with_avg_line_of_{team_name_str}.jpg', dpi=250, bbox_inches='tight')

# Show the plot
    plt.show()



if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    print('*')

    # Cleaning_the_data:
    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]

    list_of_teams = ['USA','AUS','GBR','JPN','GER','CAN','GDR','HUN']

    colors = ['orange','lightcoral', 'dodgerblue', 'yellowgreen', 'navy', 'springgreen','Black','lightgreen']

    for team_names , color in zip (list_of_teams, colors):
        mini_df_team = final_clean_table[final_clean_table['Team'] == team_names]
        avg_of_the_team_over_the_years , final_table , team_name = preparing_the_data_for_the_dot_plot(mini_df_team)
        creating_the_dot_chart_of_each_teams(avg_of_the_team_over_the_years , final_table , team_name,  color )
        print('*')

