import cv2
import pandas as pd
import time


df = pd.read_csv("Fiche.csv")

def PRESENCE(Id):
    presence=GET_TIME()
    df.at[Id-1,'State']='Present'
    df.at[Id-1,'Time']=presence[3]
    df.at[Id-1,'Date']=presence[1]+' '+presence[2]+' '+presence[4]
       


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

#time
def GET_TIME():
    Temps= time.time()
    local_time = time.ctime(Temps)
    presence = local_time.split(" ")
    return presence


cam = cv2.VideoCapture(0)
font = (cv2.FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(250,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])

        if(conf<50):
            if(Id==df.at[Id-1,'Id']):
                PRESENCE(Id)
                name=df.at[Id-1,'Name']
               
        else:
            name="Unknown"
            
            
        cv2.putText(im,str(name), (x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250,10,10),2)
        df.to_csv("Fiche.csv", index=False)
    cv2.imshow('Recognition_Face developped by Mr ABDALLAOUI MAAN Amine',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


