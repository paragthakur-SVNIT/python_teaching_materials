import pandas as pd
import numpy as np

# Create time series data
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
df = pd.DataFrame({
    'Date': date_rng,
    'Temperature': [30, 32, 31, 29, 28, 35, 36, 33, 31, 30],
    'Humidity': [65, 70, 68, 75, 72, 60, 58, 63, 66, 69]
})

print("\nTime Series Data:\n", df)

# Set date as index
df.set_index('Date', inplace=True)

# Resampling: mean temperature per 3 days
print("\nResampled (3-day mean):\n", df.resample('3D').mean())

# Rolling average
df['Temp_MA'] = df['Temperature'].rolling(window=3).mean()
print("\nRolling Average (3-day):\n", df)

# Filtering by date
print("\nFiltered (Jan 3 to Jan 7):\n", df.loc['2023-01-03':'2023-01-07'])

# Export and import data
df.to_csv('weather_data.csv', index=True)
print("\nData saved to weather_data.csv")

df2 = pd.read_csv('weather_data.csv', parse_dates=['Date'])
print("\nImported Data from CSV:\n", df2.head())

# Export to JSON
df.to_json('weather_data.json', orient='records', lines=True)
print("\nData exported to JSON format.")
