
import os
import time
import sys



def Display(msg,t,var):
    for x in msg:
        if (var == 1):
            print('\033[1m' + x, end=' ')
        elif (var == 0):
            print('\033[1m' + x, end='')
        sys.stdout.flush()
        time.sleep(t)



def Clear():
    os.system( 'cls' )

ans=True
while (ans==True):
    Clear()
    Display("\n\n                ************      Face detection System Genered By ABDALLAOUI MAAN Amine       *********** \n\n",0.02,0)
    print('--> Please choose the option that you would executed : \n')
    print ("""
    1.Add a Student
    2.Edit DataFrame cell
    3.Delete a Student
    4.Create a dataSet
    5.Training DataSet
    6.Detector
    7.DataFrame consulting
    8.New day (Make all Absent)
    9.Exit/Quit
    """)
    choice=input("  [+]  What would you like to do? " )
    if choice=="1":
        os.system('python ADD_STUDENT.py')
        print("\nStudent Added")
        
        
    elif choice=="2":
        os.system('python CHANGE_CELL.py')
        print("\n Cell edited")
    
    elif choice=="3":
        os.system('python DELETE_STUDENT.py')
        print("\n  Student Deleted")
        
    elif choice=="4":
        os.system('python datasetCreator.py')
        print("\n DataSet Created")
        
    elif choice=="5":
        os.system('python Trainner.py')    
        print("\n Trainning finished")
        
    elif choice=="6":
        os.system('python detector.py')

    elif choice=="7":
        os.system('python DATA_CONSULTING.py')
        print('\n')

        
    elif choice=="8":
        os.system('python NEW_DAY.py')
        
    elif choice=="9":
        print("\n    Goodbye")
        print("    -->Thanks for using our face recognition system ...!")
        Display('\n     ***** MASTER INFORMATIQUE ET TELECOMMUNICATION *****\n\n',0.1,1)
        break
    
    elif choice !="":
        print("\n Not Valid Choice Try again") 
        
