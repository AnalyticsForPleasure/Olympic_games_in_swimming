import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import PIL
import matplotlib.image as image
import seaborn


# **************************************************************************************************************
# Function  name: preparing_the_data
# input:
# return value:
# ***************************************************************************************************************

def preparing_the_data(final_table):
    final_table_counter = final_table['Athlete'].value_counts()
    final_table_counter = final_table_counter.reset_index()
    final_table_counter.rename(columns={"Athlete": 'Athlete_Name', "count": 'Number_of_madels'}, inplace=True)
    result = final_table_counter.loc[final_table_counter['Number_of_madels'] > 2, :]  ## we are intresting at the swimmers who won more than 2 medals
    print('*')
    return result


# **************************************************************************************************************
# Function  name: adding_advance_bar_plot
# input:
# return value:
# ***************************************************************************************************************
def adding_advance_bar_plot(final_table_counter, Gender_Athlete, font_prop_ticks, font_prop_title):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(19, 7))

    unique_list_of_number_of_medals = list(final_table_counter["Number_of_madels"].unique())
    unique_list_of_number_of_medals = unique_list_of_number_of_medals[::-1]

    # TODO: need to continue from here
    for number_of_ned in unique_list_of_number_of_medals:
        filtered_df_name_athletes = final_table_counter.loc[final_table_counter['Number_of_madels'] == number_of_ned, :]['Athlete_Name']
        list_of_swimmers_on_one_bar= list(filtered_df_name_athletes)
        print('*')
    list_of_swimmers_on_one_bar = ['Kosuke Hagino', 'Danyon Joseph Loader', 'George Thomas Breen', 'Mike Burton', 'Norbert Rozsa',
                     'Pablo Morales', 'Duke Paoa Kahanamoku', 'Charlie Hickcox', 'John Phillips Naber', 'Nathan Adrian',
                     'Cesar Cielo Filho', 'Vladimir Salnikov', 'Tsuyoshi Yamanaka', 'Evgeny Rylov', 'Tom Dolan',
                     'Gustavo Borges', 'Gary Jr. Hall', 'Curtis Allen Myden', 'Caeleb Dressel',
                     'Alexander Timothy Mckee', 'Daniel Kowalski', 'Donald Arthur Schollander', 'David Andrew Wilkie',
                     'Florent Manaudou', 'Massimiliano Rosolino', 'Hakan Malmrot', 'Anders Holmertz']
    for i, swimmer in enumerate(list_of_swimmers_on_one_bar, 1):
        ax.annotate(
            swimmer, #f'* {swimmer}'
            xy=(-0.35, len(list_of_swimmers_on_one_bar) - i +0.5),
            xytext=(-0.35, len(list_of_swimmers_on_one_bar) - i+0.5),  # Adjust the vertical position
            arrowprops=dict(facecolor='white', shrink=0.2),
            fontsize=10, weight='bold', color='white',
            ha='left', va='center'
        )


    result_table = final_table_counter["Number_of_madels"].value_counts().reset_index()

    number_of_athletes_with_the_same_num_of_medals = list(result_table.loc[:, 'count'])
    number_of_medals = list(result_table.loc[:, 'Number_of_madels'])

    # Using a list comprehension to concatenate " Madals" to each element
    number_of_medals = [str(item) + " Madals" for item in number_of_medals]

    # Iterate through each category and assign a gradient color to each bar
    for i, value in enumerate(number_of_athletes_with_the_same_num_of_medals):
        if Gender_Athlete == 'Men':
            color = sns.color_palette("Blues", n_colors=len(number_of_athletes_with_the_same_num_of_medals))[i]
        else:
            color = sns.color_palette("flare", n_colors=len(number_of_athletes_with_the_same_num_of_medals))[i]
        sns.barplot(x=[number_of_medals[i]], y=[number_of_athletes_with_the_same_num_of_medals[i]], color=color, ax=ax)

    i = -0.5
    j = 0.3
    # Annotating the bar plot with the values (number_of_athletes_with_the_same_num_of_medals)
    for i in range(len(number_of_medals)):
        plt.annotate(f'{number_of_athletes_with_the_same_num_of_medals[i]} Swimmers',
                     (i, number_of_athletes_with_the_same_num_of_medals[i] + j), weight='bold', color='slategray',
                     size=22, fontproperties='Franklin Gothic Medium Cond')



    # Remove spines (top, right, bottom, and left) - remover the entire frame
    sns.despine(left=True)
    ax.yaxis.set_ticks([])

    plt.title(f"Amount of Medals won by {Gender_Athlete}'s swimmers", loc='center',
              fontproperties='Franklin Gothic Medium Cond', size=40,
              color='slategray', pad=30)  # }

    # plt.xlabel(number_of_medals, fontsize=17, color='Gray', fontname='Franklin Gothic Medium Cond')
    plt.savefig(f'gradient_bar_plot_{Gender_Athlete}.jpg', dpi=250, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('../../Data/Olympic_Swimming_1912to2020.csv')

    #    df = pd.read_csv('/home/shay_diy/PycharmProjects/Olympic_games/data/Olympic_Swimming.csv')

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

    first_3_places = [1, 2, 3]
    final_medals_table = df[df['Rank'].isin(first_3_places)]

    Gender = ['Men', 'Women']
    for Gender_Athlete in Gender:
        final_table = final_medals_table.loc[(final_medals_table['Gender'] == Gender_Athlete)]
        res = preparing_the_data(final_table)
        adding_advance_bar_plot(res, Gender_Athlete, font_properties_x_y_yticks, font_properties_title)
        print('*')
