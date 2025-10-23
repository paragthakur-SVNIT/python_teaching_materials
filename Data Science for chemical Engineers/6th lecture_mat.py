import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [220, 340, 290, 410, 500, 480],
    'Expenses': [180, 300, 250, 370, 420, 400]
}

df = pd.DataFrame(data)
print(df)

# Line Plot
df.plot(x='Month', y=['Sales', 'Expenses'], kind='line', marker='o')
plt.title('Monthly Sales vs Expenses')
plt.xlabel('Month')
plt.ylabel('Amount (in $1000)')
plt.grid(True)
plt.show()

# Bar Plot
df.plot(x='Month', y='Sales', kind='bar', color='teal', legend=False)
plt.title('Monthly Sales')
plt.ylabel('Sales ($)')
plt.show()

# Histogram
df['Sales'].plot(kind='hist', bins=5, color='orange', edgecolor='black')
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.show()

# Boxplot
df[['Sales', 'Expenses']].plot(kind='box')
plt.title('Sales and Expenses Distribution')
plt.show()
