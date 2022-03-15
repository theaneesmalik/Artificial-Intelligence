# front facial recognition
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#read the input image
img = cv2.imread('/1.jfif')
print(img)
#convert into grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# draw rectangle around the face
for(x,y,w,h) in faces:
  cv2.rectangle(img(x,y),(x+w,y+h),(255,0,0),2)
dim = (500,500)
resized = cv2.resize(img,dim)
# display the output
cv2.imshow('img',resized)
cv2.waitKey()