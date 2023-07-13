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
        "Tokyo": "JPN",
        "Rio": "Mustang",
        "Atlanta":'USA',
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
        "Seoul":"", # South Korea
        "Stockholm": "GRE",
        "Athens":"GRE",
        "Amsterdam":"NED",
        "Helsinki":"FIN",
        "Moscow":"RSA",
        "Seoul":"FIN",
        "Antwerp":"BUL",
        "Rome":"GRE"}







