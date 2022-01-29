import os
import re
from tkinter import Frame
import cv2
import numpy as np
from tqdm import *
import matplotlib.pyplot as plt
####
# get file names of frames
vc=cv2.VideoCapture(0)
#
return_value, image = vc.read()
######
#image index
# plot image
#plt.imshow(image[:,:,0], cmap= "gray")
#plt.show()
# create a zero array
stencil = np.zeros_like(image[:,:,0])
# specify coordinates of the polygon
polygon = np.array([[50,270], [220,160], [360,160], [480,270]])
# fill polygon with ones
cv2.fillConvexPoly(stencil, polygon, 1)
img = cv2.bitwise_and(image[:,:,0], image[:,:,0], mask=stencil)
# plot masked image
#plt.imshow(img, cmap= "gray")
#plt.show()
ret, thresh = cv2.threshold(img, 130, 145, cv2.THRESH_BINARY)
# plot image
lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)

# create a copy of the original image
dmy =image[:,:,0].copy()

# draw Hough lines
try:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(dmy, (x1, y1), (x2, y2), (255, 0, 0), 3)
    print("YES")
except:
    print("No")
# plot image
plt.figure(figsize=(10,10))
plt.imshow(dmy, cmap= "gray")
plt.show()