import cv2
import pandas as pd
import csv

df = pd.read_csv('Fiche.csv')

#Ouvrir la camera principal(index=0)
cam = cv2.VideoCapture(0)

#Utiliser le detecteur classificateur 'haarcascade_frontalface_default.xml' generee par la bibliotheque opencv
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Tant que l'utilisateur entre un nombredifferent que celui correspendant a ligne suivante de la base de donnees il affiche le mm message
id=int(input('Enter your id : '))


#le nombre qui etre incremente jusqu'a capturer le nombre suffisant des photos (dans notre cas 50)
Number=0
while(True):
    #lecture du visage capturer a travers la camera
    ret, img = cam.read()

    #Transformer les images capturees en forme grise
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,10,10),2)
        
        #incrementing Number 
        Number = Number + 1
        
        #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User."+str(id)+'.'+ str(Number) + ".jpg", gray[y:y+h,x:x+w])

        #Le titre de la fenetre 
        cv2.imshow('DataSetCreator developped by Mr ABDALLAOUI MAAN Amine',img)
        
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    
    # break if the number is morethan 50
    elif Number>50:
        break
    
cam.release()
cv2.destroyAllWindows()
