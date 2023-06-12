import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import numpy as np


if __name__ == '__main__':


    plt.figure(figsize=[14, 10])
    fig, all_4_axis = plt.subplots(nrows=1, ncols=4, sharey=True) # 4 plots
    #plt.style.use('ggplot')
    #for index in range(1,4,1):

    all_4_axis[0].set_title('Men',fontsize=14,fontname='Franklin Gothic Medium Cond')
    all_4_axis[1].set_title('Women',fontsize=14,fontname='Franklin Gothic Medium Cond')
    all_4_axis[2].set_title('Men',fontsize=14,fontname='Franklin Gothic Medium Cond')
    all_4_axis[3].set_title('Women',fontsize=14,fontname='Franklin Gothic Medium Cond')
    plt.barh(['Bronze', 'Silver', 'Gold'], [2026493, 710887, 476658], color = 'Gray')
    #plt.barh(['India', 'Italy', 'Peru', 'Germany', 'Iran'], [265928, 235278, 199696, 186205, 173832], label = "Not safe zone", color = 'g')

    plt.suptitle('Freestyle VS Medley Relay', fontweight ="bold", fontsize=25,fontname='Franklin Gothic Medium Cond')

    #plt.savefig('2BarPlot.png')
    plt.show()