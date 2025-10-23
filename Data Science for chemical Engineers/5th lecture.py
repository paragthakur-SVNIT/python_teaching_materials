import pandas as pd

# DataFrames for merge
df1 = pd.DataFrame({'EmpID': [1, 2, 3, 4],
                    'Name': ['Aishwarya', 'Bhushan', 'Chetan', 'Dhananjay'],
                    'Department': ['HR', 'Finance', 'IT', 'IT']})

df2 = pd.DataFrame({'EmpID': [3, 4, 5],
                    'Salary': [70000, 80000, 60000]})

print("Left DataFrame:\n", df1)
print("\nRight DataFrame:\n", df2)

# Inner Join
inner_join = pd.merge(df1, df2, on='EmpID', how='inner')
print("\nInner Join:\n", inner_join)

# Left Join
left_join = pd.merge(df1, df2, on='EmpID', how='left')
print("\nLeft Join:\n", left_join)

# Outer Join
outer_join = pd.merge(df1, df2, on='EmpID', how='outer')
print("\nOuter Join:\n", outer_join)

# Concatenation example
df3 = pd.DataFrame({'EmpID': [6, 7],
                    'Name': ['Eknath', 'Faiz'],
                    'Department': ['HR', 'Finance']})

concat_df = pd.concat([df1, df3], ignore_index=True)
print("\nConcatenated DataFrame:\n", concat_df)
