import cv2
import os

def blend(a,b,c):
    d=cv2.add(a*c,b*(1-c))
    return d

#set base directory
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, "images")

#read image from directory
image1=cv2.imread(image_dir+'\\hands1.jpg')
image2=cv2.imread(image_dir+'\\hands2.jpg')

cv2.imshow('image1',image1)
cv2.imshow('image2',image2)
#convert to grayscale
#im1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
#im2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)


#blending
im3=cv2.add(image1*0.5,image2*0.5)
cv2.imshow('im3',im3)

cv2.waitKey(0)
cv2.destroyAllWindows()