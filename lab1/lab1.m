p=[2 4]; %create a matrix p
q=[5 7]; %create a matrix q
add= p+q %add matrices p and q
mul= p.*q %multiply matrices p and q

D = 0:0.5:10 %create a matrix with elements 0-10 with an interval of 0.5

row=[ 1 2 3] %create a row matrix
col= [1;2;3] %create a column matrix

z=complex(3,7) %create a complex vector
transpose(z) %find transpose of complex vector
ctranspose(z) %find conjugate transpose of complex vector
length(z) %find length of vector

m=[1 2 3];
n=[5 6 7];
dotprod= dot(m,n) %find dot product of m and n matrices
crossprod= cross(m,n) %find cross product of m and n matrices
dot(crossprod, m) %prove that cross product of m and n is orthogonal to it by proving their dot product is 0
dot(crossprod, n)

V= 1:2:52 %create a vector [ 1...47 49 52]

A= magic(3) %create a 3x3 matrix
A(2,:) %extract second row of matrix
A(:,3) %extract 4th column of matrix
transpose(A) %find transpose of matrix
inv(A) %find inverse of matrix
A(1:2, 1:3) %extract submatrix of A having 1,2 rows and 1,3 columns
A([1 3],:) = A([3 1],:) %interchange 1st and 3rd rows of A
A([2 3], :) %extract all rows except 1st row from A

R= rand(3,4) %create any random matrix
10.*R %scale the random matrix by 10
R>1 %this returns a 3x4 null matrix

dia= [1 2 3] %create a diagonal matrix
diag = diag(dia)

eye(3) %create identity matrix
zeros(3) %create a null matrix
x= rand(4,1) + i*rand(4,1); %create a unitary matrix
x= x/norm(x)
x'*x

C= eye(6) %create a 6x6 identity matrix
e= diag(C) %extract the diagonal elements of C

s= [0:0.1:2*pi] %create a sinusoidal signal and plot it
a= sin(s)
plot(s,a)

t= -0.02:0.001:0.0625; %create a rectangular signal and plot it
y= 0.5*square(2*pi*30*t);
plot(t,y)
