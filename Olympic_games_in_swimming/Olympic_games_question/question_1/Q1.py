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


def process_df(current_team):

    final_table = pd.DataFrame({'Team': [],
                                'Stroke': [],
                                'max_duration_time':[],
                                'min_duration_time':[],
                                'Improvement':[]})  # Fastest result , Slowest result

    unique_stroke = current_team['Stroke'].unique()
    min_duration_time_for_all_strokes = current_team['Results (In seconds)'].min()
    max_duration_time_for_all_strokes = current_team['Results (In seconds)'].max()

    groups = current_team.groupby('Stroke')
    for stroke_name, mini_df in groups:
        max_duration_time = mini_df['Results (In seconds)'].max()  # Slowest
        min_duration_time = mini_df['Results (In seconds)'].min()  # Fastest
        improvement = round(100 * ((max_duration_time - min_duration_time) / max_duration_time), 2)
        print(f'{stroke_name=}, {improvement=}')
        print('*')

    # x axis - (min_duration_time_for_all_strokes, max_duration_time_for_all_strokes)
    # plt.xlim(min_duration_time_for_all_strokes, max_duration_time_for_all_strokes)


    # df = df.set_index("Country").sort_values("2015")
    # df["change"] = df["2015"] / df["1990"] - 1

    plt.figure(figsize=(12,6))
    y_range = np.arange(1,len(unique_stroke)+1)
    colors = np.where(min_duration_time > max_duration_time, '#d9d9d9', '#d57883')
    plt.hlines(y=y_range, xmin=min_duration_time, xmax=max_duration_time, color=colors, lw=10)
    plt.scatter(min_duration_time, y_range, color='#0096d7', s=200, label='1990', zorder=3)
    plt.scatter(max_duration_time, y_range, color='#003953', s=200 , label='2015', zorder=3)

    # Adding the annotation for the improvement values
    for (_, row), y in zip(final_fastest_slowest_table.iterrows(), y_range):
        plt.annotate(f"{row['Improvement %']:+.0%}",
                     (max(row["Slowest_percentage"] - 0.05,
                          row["Fastest_percentage"]) + 1, y - 0.05))

    plt.yticks(y_range, df.index)
    plt.title("Energy productivity in selected countries and regions, 1990 and 2015\nBillion dollars GDP per quadrillion BTU", loc='left')
    plt.xlim(min_duration_time_for_all_strokes, max_duration_time_for_all_strokes)
    plt.gcf().subplots_adjust(left=0.35)
    plt.tight_layout()
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

    # I have added the list of years hard coded because we want to select only 8 teams q countries
    list_of_teams = ['USA', 'AUS', 'GBR', 'JPN', 'GER', 'CAN', 'GDR', 'HUN']

    for team_names in list_of_teams:
        mini_df_team = final_clean_table[final_clean_table['Team'] == team_names]
        print('#' * 25 + team_names + '#' * 25)
        process_df(mini_df_team)

