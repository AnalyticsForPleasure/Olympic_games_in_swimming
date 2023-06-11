import pandas as pd

# # Create sample dataframes
# df1 = pd.DataFrame({'Column1': ['A', 'C', 'E'], 'Column2': [1, 3, 5]})
# df2 = pd.DataFrame({'Column1': ['B', 'D', 'F'], 'Column2': [2, 4, 6]})
# print('*')
#
# # Merge dataframes alternately
# merged_df = pd.concat([df1, df2], ignore_index=True)
# print('*')
#
# # Display the merged dataframe
# print(merged_df)



# Create sample dataframes
df1 = pd.DataFrame({'Column1': ['A', 'C', 'E'], 'Column2': [1, 3, 5]}, index=[1, 3, 5])
df2 = pd.DataFrame({'Column1': ['B', 'D', 'F'], 'Column2': [2, 4, 6]}, index=[2, 4, 6])
print('*')

# Merge dataframes alternately by index numbers
merged_df = pd.concat([df1.loc[1:6:2], df2.loc[2:6:2]])
print('*')
# Reset the index of the merged dataframe
merged_df.reset_index(drop=True, inplace=True)
print('*')
# Display the merged dataframe
print(merged_df)