import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import dataframe_image as dfi
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


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
# Function  name: retrieving_the_number_of_medals_with_home_court_advantage
# input:
# return value:
# ****************************************************************************************************************
def retrieving_the_number_of_medals_with_home_court_advantage(final_clean_table):
    Unique_Location = list(final_clean_table['Location'].unique())
    # ['Tokyo', 'Rio', 'London', 'Beijing', 'Athens', 'Sydney', 'Atlanta', 'Barcelona', 'Seoul', 'Angeles', 'Moscow', 'Montreal', 'Munich', 'City', 'Rome', 'Melbourne', 'Helsinki', 'Berlin', 'Amsterdam', 'Paris', 'Antwerp', 'Stockholm']#
    Unique_Team = list(final_clean_table['Team'].unique())
    # ['ROC', 'USA', 'ITA', 'CHN', 'ESP', 'AUS', 'ROU', 'GBR', 'NED', 'BLR', 'HUN', 'SUI', 'POL', 'GUA', 'BUL', 'FRA', 'KOR', 'UKR', 'GER', 'AUT', 'JPN', '', 'SWE', '', 'BRA', 'LTU', 'NZL', 'TUN', 'GRE', 'CAN', 'ISR', 'IRL', 'HKG', 'BEL', 'CZE', 'DEN', 'RUS', 'KAZ', 'ISL', 'JAM', 'SGP', 'NOR', 'ZIM', 'NZ', 'NL', 'NLD', 'SRB', 'CUB', 'ZAF', 'TTO', 'BAH', 'VEN', 'KEN', 'PNG', 'SLO', 'CRO', 'SVK', 'ALG', 'ARG', 'CRC', 'PUR', 'MDA', 'BAR', 'EUN', 'SUR', 'Unified Team ', 'TCH', 'URS', 'GDR', 'FRG', 'YUG', 'SUN', 'BGR', 'COL', 'POR', 'CHE', 'MEX', 'ECU', 'PER', 'URU', 'EGY', 'PHI', 'LUX', 'ANZ']
    print('*')
    # Create a dictionary of the location of the Olympic took place and team
    dict_location_city = {
        "Beijing": 'CHN',
        "Tokyo": "JPN",
        "Rio": "BRA",
        "Atlanta": "USA",
        "London": "GBR",
        "Paris": "FRA",
        "Sydney": "AUS",
        "Barcelona": "ESP",
        "Melbourne": "AUS",
        "Montreal": "CAN",
        "Angeles": "USA",
        "London": "GBR",
        "Munich": "GRE",
        "Berlin": "GRE",
        "Athens": "GRE",
        "Seoul": "KOR",
        "Stockholm": "SWE",
        "Athens": "GRE",
        "Amsterdam": "NED",
        "Helsinki": "FIN",
        "Moscow": "RSA",
        "City": "MEX",
        "Antwerp": "BUL",
        "Rome": "GRE"}
    print('*')
    list_number_of_medals_home_court_advantage = []
    list_number_of_medals_before_home_court_advantage = []
    # We will be focusing on the best hosting team's home court:
    list_of_years = np.array([2012, 1972, 1988, 1956, 2000, 2020, 2008, 1980, 1956, 1936, 1984, 1996])
    list_of_years_minus_4 = list_of_years - 4
    List_of_best_home_courts = ['London', 'Munich', 'Seoul', 'Stockholm', 'Sydney', 'Tokyo', 'Beijing', 'Moscow',
                                'Melbourne', 'Berlin', 'Angeles', 'Atlanta']
    List_of_country_code = ['GBR', 'GRE', 'KOR', 'SWE', 'AUS', 'JPN', 'CHN', 'RSA', 'AUS', 'GRE', 'USA', 'USA']
    #first_3_places = [1, 2, 3]
    first_place_gold = [1]
    #second_place_silver = [2]
    # 1934 - Angeles - 10 medals
    for home_court_location, code_country, olympic_year_before in zip(List_of_best_home_courts, List_of_country_code,
                                                                      list_of_years_minus_4):
        # Home court info:
        home_court_data = final_clean_table[final_clean_table['Location'] == home_court_location]
        home_court_data_code_country = home_court_data[home_court_data['Team'] == code_country]
        home_court_data = home_court_data_code_country[home_court_data_code_country['Rank'].isin(first_place_gold)] # first_3_places
        number_of_medals = home_court_data.shape[0]
        list_number_of_medals_home_court_advantage.append(number_of_medals)

        # Before home court (One Olympic games before) - number of medals:
        before_home_court_data = final_clean_table.loc[final_clean_table['Year'] == olympic_year_before, :]
        before_home_court_data_code_country = before_home_court_data.loc[before_home_court_data['Team'] == code_country, :]
        home_court_data_3_places = before_home_court_data_code_country.loc[
            before_home_court_data_code_country['Rank'].isin(first_place_gold)]
        number_of_medals_before = home_court_data_3_places.shape[0]
        list_number_of_medals_before_home_court_advantage.append(number_of_medals_before)
        print('*')
    final_table = pd.DataFrame({'Host City': List_of_best_home_courts,
                                #'Country code': List_of_country_code,
                                'Medals before getting home court advantage': list_number_of_medals_before_home_court_advantage,
                                'Medals with home court advantage': list_number_of_medals_home_court_advantage})


    # Initialize a list to store the indices of rows to be dropped
    rows_to_drop = []

    for index, row in final_table.iterrows():
        if row['Medals before getting home court advantage'] == 0 and row['Medals with home court advantage'] == 0:
            rows_to_drop.append(index)

    # Drop the rows using the list of indices
    final_table = final_table.drop(rows_to_drop)
    print('*')
        #if final_table.loc[,'Medals before getting home court advantage'] == 0 &
    #final_table.at[10, 'Medals with home court advantage'] = 34


    #result = final_table.style.apply(func=relevant_columns_highlighter, subset=['Host Cities of the Olympic Games']).hide_index()
    #dfi.export(result,'Users\Gil\PycharmProjects\Olympic_games_in_swimming_1\Olympic_games_in_swimming\Olympic_games_question\question_5\output_image.png')
    #dfi.export(result, filename='output_images/home_court_image.png')

    dfi.export(final_table, 'home_court_gold_image.png')

    #
    print('*')
    #C:\Users\Gil\PycharmProjects\Olympic_games_in_swimming_1\Olympic_games_in_swimming\Olympic_games_question\question_5\output_image
    return final_table
###############################################################################################################################################
# Function  name: need to connect this part to the function up here
# input:
# return value:
###############################################################################################################################################
# # Step 1: Prepare the bar chart data and labels
# data = [10, 12, 15, 14, 12, 18]
# #labels = ['Bar 1', 'Bar 2', 'Bar 3', 'Bar 4', 'Bar 5', 'Bar 6']
# x = [0,1, 2, 3, 4, 5]
#
# # Step 2: Prepare the small images (Replace 'image1.png', 'image2.png', and 'image3.png' with your actual image file paths)
# image_paths = ['beijig_2008.png', 'london_2012.png', 'sydney_2000.png','stockholm_1956.png','tokyo_2020.png','los_angeles_1984.png']
# images = [plt.imread(path) for path in image_paths]
#
# plt.figure(facecolor='gainsboro')
# # Step 3: Create the bar chart
# #plt.bar(range(len(data)), data, tick_label=labels)
#
# # Step 4: Add the images under each bar
# for i, image in enumerate(images):
#     imagebox = OffsetImage(image, zoom=0.45)  # Adjust the 'zoom' parameter to scale the image size
#     ab = AnnotationBbox(imagebox, (i, 0), xybox=(0, -60), xycoords='data', boxcoords="offset points", frameon=False)
#     plt.gca().add_artist(ab)
#
#
#
#
# #bar plot
# plt.bar(x, height = data, width = 0.6)
#
# # Set the title and labels for the chart
# plt.title("Number of medals with home court advantage")
# #plt.xlabel("Home Court")
# plt.ylabel("Values")
#
#
# # Show the plot
# plt.show()




# **************************************************************************************************************
# Function  name:
# input:
# return value:
# ****************************************************************************************************************
if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    # df = pd.read_csv('/home/shay_diy/PycharmProjects/Olympic_games/data/Olympic_Swimming.csv')
    print('*')

    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]
    print('*')

    retrieving_the_number_of_medals_with_home_court_advantage(final_clean_table)
    print('*')










