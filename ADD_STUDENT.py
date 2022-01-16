import csv
import pandas as pd
import time

df = pd.read_csv("Fiche.csv")
nom=input('Merci de saisir votre nom :')
Id=int(df.shape[0])

print("\n",df)
df.at[Id+1,'Name']=str(nom)
df.at[int(Id+1),'Id']=int(Id+1)

print("\n",df,"\n")

df.to_csv("Fiche.csv", index=False)



input(' [+]  Continue ? ...')    
        
