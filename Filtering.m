image=imread('cameraman.tif');
imshow(image);
hsize=31;
sigma=5;
h=fspecial('gaussian',hsize,sigma);
surf(h);%plot h as a surface
imagesc(h);%see the image h
outim=imfilter(image,h);%apply filter
imshow(outim)
