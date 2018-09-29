import cv2
import os

#set base directory
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, "images")

#read image from directory
image=cv2.imread(image_dir+'\\hands1.jpg')
noise=image.copy()

cv2.imshow('image',image)

m=(50,50,50)
s=(60,60,60)
cv2.randn(noise,m,s)
noisy_image=cv2.add(image,noise)

cv2.imshow('noisy image', noisy_image)

cv2.waitKey(0)
cv2.destroyAllWindows()