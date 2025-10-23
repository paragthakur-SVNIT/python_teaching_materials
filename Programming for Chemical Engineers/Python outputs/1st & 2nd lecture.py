 
import pandas as pd
import numpy as np

data = {'Name': ['Aishwarya', 'Bhushan', 'Chetan','Dhananjay','Eknath','Faiz','Ganesh','NA'],
        'Age': [25,30,35,40,45,50,55,None], #np.nan
        'City': ['Surat','Mumbai','Pune','Surat','Chennai','Delhi','Kolkata','NA'],
        'Status':['Y','N','Y','N','Y','Y','N','NA']}

df = pd.DataFrame(data) 

#print(df)

#print(df.head(2))
#print(df.tail(3))
#print(df.columns)        #2nd lecture
#print(df.index)         #2nd lecture
print(df.iloc[1,:])     #2nd lecture
df.loc[0,"Name"]=3     #2nd lecture
df.loc[df["Name"]=="Chetan","Age"]=30
df.loc[df["Name"]=="Chetan","Name"]=30 
print(df)              #2nd lecture
#print(df.describe(include='all'))  # Summary statistics df.info()
print(df['Age'].mean())
print(df['Status'].value_counts())
#print(df.dropna(inplace=False))
df.drop("City", axis=1, inplace=True)  #2nd lecture
df.drop(0, axis=0, inplace=True)       #2nd lecture
df=df.drop(3)        #Similarly, fillna command can be used
print(df)
#df['Values']=df['Age']+10
df['Age']=df['Age']+10               #2nd lecture
#print(df)
#df.to_csv(r"C:\Users\YourName\Documents\Parag.csv", index=False)   # Windows
#df.to_csv(r"/Users/YourName/Documents/Parag.csv", index=False)     # Mac/Linux

#df.to_csv('Parag.csv', index=False)
#df = pd.read_excel("data.xlsx")
#k=pd.read_csv('Parag.csv')
#print(k) 
print(df[df["City"]=="Surat"])
print(df[(df["City"]=="Surat") & (df["Status"]=="N")])
print(df[(df["City"]=="Surat") | (df["Status"]=="N")])
print(df[df["City"].str.startswith("S")]) 
print(df[df["City"].str.endswith("i")])
print(df[df["City"].isin(["Surat","Mumbai", "Delhi"])])