import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
#plt.style.use(['unhcrpyplotstyle','dotplot'])
#import dataframe_image as dfi
import numpy as np

# **************************************************************************************************************
# Function  name: relevant_columns_highlighter
# input: adding styles to our dataframe
# return value:
# ****************************************************************************************************************
def relevant_columns_highlighter(x):
    my_style = "color: #1E90FF;" \
               "font-weight: bold;"
    return [my_style] * len(x)

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
# Function  name: preparing_the_olympic_data_for_the_dot_plot - Countries :  'USA','AUS', 'CAN','JPN' , 'GBR' ( 4 from 5 ), 'GER' ( 4 from 5 )
# input:
# return value: Converting  the values to seconds with two decimal place
# ****************************************************************************************************************
def preparing_the_olympic_data_for_the_dot_plot(mini_df_team):

    starting_point_percentage_list = []
    ending_point_percentage_list = []

    final_table_fastest_results =  pd.DataFrame({ 'Team':[],
                                                  'Stroke':[],
                                                  'Location': [],
                                                  'Year': [],
                                                  'Athlete': [],  # This filed is possible to be in a  pivot table index
                                                  'Results (In seconds)': [] , # Fastest result , Slowest result
                                                  'Fastest percentage':[]})


    final_table_slowest_results = pd.DataFrame({ 'Team':[],
                                                 'Stroke':[],
                                                 'Location': [],
                                                 'Year': [],
                                                 'Athlete': [],  # This filed is possible to be in a  pivot table index
                                                 'Results (In seconds)': [] , # Fastest result , Slowest result
                                                 'Slowest percentage':[]})

    list_of_strokes = mini_df_team['Stroke'].unique()  # kinds of strokes: ['Breaststroke' 'Backstroke' 'Freestyle' 'Butterfly' 'Individual medley']
    for name_stroke in list_of_strokes:
        mini_df_by_stroke = mini_df_team[mini_df_team['Stroke'] == name_stroke]
        print('*')

        # Best & Worst above all the teams over entire years:
        worst_score_ever_in_the_event = final_clean_table['Results (In seconds)'].max()
        best_score_ever_in_the_event = final_clean_table['Results (In seconds)'].min()
        print('*')

        worst_score_achieved_by_the_team = mini_df_by_stroke['Results (In seconds)'].max()
        # retrieving the row of the worst_score_achieved_by_the_team :
        full_line_worst_score = mini_df_by_stroke[mini_df_by_stroke['Results (In seconds)'] == mini_df_by_stroke['Results (In seconds)'].max()]
        line_values_for_worst = full_line_worst_score.loc[:,['Team','Stroke','Location', 'Year','Athlete', 'Results (In seconds)']]
        print('*')
        best_score_achieved_by_the_team = mini_df_by_stroke['Results (In seconds)'].min()
        # retrieving the row of the best_score_achieved_by_the_team:
        full_line_best_score = mini_df_by_stroke[mini_df_by_stroke['Results (In seconds)'] == mini_df_by_stroke['Results (In seconds)'].min()]
        line_values_for_best = full_line_best_score.loc[:, ['Team','Stroke','Location', 'Year','Athlete', 'Results (In seconds)']]
        print('*')

        # normalization_scale = (100 / (worst_score_ever_in_the_event - best_score_ever_in_the_event))
        # Getting to the precentage values of the slowest & fastest swimmer in each teams :

        starting_point_for_the_team = (100 / (worst_score_ever_in_the_event - best_score_ever_in_the_event)) * (worst_score_ever_in_the_event - worst_score_achieved_by_the_team)
        starting_point_percentage_for_the_team = "{:.2f}".format(starting_point_for_the_team)

        starting_point_percentage = starting_point_percentage_for_the_team
        starting_point_percentage_list.append(starting_point_percentage)
        # working on the data before passing it to the Area chart


        ending_point_for_the_team = (100 / (worst_score_ever_in_the_event - best_score_ever_in_the_event)) * (worst_score_ever_in_the_event - best_score_achieved_by_the_team)
        ending_point_percentage_for_the_team = "{:.2f}".format(ending_point_for_the_team)

        ending_point_percentage = ending_point_percentage_for_the_team
        ending_point_percentage_list.append(ending_point_percentage)
        print('*')



        total_improvement_by_the_team = (ending_point_for_the_team - starting_point_for_the_team)
        total_improvement_by_the_team = "{:.2f}%".format(total_improvement_by_the_team)
        print('*')

        merged_df_one_line_after_the_other = pd.concat([line_values_for_best, line_values_for_worst], ignore_index=True)
        # Table of fastest results:
        final_table_fastest_results  = pd.concat([final_table_fastest_results,line_values_for_best], axis=0)

        # Table of slowest results:
        final_table_slowest_results = pd.concat([final_table_slowest_results, line_values_for_worst], axis=0)
        print('*')
    list_starting_percentage = starting_point_percentage_list
    list_ending_percentage = ending_point_percentage_list

    print('*')
    final_table_fastest_results.rename(columns={final_table_fastest_results.columns[5]: 'Best results by the team (In seconds)'}, inplace=True) # 'Best results by the team (In seconds)'
    #final_table_fastest_results_6_rows = final_table_fastest_results[final_table_fastest_results['Team'] == 'USA']
    final_table_fastest_results['Best results by the team (In seconds)'] = final_table_fastest_results['Best results by the team (In seconds)'].apply(lambda x: "{0:.2f}".format(x))
    final_table_fastest_results['Year'] = final_table_fastest_results['Year'].apply(lambda x:int(x))
    final_table_fastest_results = final_table_fastest_results.reset_index()  # final_table_fastest_results_6_rows
    print('*')


    # Adding_columns_for_the pre - plot :
    final_table_fastest_results=final_table_fastest_results.drop(['index'], axis=1)
    final_table_fastest_results = final_table_fastest_results.drop_duplicates()
    final_table_fastest_results['order'] = np.arange(final_table_fastest_results.shape[0])
    final_table_fastest_results['status'] = 'Best result by the team (In seconds)'
    final_table_fastest_results['Fastest percentage'] = list_ending_percentage


    final_table_slowest_results.rename(columns={final_table_slowest_results.columns[5]: 'Worst results by the team (In seconds)'}, inplace=True) # 'Worst results by the team (In seconds)'
    final_table_slowest_results['Worst results by the team (In seconds)'] = final_table_slowest_results['Worst results by the team (In seconds)'].apply(lambda x: "{0:.2f}".format(x))
    final_table_slowest_results['Year'] = final_table_slowest_results['Year'].apply(lambda x:int(x))
    final_table_slowest_results = final_table_slowest_results.reset_index()
    print('*')

    # Adding_columns_for_the pre - plot :
    final_table_slowest_results=final_table_slowest_results.drop(['index'], axis=1)
    final_table_slowest_results = final_table_slowest_results.drop_duplicates()
    final_table_slowest_results['order'] = np.arange(final_table_fastest_results.shape[0])
    final_table_slowest_results['status'] = 'Worst result by the team (In seconds)'
    final_table_slowest_results['Slowest percentage'] = list_starting_percentage

    # Move third column values to index column
    final_table_slowest_results = final_table_slowest_results.set_index('Stroke')
    final_table_fastest_results = final_table_fastest_results.set_index('Stroke')

    final_table = pd.merge(final_table_slowest_results, final_table_fastest_results, left_index=True, right_index=True)

    #df_output = pd.concat([final_table_fastest_results, final_table_slowest_results]).sort_index(kind='merge')
    print('*')
    return final_table


