import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import seaborn as sys

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
# Function  name: process_df
# input:
# return value:
# ****************************************************************************************************************
def process_df(current_team):
    data = {'Stroke': [],
            'max_duration_time': [],
            'min_duration_time': [],
            'Improvement': []}

    unique_stroke = current_team['Stroke'].unique()
    min_duration_time_for_all_strokes = current_team['Results (In seconds)'].min()
    max_duration_time_for_all_strokes = current_team['Results (In seconds)'].max()

    groups = current_team.groupby('Stroke')
    for stroke_name, mini_df in groups:
        max_duration_time = mini_df['Results (In seconds)'].max()  # Slowest
        min_duration_time = mini_df['Results (In seconds)'].min()  # Fastest
        improvement = round(100 * ((max_duration_time - min_duration_time) / max_duration_time), 2)
        data['Stroke'].append(stroke_name)
        data['max_duration_time'].append(max_duration_time)
        data['min_duration_time'].append(min_duration_time)
        data['Improvement'].append(improvement)
        print(f'{stroke_name=}, {improvement=}')

    data = pd.DataFrame(data)

    return data, min_duration_time_for_all_strokes, max_duration_time_for_all_strokes
# **************************************************************************************************************
# Function  name: creating_Cleveland_dot_plot
# input:
# return value:
# ****************************************************************************************************************
def creating_Cleveland_dot_plot(df, total_min_duration, total_max_duration, country_name,font_prop_title, font_prop_x_y_yticks):
    strokes = df['Stroke']
    #plt.style.use('seaborn')
    plt.figure(figsize=(22, 10))

    y_range = np.arange(1, len(strokes) + 1)
    colors = np.where(df['max_duration_time'] > df['min_duration_time'], '#d9d9d9', '#d57883')
    plt.hlines(y=y_range, xmin=df['min_duration_time'], xmax=df['max_duration_time'], color=colors, lw=10)
    plt.scatter(df['min_duration_time'], y_range, color='#0096d7', s=200, label='1990', zorder=3)
    plt.scatter(df['max_duration_time'], y_range, color='#003953', s=200, label='2015', zorder=3)


    small_left_shifting =2
    # Adding 3 annotations for the improvement value + min_duration_time + max_duration_time
    for (idx_row, row), y in zip(df.iterrows(), y_range):
        plt.annotate(text=f"Improvement \n     {row['Improvement']:.2f}%",
                     xy=(((row['min_duration_time'] + row['max_duration_time']) / 2) - small_left_shifting, y + 0.05)) # positioning "improvement" labels.

        plt.annotate(text=f"{row['min_duration_time']:.2f}", xy=(row['min_duration_time'], y - 0.12))
        plt.annotate(text=f"{row['max_duration_time']:.2f}", xy=(row['max_duration_time'], y - 0.12))

    plt.title(f"The improvement of the {country_name} team in each Olympic swimming events - Men's 200m",
              loc='center',
              fontdict=font_prop_title ,
              fontname=font_prop_title['fontname'],
              pad=35)

    plt.legend(labels=["Best score by the team", "Worst score by the team"],loc=(0, 1.01)  ,ncol=2)  # loc=(0, 1.07), ncol=2) # loc="upper right"
    plt.xlabel('Time duration in seconds',font_prop_x_y_yticks)
    plt.yticks(ticks=y_range ,labels = strokes, fontdict=font_prop_x_y_yticks)
    #plt.ylabel('Stroke')
    plt.xlim(total_min_duration - 5, total_max_duration + 5)
    plt.gcf().subplots_adjust(left=0.35)
    plt.tight_layout()

    plt.savefig(f'Cleveland_dot_plot_{country_name}.jpg', dpi=250, bbox_inches='tight')

    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    print('*')

    # -> ['Location', 'Year', 'Distance (in meters)', 'Stroke', 'Relay?', 'Gender', 'Team', 'Athlete', 'Results', 'Rank']

    column_headers = list(df.columns.values)

    # Cleaning_the_data:
    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]

    # Apply the conversion function to the 'time' column    # '1:59.06'  ->119.06 , '00:01:53.410000' -> 113.41
    final_clean_table['Results (In seconds)'] = final_clean_table['Results'].apply(convert_time_to_seconds)
    final_clean_table = final_clean_table.loc[
        (final_clean_table["Distance (in meters)"] == '200m') & (final_clean_table['Gender'] == 'Men')]

    font_properties_x_y_yticks = {'fontsize': 20,
                       'weight': 'heavy',
                       'ha': 'right',
                       'alpha': 0.9,
                       'color': 'Gray',
                       'fontname': 'Franklin Gothic Medium Cond'
                       }
    font_properties_title = {'fontsize': 24,
                             'weight': 'heavy',
                             'ha': 'right',
                             'alpha': 0.9,
                             'color': 'navy',
                             'fontname': 'Franklin Gothic Medium Cond'
                            }
    # I have added the list of years hard coded because we want to select only 8 teams q countries
    list_of_country_teams = ['USA', 'AUS', 'GBR', 'JPN', 'GER', 'CAN', 'GDR', 'HUN']

    for country_name in list_of_country_teams:
        mini_df_team = final_clean_table[final_clean_table['Team'] == country_name]
        print('#' * 25 + country_name + '#' * 25)
        df, min_duration, max_duration = process_df(mini_df_team)
        creating_Cleveland_dot_plot(df, min_duration, max_duration, country_name,font_properties_title,font_properties_x_y_yticks)
