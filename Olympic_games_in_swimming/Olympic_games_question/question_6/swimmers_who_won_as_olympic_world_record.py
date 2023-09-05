import matplotlib.pyplot as plt
from matplotlib import transforms, pyplot as plt
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

# **************************************************************************************************************
# Function  name: prepering_the_data_pf_the_swimmers_who_won_a_olymplic_world_record
# input:
# return value:
# ****************************************************************************************************************
def prepering_the_data_pf_the_swimmers_who_won_a_olymplic_world_record(final_clean_table):

    final_men_table = final_clean_table.loc[ (final_clean_table['Gender'] == 'Men')]
    final_women_table = final_clean_table.loc[ (final_clean_table['Gender'] == 'Women')]

    final_men_table.sort_values(by = 'Year', inplace=True, ascending=True)
    final_women_table.sort_values(by = 'Year', inplace=True, ascending=True)
    print('*')

    world_olympic_record = pd.DataFrame({'Location':[],
                                         'Gender':[],
                                         'Distance (in meters)':[],
                                         'Stroke':[],
                                         'Team':[],
                                         'Athlete':[],
                                         'Results':[],
                                         'Results (In seconds)':[]})


    # Iterate over male and female data frames separately
    for gender, final_table in [('Men', final_men_table), ('Women', final_women_table)]:
        groupby_stroke = final_table.groupby("Stroke")

        for swimming_style, mini_df_style in groupby_stroke:
            grooupby_distance = mini_df_style.groupby("Distance (in meters)")

            # In the for loop below we will get a table of each gender who won first place in each event and each swimming distance
            for distance, mini_df_distance in grooupby_distance:
                final_medals_table = mini_df_distance[mini_df_distance['Rank'] == 1]
                # The sorting part is important in order to find the each time the new record breaker.
                final_medals_table.sort_values(by='Year', inplace=True, ascending=False) # True
                res = final_medals_table.reset_index()

                current_min = float('inf')

                # In the loop below, after we sorted the loop by 'Year' - we are willing to go backwards for finding the current_min - current best
                for value in res['Results (In seconds)'][::-1]:  # TODO :Need to check if it's correct here to go backwards, don't think it's correct
                    current_min = min(value, current_min)
                    current_Olympic_record = res[res['Results (In seconds)'] == current_min][['Location','Gender','Distance (in meters)', 'Stroke', 'Team', 'Athlete', 'Results', 'Results (In seconds)']]
                    world_olympic_record = pd.concat([world_olympic_record, current_Olympic_record], axis=0)

                world_breaker_holder = world_olympic_record['Athlete'].value_counts()
                print('*')
                if gender == 'Men':
                    men_world_breaker_holder = world_breaker_holder
                #else:

            # Continue with other actions or analyses you want to perform here

    # Now you have 'men_world_breaker_holder' containing the top record holders for men
    Top_men_world_breaker_holder = men_world_breaker_holder.head(n=10)
    final_result = Top_men_world_breaker_holder.reset_index()
    final_result.rename(columns={final_result.columns[0]: 'Swimmer name'}, inplace=True)
    final_result.rename(columns={final_result.columns[1]: 'Number of times broke world record'}, inplace=True)
    print('*')

    return final_result

# **************************************************************************************************************
# Function  name: rainbow_text
# input: matplotlib doesn't have a function for drawing text with different colors, let's implement it
# return value:
# ****************************************************************************************************************
def rainbow_text(x, y, text, colors, spacing=20, ax=None, **kw):
    colors = list(reversed(colors))
    t = ax.transData
    canvas = ax.figure.canvas

    for i, line in enumerate(reversed(text.split('\n'))):
        strings = line.split('||')
        for s, c in zip(strings, colors[i]):
            text = ax.text(x, y, s, color=c, transform=t, **kw)
            text.draw(canvas.get_renderer())
            ex = text.get_window_extent()
            t = transforms.offset_copy(text._transform, x=ex.width,
                                       units='dots')

        t = transforms.offset_copy(ax.transData, x=0, y=(i + 1) * spacing,
                                   units='dots')


