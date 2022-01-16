import csv, pandas as pd
import msvcrt


df = pd.read_csv('Fiche.csv')
print()
print(df)
print()


ans='a'
while(ans=='a'):
    ans=input('press q to EXIT : ')
    print('You can choose Id : '+str(int(df.shape[0])+1))
    break
        
