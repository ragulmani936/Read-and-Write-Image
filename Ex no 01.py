#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[2]:


import cv2
color_image=cv2.imread('rose1.jpeg',1)
cv2.imshow('rose',color_image)
cv2.waitKey(0)


# In[3]:


import cv2
color_image = cv2.imread('rose1.jpeg',1)
h = cv2.imwrite('rose.jpeg',color_image)
cv2.imshow('ragul',color_image)
cv2.waitKey(0) 


# In[4]:


import cv2
color_image = cv2.imread('rose1.jpeg',1)
print(color_image.shape)


# In[5]:


import random
import cv2
color_image = cv2.imread('rose1.jpeg',1)
for i in range(150):
    for j in range(color_image.shape[1]):
        color_image[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('rose.jpeg',color_image)
cv2.waitKey(0)


# In[6]:


print(color_image.shape)


# In[7]:


import cv2
color_image = cv2.imread('rose1.jpeg',1)
part = color_image[50:100, 50:100]
color_image[130:180, 130:180]=part
cv2.imshow("ragu",color_image)
cv2.waitKey(0)


# In[8]:


import cv2
color_image = cv2.imread('rose1.jpeg',1)
h = cv2.imwrite('rose.png',color_image)
cv2.imshow('ragul',color_image)
cv2.waitKey(0) 


# In[ ]:




