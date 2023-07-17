import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# **************************************************************************************************************
# Function  name:
# input: How home field advantage gives Olympic hpst countries an Edge?
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



    Unique_Location = list(final_clean_table['Location'].unique())
    #['Tokyo', 'Rio', 'London', 'Beijing', 'Athens', 'Sydney', 'Atlanta', 'Barcelona', 'Seoul', 'Angeles', 'Moscow', 'Montreal', 'Munich', 'City', 'Rome', 'Melbourne', 'Helsinki', 'Berlin', 'Amsterdam', 'Paris', 'Antwerp', 'Stockholm']#
    Unique_Team = list(final_clean_table['Team'].unique())
    # ['ROC', 'USA', 'ITA', 'CHN', 'ESP', 'AUS', 'ROU', 'GBR', 'NED', 'BLR', 'HUN', 'SUI', 'POL', 'GUA', 'BUL', 'FRA', 'KOR', 'UKR', 'GER', 'AUT', 'JPN', '', 'SWE', '', 'BRA', 'LTU', 'NZL', 'TUN', 'GRE', 'CAN', 'ISR', 'IRL', 'HKG', 'BEL', 'CZE', 'DEN', 'RUS', 'KAZ', 'ISL', 'JAM', 'SGP', 'NOR', 'ZIM', 'NZ', 'NL', 'NLD', 'SRB', 'CUB', 'ZAF', 'TTO', 'BAH', 'VEN', 'KEN', 'PNG', 'SLO', 'CRO', 'SVK', 'ALG', 'ARG', 'CRC', 'PUR', 'MDA', 'BAR', 'EUN', 'SUR', 'Unified Team ', 'TCH', 'URS', 'GDR', 'FRG', 'YUG', 'SUN', 'BGR', 'COL', 'POR', 'CHE', 'MEX', 'ECU', 'PER', 'URU', 'EGY', 'PHI', 'LUX', 'ANZ']
    print('*')

    # Create a dictionary of the location of the Olympic took place and team
    dict_location_city = {
        "Beijing": 'CHN',
        "Tokyo": "JPN",
        "Rio": "BRA",
        "Atlanta":"USA",
        "London": "GBR",
        "Paris": "FRA",
        "Sydney":"AUS",
        "Barcelona": "ESP",
        "Melbourne": "AUS",
        "Montreal":"CAN",
        "Angeles":"USA",
        "London": "GBR",
        "Munich": "GRE",
        "Berlin": "GRE",
        "Athens":"GRE",
        "Seoul":"KOR",
        "Stockholm": "SWE",
        "Athens":"GRE",
        "Amsterdam":"NED",
        "Helsinki":"FIN",
        "Moscow":"RSA",
        "City":"MEX",
        "Antwerp":"BUL",
        "Rome":"GRE"}
    print('*')

    # we will be focusing over the best hosting team home court :

    list_of_years = np.array([1984, 1996, 2012, 1972, 1988, 1956, 2000, 2020, 2008, 1980, 1956, 1936])
    list_of_years_minus_4 = list_of_years - 4
    List_of_best_home_courts = ['Angeles','Atlanta','London','Munich','Seoul','Stockholm','Sydney','Tokyo','beijing','Moscow','Melbourne','Berlin']
    List_of_country_code = ['USA','USA','GBR','GRE','KOR','SWE','AUS','JPN','CHN','RSA','AUS','GRE']

    first_3_places = [1, 2, 3]

    for home_court_location, code_country,olypic_year_before in zip(List_of_best_home_courts, List_of_country_code, list_of_years_minus_4 ):

        # Home court info:
        home_court_data = final_clean_table[final_clean_table['Location'] == home_court_location]
        home_court_data_code_country = home_court_data[home_court_data['Team']== code_country]
        home_court_data = home_court_data_code_country[home_court_data_code_country['Rank'].isin(first_3_places)]
        number_of_medals = home_court_data.shape[0]

        # Before home court ( One Olymplic games before ) - number of medals :
        before_home_court_data = final_clean_table[final_clean_table['Year'] == olypic_year_before]
        before_home_court_data = before_home_court_data[before_home_court_data['Team'] == code_country]
        home_court_data_3_places = before_home_court_data[before_home_court_data['Rank'].isin(first_3_places)]
        number_of_medals_before = home_court_data_3_places.shape[0]
        print('*')




        print('*')

    #GBR











