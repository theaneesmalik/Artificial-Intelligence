!pip install deepface
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2 as cv
import os

image_path = '/WhatsApp Image 2022-01-30 at 5.49.26 PM.jpeg'
img = cv.imread(image_path)
result = DeepFace.analyze(img)
print('\033[1m'+'Emotions : ]')
print('Angry : ', result['emotion']['angry'])
print('Disgust : ', result['emotion']['disgust'])
print('Fear : ', result['emotion']['fear'])
print('Happy : ', result['emotion']['happy'])
print('Sad : ', result['emotion']['sad'])
print('Surprise : ', result['emotion']['surprise'])
print('Neutral : ', result['emotion']['neutral'])
print('Gender : ', result['gender'])
print('Race : ', result['race'])
print('Age : ', result['age'])\
from google.colab import drive
drive.mount('/content/drive')