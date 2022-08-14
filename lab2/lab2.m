
A=imread('image1.jfif');
Z= imread('image2.jfif');
imresize(Z, 0.003)
imagesc(A)
hold on
image([40 21], [7,34], Z)

imshow(A)
round(points)
length = round(points(2) - points(1))
breadth= round(points(2)- points(4))
size = length*breadth
crop= A(points(1):points(2), points(3):points(4), :);
image(crop)
%B=rgb2gray(A);
points= ginput(2);
round(x)
round(y)
Z= imread('image2.jfif');
round(points)
length = points(3) - points(1)
breadth= points(2)- points(4)
size = length*breadth
%C=imresize(B,0.5);
%figure, imshow(B), figure, imshow(C)
%rgb2gray(B)
%red= A(65,130,1)
%green=A(65,130,2)
%blue=A(65,130,3)
%imshow(red)
%imshow(green)
%imshow(blue)
%Z= imread('image2.jfif')
%imshow(A)
%hold on
%image([52 5], [5,52], Z)
%A(1)= min(floor(i(1)), floor(i(2)));
%A(2)= min(floor(i(3)), floor(i(4)));
%A(3)= min(floor(i(1)), floor(i(2)));
%A(4)= min(floor(i(3)), floor(i(4)));
%crop= Z(A(2):A(4), A(1) : A(3), :);
%image(crop)









