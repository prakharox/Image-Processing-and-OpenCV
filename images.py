import os
from PIL import Image
import scipy.misc
import time
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, "images")

img1=Image.open(image_dir+'\\mandi.tif')
img2=Image.open(image_dir+'\\glass.png')
im=scipy.misc.imread(image_dir+'\\mandi.tif',flatten=False,mode='RGB')
print(im.shape)
red=im(:,:,0)
#img1.show()
#time.sleep(5.5)
#img2.show()
image_data1=list(img1.getdata())
image_data2=list(img2.getdata())
size1=img1.size
size2=img2.size
print(size1)
print(size2)