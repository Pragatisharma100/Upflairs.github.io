import pandas as pd
from datetime import datetime, timedelta

# Step 1: Read the CSV file
df = pd.read_csv('stock_data.csv')

# Step 2: Convert the date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Take today's date as input from the user
user_input = input("Enter today's date (YYYY-MM-DD): ")
today = datetime.strptime(user_input, '%Y-%m-%d')
previous_date = today - timedelta(days=1)

# Step 4: Filter the data based on the date range
filtered_df = df[(df['Date'] >= previous_date) & (df['Date'] <= today)]

# Step 5: Save the filtered data to a new CSV file
filtered_df.to_csv('filtered_stock_data.csv', index=False)

# Step 6: Print the filtered data
print(filtered_df)
