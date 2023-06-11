import pandas as pd

# # Create a sample dataframe
# df = pd.DataFrame({'Time': ['00:01:08.200000', '00:02:30.500000', '00:00:45.750000']})
# print('*')
# # 52.19   00:00:52.19
# # Define the conversion function
# def convert_to_seconds(time_str):
#     h, m, s = map(float, time_str.split(':'))
#     return 60 * 60 * h + 60 * m + s
#
# # Apply the conversion function to the 'Time' column
# df['Time'] = df['Time'].apply(lambda x: convert_to_seconds(x) if isinstance(x, str) else x)
#
# # Convert the values to seconds with one decimal place
# df['Time'] = df['Time'].round(1)
#
# # Output the modified dataframe
# print(df)
#


# Create a sample DataFrame
df = pd.DataFrame({'time': ['00:01:06.200000', '00:02:30.500000', '00:00:45.750000', 'abc', '00:01:08.200000']})

# Use regular expression to find cells with the specified time format
pattern = r'^\d{2}:\d{2}:\d{2}\.\d+$'
filtered_df = df[df['time'].str.contains(pattern)]

# Display the filtered DataFrame
print(filtered_df)
print('*')