# **************************************************************************************************************
# Function  name: prepering_the_data_pf_the_swimmers_who_won_a_olymplic_world_record
# input:
# return value:
# ****************************************************************************************************************
def creating_a_storytelling_bar_chart(res):
    # define colors
    '#030764'
    GRAY1, GRAY2, GRAY3 = '#231F20', '#414040', '#555655'
    GRAY4, GRAY5, GRAY6 = '#646369', '#76787B', '#828282'
    GRAY7, GRAY8, GRAY9 = '#929497', '#A6A6A5', '#BFBEBE'
    BLUE_1,BLUE_2, BLUE_3, BLUE_4, BLUE_5, BLUE_6 , BLUE_7, BLUE_8  = '#01153E','#030764','#174A7E', '#0343DF' ,  '#069AF3' , '#4A81BF', '#94B2D7', '#94AFC5',
    RED1, RED2 = '#C3514E', '#E6BAB7'
    GREEN1, GREEN2 = '#0C8040', '#9ABB59'
    ORANGE1 = '#F79747'
    # survey responses
    X = list(res.loc[:,'Swimmer name'])
    Y =  list( res.loc[:,'Number of times broke world record'])
    print('*')

    #plt.style.use('seaborn')
    # create new figure
    fig, ax1 = plt.subplots(figsize=(8.2, 4.2),  # width, height in inches
                            dpi=110)             # resolution of the figure

    # tune the subplot layout by setting sides of the figure
    fig.subplots_adjust(left=0.28, right=0.53, top=0.61, bottom=0.107)

    # draw horizontal bars
    ax1.barh(range(len(X)),
             Y,
             height=0.65,
             color=[GRAY1] + [GRAY2]*2 + [GRAY8]*3 + [GRAY2])

    # set the data limits for the y-axis and x-axis
    ax1.set_xlim([0, 80])
    ax1.set_ylim([-0.5, 6.5])

    # set properties for axes object
    plt.setp(ax1,
         xticks=[0, 15, 30, 30, 40,50],  # 5 x-ticks only 0 and 1
         xticklabels=['0','3', '6', '9', '12', '15'],#, '12', '14','16','18'],  # with n% labels
         yticks=np.arange(len(Y)),  # tick for all response
         yticklabels=X)  # with text labels
    print('*')
    # change the appearance of ticks, tick labels, and gridlines
    ax1.tick_params(top='on', bottom='off', left='off',labelbottom='on', labeltop='on')

    print('*')
    # configure y tick label appearance
    for item in ax1.get_yticklabels():
        item.set_fontsize(12)
    # use trasformations to shift y tick labels
    # left y labels slightly right, and right labels slightly left
    offset = transforms.ScaledTranslation(-0.06, 0.02, fig.dpi_scale_trans)
    item.set_transform(item.get_transform() + offset)
    print('*')

    # remove chart border
    ax1.tick_params(color=GRAY7)
    ax1.spines['top'].set_color(GRAY7)
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    print('*')





    # title the plot
    rainbow_text(-64, 10.4,
                 '$\\bf{Which\ swimmers\ hold\ the\ highest\ number\ of\ Olympic\ records?}$||'
                 ' (1912 - 2020)\n'
                 'AnalyticsForPleasure',
                 [[BLUE_3, BLUE_8], [BLUE_7]],
                 spacing=25,
                 ax=ax1,
                 fontsize=14.7)

    # survey question
    # rainbow_text(-86, 8.35,
    #              'In general, ||$\\bf{what\ attributes\ are\ the\ most\ '
    #              'important}$\n'
    #              'to you in selecting a service provider?',
    #              [[GRAY4, GRAY1], [GRAY4]],
    #              spacing=20,
    #              ax=ax1,
    #              fontsize=11.5)
    # ax1.text(-86, 7.5, '$\\it{(Choose\ up\ to\ 3)}$', color=GRAY7, fontsize=10)
    # ax1.text(-4, 7.5, '% selecting given attribute', color=GRAY7, fontsize=10)



    # Several swimmers have made their mark in Olympic history by holding multiple records.
    # Some notable names include Michael Phelps of the United States, who boasts a remarkable 23 Olympic gold medals and
    # numerous records, and Katie Ledecky, also from the United States, who has set numerous world records in freestyle
    # events. Additionally, Ian Thorpe of Australia and Kristin Otto of Germany have left their indelible marks on the
    # Olympic swimming record books. These extraordinary athletes have become legends in the world of swimming and have
    # set standards that inspire generations to come.


    # survey question
    rainbow_text(87.6, 5.5,
                 'Several swimmers have made their mark in\n'
                 'Olympic history by holding ||$\\bf{multiple\ records}$\n'
                 'Some notable names include ||$\\bf{Michael\ Phelps}$\n'
                 'States, who boasts a remarkable 23 Olympic\n'
                 'gold medals and numerous records, and Katie Ledecky,',
                 [[GRAY4], # second line
                 [GRAY4 , GRAY1], # first line
                  [GRAY4, GRAY1 ], # third line
                  [GRAY4],
                  [GRAY4,GRAY1 ]],# forth line
                 spacing=20,
                 ax=ax1,
                 fontsize=11.5)

        #  Ian Thorpe of Australia and Kristin Otto of Germany have left their indelible marks on the Olympic swimming record books

    # text note with initial hypothesis
    rainbow_text(87.6, -0.5,
                 '$\\bf{Ian\ Thorpe}$|| of Australia and ||$\\bf{ Kristin\ Otto}$ of Germany\n'
                 '$\\bf{have\ left\ their\ indelible\ marks}$, on the Olympic\n'
                 'swimming record books.\n'
                 'very important in the decision\n'
                 'making process, were both cited\n'
                 'less frequently as important attributes.',
                 [[GRAY1, GRAY4, GRAY1],
                  [GRAY1,GRAY4 ],
                  [GRAY4],
                  [GRAY4],
                  [GRAY4],
                  [GRAY4]],
                 spacing=20,
                 ax=ax1,
                 fontsize=11.5)

    ax1.text(59, 9.30, '       Number of OR \n ( = Olympic Records)', color=GRAY7, fontsize=9)



