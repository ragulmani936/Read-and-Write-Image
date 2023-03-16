# READ AND WRITE AN IMAGE
## AIM
To write a python program using OpenCV to do the following image manipulations.
i) Read, display, and write an image.
ii) Access the rows and columns in an image.
iii) Cut and paste a small portion of the image.

## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Choose an image and save it as a filename.jpg
### Step2:
Use imread(filename, flags) to read the file.
### Step3:
Use imshow(window_name, image) to display the image.
### Step4:
Use imwrite(filename, image) to write the image.
### Step5:
End the program and close the output image windows.
## Program:
#### Developed By: Ragul M
#### Register Number: 212221230080
i) #To Read,display the image
```
import cv2
color_image=cv2.imread('rose.jpeg',1)
cv2.imshow('rose',color_image)
cv2.waitKey(0)
```
ii) #To write the image
```
import cv2
color_image = cv2.imread('sun2.jpg',1)
h = cv2.imwrite('rose.jpg',color_image)
cv2.imshow('ragul',color_image)
cv2.waitKey(0) 
```
iii) #Find the shape of the Image
```
import cv2
color_image = cv2.imread('sun2.jpg',1)
print(color_image.shape)
```
iv) #To access rows and columns
```
import random
import cv2
color_image = cv2.imread('rose.jpg',1)
for i in range(150):
    for j in range(color_image.shape[1]):
        color_image[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('sun2.jpg',color_image)
cv2.waitKey(0)
```
v) #To cut and paste portion of image
```
import cv2
color_image = cv2.imread('sun2.jpg',1)
part = color_image[300:400,300:400]
color_image[50:150,50:150] = part
cv2.imshow("hari",color_image)
cv2.waitKey(0)
```

## Output:

### i) Read and display the image
![dip11](1.png)


### ii)Write the image
![dip12](2.png)


### iii)Shape of the Image
![image](3.png)


### iv)Access rows and columns
![dip13](4.png)


### v)Cut and paste portion of image
![dip14](5.png)


## Result:
Thus the images are read, displayed, and written successfully using the python program.
