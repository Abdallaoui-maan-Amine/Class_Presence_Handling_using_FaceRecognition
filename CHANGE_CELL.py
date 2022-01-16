import csv, pandas as pd
from time import *
df = pd.read_csv('Fiche.csv')
print('Your DataFrame is : \n')


print(df)
row=int(input('\n  [+]  enter Please the cell number : '))
col=str(input('\n  [+]  Enter Please the column name : '))
new_value=input('\n  [+]  Enter Please the cell''s new value : ')

def CHANGE_CELL(row,col,new_value):
    df.at[row, col] = new_value

CHANGE_CELL(row,col,new_value)    
df.to_csv("Fiche.csv", index=False)
print(df)
input('\n\n   [+] Continue ?... ')
