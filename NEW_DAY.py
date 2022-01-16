import csv, pandas as pd
import time

df = pd.read_csv('Fiche.csv')

for i in range(df.shape[0]):
    df.at[i,'State']='Absent'

    
df.to_csv("Fiche.csv", index=False)    
print(df)
time.sleep(1.5)
