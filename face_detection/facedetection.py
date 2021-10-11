import os

import cv2
import numpy as np

alg="face_detection/haarcascade_frontalface_default.xml" 
haar_cascade=cv2.CascadeClassifier(alg)  
dataset="face_detection/datasets"  #making a folder in which our train data is captured
sub_data="your name"
path=os.path.join(dataset,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width,height)=(130,100)
  
cam=cv2.VideoCapture(0)



count=0
while count<51:
    print(count)
    (_,img)=cam.read()
    
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayimg,1.3,4)
    for x,y,w,h in face:

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        slice_face=grayimg[y:y+h ,x:x+w]
        face_resize=cv2.resize(slice_face,(width,height))
        cv2.imwrite("%s/%s.png" % (path,count),face_resize)
        count+=1
        

        
    cv2.imshow("face_detection",img)

print("50 imaged is saves to datasets")
    key=cv2.waitKey(10)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()
