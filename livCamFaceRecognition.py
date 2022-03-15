import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default')
# to capture video from webcam
cap = cv2.VideoCapture(0)
# to use a video file as input
# cap = cv2.VideoCapture('filename.mp4')
while True:
  # read the frame
  img = cap.read()
  # convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # detect the faces
  faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  # draw the rectangle around each face
  for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
  # display
  cv2.imshow('img', img)
  # stop if escape key is pressed
  k = cv2.waitKey(30) & 0xff
  if k==27:
    break
# release the VideoCapture object
cap.release()
