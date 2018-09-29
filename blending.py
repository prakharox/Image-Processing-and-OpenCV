import cv2
import os

#set base directory
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, "images")

#read image from directory
image1=cv2.imread(image_dir+'\\hands1.jpg',cv2.IMREAD_GRAYSCALE)
image2=cv2.imread(image_dir+'\\hands2.jpg',cv2.IMREAD_GRAYSCALE)

print('1:',image1)
print('2:',image2)

image3=cv2.add(image1,image2) # addition of images
image4=cv2.addWeighted(image1,0.5,image2,0.5,0) # alpha blending
cv2.imshow('image3',image3)
cv2.imshow('image4',image4)
print('4:',image4)

cv2.waitKey(0)
cv2.destroyAllWindows()