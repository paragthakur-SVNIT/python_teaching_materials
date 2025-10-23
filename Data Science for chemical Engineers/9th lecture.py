import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name': ['Amit', 'Bhavna', 'Chirag', 'Deepa', 'Esha', 'Farhan', 'Gita', 'Hiren'],
    'Age': [25, 28, 34, 29, 40, 35, 30, 38],
    'Department': ['HR', 'Finance', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [40000, 52000, 61000, 58000, 72000, 45000, 50000, 67000],
    'Experience': [2, 4, 8, 6, 12, 5, 4, 10]
}

df = pd.DataFrame(data)
print(df)
# Summary statistics
print(df.describe())

# Check data types
print(df.info())

# Unique values in categorical column
print(df['Department'].value_counts())

# Mean salary by department
print(df.groupby('Department')['Salary'].mean())
plt.hist(df['Age'], bins=5)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

plt.boxplot(df['Salary'])
plt.title('Salary Distribution')
plt.ylabel('Salary')
plt.show()

plt.scatter(df['Experience'], df['Salary'])
plt.title('Salary vs Experience')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.show()

df.groupby('Department')['Salary'].mean().plot(kind='bar')
plt.title('Average Salary by Department')
plt.ylabel('Average Salary')
plt.show()

corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

# Visual correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()