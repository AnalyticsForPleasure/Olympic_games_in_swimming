import pandas as pd
import dataframe_image as dfi

if __name__ == '__main__':



    df = pd.DataFrame([[38.0, 2.0, 18.0, 22.0, 21, np.nan],[19, 439, 6, 452, 226,232]],
                      index=pd.Index(['Tumour (Positive)', 'Non-Tumour (Negative)'],
                                     name='Actual Label:'),
                      columns=pd.MultiIndex.from_product([['Decision Tree', 'Regression', 'Random'],['Tumour', 'Non-Tumour']], names=['Model:', 'Predicted:']))
    res= df.style
    dfi.export(res, filename='/output_images_olympic/res.png')
    print('*')

