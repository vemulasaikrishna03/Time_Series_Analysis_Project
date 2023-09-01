import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Create an SQLite database and connect to it
conn = sqlite3.connect('time_series_data.db')

# Load time series data (replace 'your_data.csv' with your dataset)
data = pd.read_csv('your_data.csv')

# Store the data in the database
data.to_sql('time_series', conn, if_exists='replace', index=False)

# Query the data from the database (you can customize the SQL query)
query = '''
    SELECT date, value
    FROM time_series
    ORDER BY date;
'''
time_series = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Perform time series analysis and visualization
time_series['date'] = pd.to_datetime(time_series['date'])
time_series.set_index('date', inplace=True)

# Calculate rolling mean and rolling standard deviation
rolling_mean = time_series['value'].rolling(window=30).mean()
rolling_std = time_series['value'].rolling(window=30).std()

# Plot the time series data with rolling statistics
plt.figure(figsize=(12, 6))
plt.plot(time_series['value'], label='Original Data')
plt.plot(rolling_mean, label='Rolling Mean (30 days)')
plt.plot(rolling_std, label='Rolling Std Dev (30 days)')
plt.title('Time Series Analysis')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
