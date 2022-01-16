import pandas as pd
import os

line=int(input('input the line : '))

df = pd.read_csv('Fiche.csv') 
print(df)
print('Taille '+str(df.shape[0]))

df=df.drop(index=[line-1])

for i in range(line,df.shape[0]+1):
    df.at[i,'Id']=int(i)
    
print(df)
df.to_csv("Fiche.csv", index=False)

for j in range(1,52):
    os.remove('dataSet/User.'+str(line)+'.'+str(j)+'.jpg')

df = pd.read_csv('Fiche.csv') 
t=os.listdir('dataSet')
for i in t:
    splitted=i.split(".")
    
    print(splitted)
    
    if(int(splitted[1])>line):

        for j in range(1,52):
            os.rename(r'dataSet/User.'+str(splitted[1])+'.'+str(j)+'.jpg',r'dataSet/User.'+str(int(splitted[1])-1)+'.'+str(j)+'.jpg')
        line=int(splitted[1])    
        print(splitted)
