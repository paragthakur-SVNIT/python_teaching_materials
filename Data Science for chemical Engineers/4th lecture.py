import pandas as pd

data = {'Department': ['HR', 'IT', 'IT', 'HR', 'Sales', 'Finance', 'Sales'],
        'Employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        'Salary': [50000, 60000, 70000, 75000, 55000, 52000, 65000],
        'Experience': [3, 5, 7, 8, 2, 4, 6]}

df = pd.DataFrame(data)
#print("Original Data:\n", df)

# Group by department and get average salary
grouped = df.groupby('Department')
#print(grouped)
#print(grouped['Salary'].mean())  # Mean salary by department
#print(grouped['Experience'].sum())  # Total experience by department
#print("\nAverage Salary by Department:\n", df.groupby('Department')['Salary'].mean())

# Multiple aggregation
agg_data = grouped.agg({'Salary': ['mean', 'max'], 'Experience': 'sum'})
#print("\nAggregated Data:\n", agg_data)

summary = grouped.agg({
    'Salary': ['mean', 'max', 'min'],
    'Experience': ['mean', 'count']})

#print(summary)
#print(summary.sort_values(('Salary','mean'),ascending=False))

#print(grouped['Salary'].mean().sort_values(ascending=False))

# Custom function
def salary_range(x):
    return x.max() - x.min()

#print("\nSalary Range by Department:\n", grouped['Salary'].apply(salary_range))

# Pivot table
pivot = df.pivot_table(values='Salary', index='Department', aggfunc=['mean', 'max','min'])
print("\nPivot Table:\n", pivot)
