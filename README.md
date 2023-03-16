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
![1](https://user-images.githubusercontent.com/94881918/225675457-0367e4e5-28f7-459d-a023-7cf319099881.png)


### ii)Write the image
![1](https://user-images.githubusercontent.com/94881918/225675661-1346206b-4645-4c10-99bf-8dbab6dfe191.png)


### iii)Shape of the Image
![1](https://user-images.githubusercontent.com/94881918/225675758-7617867b-2dc4-4071-a23a-b6316d31e835.png)


### iv)Access rows and columns
![1](https://user-images.githubusercontent.com/94881918/225675898-48f6e09e-1517-4639-8238-cddf2be73d44.png)


### v)Cut and paste portion of image
![1](https://user-images.githubusercontent.com/94881918/225675976-b42f1114-e0c4-4ad4-ab11-f175d765ea54.png)


## Result:
Thus the images are read, displayed, and written successfully using the python program.
