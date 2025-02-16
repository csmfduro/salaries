import pandas as pd
df = pd.read_csv('nwsl.csv')


# Print the last 3 rows of the DataFrame
# print(df.tail(3))

# Print the first 3 rows of the DataFrame
# print(df.head(3))

# Print the shape of the DataFrame
# print(df.shape)

# Print the headers of the DataFrame
# print(df.columns)

# Print the info of the DataFrame
# print(df.info())

# Read each Column of the DataFrame
# print(df['team'])

# Reading different columns of the DataFrame
# print(df[['team', 'city']])

# Reading each row of the DataFrame
# print(df.iloc[1])

# Reading multiple row of the DataFrame
# print(df.iloc[1:4])

# Reading a specific location (R,C)
# print(df.iloc[2,1])

# Find the row where the state is California
# print(df.loc[df['state'] == 'California'])

# Describing the DataFrame
# print(df.describe())

# Sorting the DataFrame
  # Sorting the DataFrame by the team
# print(df.sort_values('team'))
  # Sorting the DataFrame by the city in descending order
# print(df.sort_values('city', ascending=False))
  # Sorting the DataFrame by the city and teams
# print(df.sort_values(['city', 'team'], ascending=[1,0]))


# Making changes to the DataFrame
 # Adding a new column and adding the values of the other columns
'''df['Total'] = df['latitude'] + df['longitude']
print(df['Total'])'''

  # Removing a column
'''df = df.drop(columns=['Total'])  # This will remove the column 'Total' '''