# **************************************************************************************************************
# Function  name: dot_plot_for_the_slowest_and_lastest_athletics
# input:
# return value: dot_plot
# ****************************************************************************************************************

def dot_plot_for_the_slowest_and_lastest_athletics(final_fastest_slowest_table):



    # df = pd.read_csv(data, sep="\s+", quotechar='"')
    # df = df.set_index("Country").sort_values("2015")
    # df["change"] = df["2015"] / df["1990"] - 1
    print('*')

    plt.figure(figsize=(12,6))
    y_range = np.arange(1, len(final_fastest_slowest_table.index) + 1) # Dynamic Y range of axis
    colors = np.where(final_fastest_slowest_table['Fastest percentage'] > final_fastest_slowest_table['Slowest percentage'], '#d9d9d9', '#d57883')
    plt.hlines(y=y_range, xmin=df['1990'], xmax=df['2015'],
               color=colors, lw=10)
    plt.scatter(df['1990'], y_range, color='#0096d7', s=200, label='1990', zorder=3)
    plt.scatter(df['2015'], y_range, color='#003953', s=200 , label='2015', zorder=3)
    for (_, row), y in zip(df.iterrows(), y_range):
        plt.annotate(f"{row['change']:+.0%}", (max(row["1990"], row["2015"]) + 4, y - 0.25))
    plt.legend(ncol=2, bbox_to_anchor=(1., 1.01), loc="lower right", frameon=False)

    plt.yticks(y_range, df.index)
    fontdict_input = {'fontsize': 19, 'weight': 'heavy', 'alpha': 0.9, 'color': 'Navy','fontname':'Franklin Gothic Medium Cond'}
    plt.title("The USA team improvement in their results across every Olympic swimming category", loc='left',fontdict=fontdict_input)
    plt.xlim(50, 300)
    plt.gcf().subplots_adjust(left=0.35)
    plt.tight_layout()
    plt.show()




if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../Data/Olympic_Swimming_1912to2020.csv')
    print('*')

    column_headers = list(df.columns.values)  # -> ['Location', 'Year', 'Distance (in meters)', 'Stroke', 'Relay?', 'Gender', 'Team', 'Athlete', 'Results', 'Rank']

    # Q - 1 : The swimming results of the USA team showed significant improvement across all fields -

    # Cleaning_the_data:
    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]

    # Apply the conversion function to the 'time' column    # '1:59.06'  ->119.06 , '00:01:53.410000' -> 113.41
    final_clean_table['Results (In seconds)'] = final_clean_table['Results'].apply(convert_time_to_seconds)
    final_clean_table = final_clean_table.loc[(final_clean_table["Distance (in meters)"] == '200m') & (final_clean_table['Gender'] == 'Men')]

    # I have added the list of years hard coded because we want to select only 8 teams q countries
    list_of_teams = ['USA','AUS','GBR','JPN','GER','CAN','GDR','HUN']

    for team_names in list_of_teams:
        mini_df_team = final_clean_table[final_clean_table['Team'] == team_names]
        final_table= preparing_the_olympic_data_for_the_dot_plot(mini_df_team)
        dot_plot_for_the_slowest_and_lastest_athletics(final_table )
    print('*')






