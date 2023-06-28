import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

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
    print('*')
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
    print('*')
    df_starting = {'Olympic_year': list_of_years,
                   'Amount_of_medals': list_of_number_of_medals_for_the_team}

    final_table = pd.DataFrame(df_starting,columns=['Olympic_year', 'Amount_of_medals'])
    print('*')
    return avg_of_the_team_over_the_years , final_table ,  team_name

# **************************************************************************************************************
# Function  name: creating_the_plot_chart_of_each_teams
# input:
# return value:
# ****************************************************************************************************************
def creating_the_dot_chart_of_each_teams(avg_of_the_team_over_the_years,final_table, team_name):

    #sns.catplot(data=tips, x="day", y="total_bill", jitter=False)
    print('*')
    #https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#17.-Dot-Plot
    #https://seaborn.pydata.org/tutorial/categorical.html
    # Prepare Data
    # Generate sample data
    # np.random.seed(0)
    # x = np.random.randn(25)
    # y = np.random.randint(1, 33, size=25)


    team_name_str = ', '.join(team_name)
    print('*')
    x_axis = final_table['Olympic_year'].to_numpy()
    y_axis = final_table['Amount_of_medals'].to_numpy()


    print('*')
    # Define the threshold for color differentiationrn, di
    threshold = 12


    # Assign colors based on the y-values
    colors = np.where(y_axis <= avg_of_the_team_over_the_years, 'silver', 'navy')

    # Create the dot plot

    plt.scatter(x_axis, y_axis, c=colors)

    # Customize the plot
    plt.xlabel('Olympic Years',fontsize= 17,  color= 'Gray',fontname='Franklin Gothic Medium Cond')
    plt.ylabel(f'Amount of medals for the {team_name_str} team',fontsize= 17,  color= 'Gray',fontname='Franklin Gothic Medium Cond')

    fontdict_input_title = {'fontsize': 23, 'weight': 'heavy', 'alpha': 0.9, 'color': 'Navy','fontname':'Franklin Gothic Medium Cond'}
    plt.title(f"Number of time the {team_name_str} team got medals over the years", loc='left',fontdict=fontdict_input_title,  pad=20) # }

    plt.xticks(range(1, 5))
# Show the plot
    plt.show()






if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    print('*')

    # Cleaning_the_data:
    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]

    list_of_teams = ['USA','AUS','GBR','JPN','GER','CAN','GDR','HUN']

    for team_names in list_of_teams:
        mini_df_team = final_clean_table[final_clean_table['Team'] == team_names]
        avg_of_the_team_over_the_years , final_table , team_name = preparing_the_data_for_the_dot_plot(mini_df_team)
        creating_the_dot_chart_of_each_teams(avg_of_the_team_over_the_years , final_table , team_name )
        print('*')