#These extraordinary athletes have become legends in the world of swimming and have set standards that inspire generations to come
    # rainbow_text(87.6, -0.5,
    #              #'$\\bf{Ian\ Thorpe}$|| of Australia and ||$\\bf{ Kristin\ Otto}$ of Germany\n'
    #              #'$\\bf{have\ left\ their\ indelible\ marks}$, on the Olympic\n'
    #              '$\\bf{These extraordinary athletes have become legends in the world of swimming}$||'
    #              #'world of swimming and have set standards that inspire generations to come\n'
    #              #'making process, were both cited\n'
    #              #'less frequently as important attributes.',
    #              [GRAY4],
    #               #[GRAY4]],
    #               # [GRAY4],
    #               # [GRAY4],
    #               # [GRAY4],
    #               # [GRAY4]],
    #              spacing=20,
    #              ax=ax1,
    #              fontsize=11.5)



#These extraordinary athletes have become legends in the world of swimming and have
# set standards that inspire generations to come
    # footnote with the data source
    ax1.text(-60, -2.1,
             'Data source: Kaggle website -  Datasets\n' # 
             'Olympic Swimming Results 1912 to 2020',
             fontsize=8.3,
             color=GRAY3)

    # Show the plot
    plt.show()
    print('*')


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
    final_clean_table['Results (In seconds)'] = final_clean_table['Results'].apply(convert_time_to_seconds)

    print('*')

    column_headers = list(final_clean_table.columns.values)

    res = prepering_the_data_pf_the_swimmers_who_won_a_olymplic_world_record(final_clean_table)
    creating_a_storytelling_bar_chart(res)
    print('*')
