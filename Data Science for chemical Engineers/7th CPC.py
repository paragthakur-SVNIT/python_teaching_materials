#7th CPC
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/Users/paragthakur/Desktop/Teaching Material/Data Science for chemical Engineers/Salary.csv', header=2)
print(df.columns); print(df.head()); print(df.info()); print(df.describe())
print(df['1']); print(df.iloc[:,1]); 
print(df[df['6']==47600])
print(df[df['6']!=47600])
print(df[(df['1']==35400) | (df['6']==35400)])
print(df[(df['1']<=25000) & (df['6']<=50000)])
print(df[~((df['1']<=25000) & (df['6']<=50000))])
print(df)
df.rename(columns={'1': 'Level 1','2':'Level 2','3':'Level 3',
                   '4':'Level 4','5':'Level 5','6':'Level 6',
                   '7':'Level 7','8':'Level 8','9':'Level 9',
                   '10':'Level 10','11':'Level 11','12':'Level 12',
                   '13':'Level 13','14':'Level 14','15':'Level 15',
                   '16':'Level 16','17':'Level 17','18':'Level 18',}, inplace=True)
#print(df.columns)
#print(df)
j=df.T
#print(j)
#print(df.max(axis=1))
(df.sort_values(by='3', ascending=False))
j=df.isna().max() 
df.fillna(j, inplace=True)
#df[['1','3']].plot(kind='line',marker='*')
plt.scatter(df['Level'], df['1'], label='Stage 1', color='blue')
plt.scatter(df['Level'], df['3'], label='Stage 3', color='red')
plt.title("Comparison of Stage 1 and Stage 3 Pay Levels")
plt.xlabel("Stages of yearly Increment")
plt.ylabel("Basic Pay (₹)")
plt.show()
#print(df)
plt.show()