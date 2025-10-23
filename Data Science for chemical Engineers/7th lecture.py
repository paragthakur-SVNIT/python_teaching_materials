import pandas as pd
import numpy as np

data = {
    'Employee': ['A', 'B', 'C', 'D', 'E'],
    'Salary': [50000, 60000, 75000, 80000, 65000],
    'Experience': [2, 4, 7, 8, 5],
    'Performance': [70, 80, 90, 85, 75]
}

df = pd.DataFrame(data)
print(df)

# Basic statistics
print("\nSummary Statistics:\n", df.describe())

# Mean, Median, Mode
print("\nMean Salary:", df['Salary'].mean())
print("Median Experience:", df['Experience'].median())
print("Mode of Performance:\n", df['Performance'].mode())

# Correlation and Covariance
print("\nCorrelation:\n", df[['Salary', 'Experience', 'Performance']].corr())
print("\nCovariance:\n", df[['Salary', 'Experience']].cov())

# Cumulative sum and product
df['Cumulative_Salary'] = df['Salary'].cumsum()
print("\nCumulative Salary:\n", df[['Employee', 'Cumulative_Salary']])

# Ranking employees by performance
df['Performance_Rank'] = df['Performance'].rank(ascending=False)
print("\nRanking:\n", df[['Employee', 'Performance', 'Performance_Rank']])

# Rolling mean (moving average of Salary)
df['Rolling_Mean_Salary'] = df['Salary'].rolling(window=3).mean()
print("\nRolling Mean Salary (3-period):\n", df)
