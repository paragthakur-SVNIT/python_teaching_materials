import pandas as pd  # Import the pandas library

# Create a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)  # Convert dictionary to DataFrame

# Display the DataFrame
print(df)

# Basic operations
#print(df.head())   # Show first 5 rows
#print(df.describe())  # Summary statistics
#print(df['Age'].mean())