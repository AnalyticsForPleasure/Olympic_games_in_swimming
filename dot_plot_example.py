# import libraries
import matplotlib.pyplot as plt
import pandas as pd
from textwrap import wrap
#plt.style.use(['unhcrpyplotstyle','dotplot'])

#load and reshape the data
df = pd.read_csv('https://raw.githubusercontent.com/GDS-ODSSS/unhcr-dataviz-platform/master/data/change_over_time/dot_plot.csv')
df = df.pivot_table(index=['location','order'], columns='period', values='percent', sort=False)
df = df.reset_index()

#sort values in descending order
ordered_df = df.sort_values(by='order', ascending=False)

#wrap the long labels
y_labels = ordered_df['location']
wrapped_label = [ '\n'.join(wrap(l, 20)) for l in y_labels ]
plt.style.use('seaborn') # this time we add this labrary
#plot the chart
fig, ax = plt.subplots()
plt.scatter(ordered_df['before_covid'], wrapped_label, label='before_covid')
plt.scatter(ordered_df['first_months'], wrapped_label, label='first_months')
plt.hlines(y=wrapped_label, xmin=ordered_df['before_covid'], xmax=ordered_df['first_months'], color='#666666')

#set chart legend
ax.legend(labels = ["Before COVID-19", "First month of the crisis"], loc=(0,1.05), ncol=2)

#set chart title
ax.set_title('COVID-19 impact on poverty rates of informal workers', pad=50)

plt.style.use('seaborn') # this time we add this labrary
# xticks and xticklabel format
limit = plt.xlim(0, 1)
vals = ax.get_xticks()
ax.set_xticklabels(['{:,.0%}'.format(x) for x in vals])

#set chart source and copyright
plt.annotate('Source: UNHCR Refugee Data Finder', (0,0), (0, -25), xycoords='axes fraction', textcoords='offset points', va='top', color = '#666666', fontsize=9)
plt.annotate('©UNHCR, The UN Refugee Agency', (0,0), (0, -35), xycoords='axes fraction', textcoords='offset points', va='top', color = '#666666', fontsize=9)

#adjust chart margin and layout
fig.tight_layout()

#show chart
plt.show()