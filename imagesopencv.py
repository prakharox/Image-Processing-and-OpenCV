import cv2
import os

#set base directory
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, "images")

#read image from directory
image1=cv2.imread(image_dir+'\\hands1.jpg')
image2=cv2.imread(image_dir+'\\hands2.jpg')

#read image sizes
height, width, channels=image1.shape
print(height,width,channels)

height,width,channels=image2.shape
print(height, width, channels)

#convert to grayscale
im1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
im2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
cv2.imshow('im1',im1)
cv2.imshow('im2',im2)

#image-processing
im3=im1+im2
cv2.imshow('image3',im3)
im4=im1/2+im2/2
cv2.imshow('image4',im4)
im5=(im1+im2)/2
cv2.imshow('image5',im5)

cv2.waitKey(0)
