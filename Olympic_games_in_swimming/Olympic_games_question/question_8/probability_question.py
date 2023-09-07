import pandas as pd



if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')
    #df = pd.read_csv('/home/shay_diy/PycharmProjects/Olympic_games/data/Olympic_Swimming.csv')

    print('*')

    data_without_na = df.dropna(how='all')
    cleaner_df = data_without_na.dropna(subset=['Results'])
    # Removing rows with the values : 'Disqualified','Did not start','Did not finish'
    removing_words = ['Disqualified', 'Did not start', 'Did not finish', '36.4est']
    final_clean_table = cleaner_df[~cleaner_df['Results'].isin(removing_words)]



    # Now lets receive information about the swimmers who won the gold medals
    gold_medals_info = final_clean_table[final_clean_table['Rank'] == 1]

    list_of_hosting_games= list(gold_medals_info['Location'].unique())
    print('*')
    gold_medals_info_in_Tokyo = gold_medals_info[gold_medals_info['Location'] == 'Tokyo']
    number_of_japans_won = gold_medals_info_in_Tokyo[gold_medals_info['Team'] == 'JPN']
    print('*')
    ##
    # Create a Mapping table --> dictionary of the location of the Olympic took place and team
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



    for key, value in dict_location_city.items():
        print(f'Key: {key}, Value: {value}')
    # Filter the data for the specific country hosting the Games
    #host_country
    #hosted_games = final_clean_table[final_clean_table['Location'] == host_country]

    # Calculate the number of times the host country won the most gold medals in swimming
    #winning_swimming_events = hosted_games[hosted_games['Sport'] == 'Swimming']
    #most_gold_medals = winning_swimming_events['Country'].value_counts().max()

    # Calculate the total number of times the host country hosted the Games
    total_hosted_games = len(hosted_games)

    # Calculate the probability
    probability = most_gold_medals / total_hosted_games

    # Print the probability
    # print(f"The probability of {host_country} winning