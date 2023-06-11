import matplotlib.pyplot as plt
import numpy as np
import probscale
import seaborn
import pandas as pd
import dataframe_image as dfi


if __name__ == '__main__':

    N = 15
    np.random.seed(0)
    x = np.random.normal(size=N) + np.random.uniform(size=N)
    fig, ax = plt.subplots(figsize=(8, 4))
    fig = probscale.probplot(x, ax=ax, bestfit=True, estimate_ci=True,
                             line_kws={'label': 'BF Line', 'color': 'b'},
                             scatter_kws={'label': 'Observations'},
                             problabel='Probability (%)')
    ax.legend(loc='lower right')
    ax.set_ylim(bottom=-2, top=4)
    seaborn.despine(fig)
    plt.savefig('probability_example.jpg',dpi=450, bbox_inches='tight')
    plt.show()
########################################################################################################################

