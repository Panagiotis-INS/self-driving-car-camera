import cv2
import numpy as np
from tqdm import *
import matplotlib.pyplot as plt
####
# get file names of frames
frame=cv2.imread("./lines/wut.jpg")
######
#frame index
# plot frame
#plt.imshow(frame[:,:,0], cmap= "gray")
#plt.show()
# create a zero array
stencil = np.zeros_like(frame[:,:,0])
# specify coordinates of the polygon
polygon = np.array([[50,270], [220,160], [360,160], [480,270]])
# fill polygon with ones
cv2.fillConvexPoly(stencil, polygon, 1)
img = cv2.bitwise_and(frame[:,:,0], frame[:,:,0], mask=stencil)
# plot masked frame
#plt.imshow(img, cmap= "gray")
#plt.show()
ret, thresh = cv2.threshold(img, 130, 145, cv2.THRESH_BINARY)
# plot image
lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)

# create a copy of the original frame
dmy =frame[:,:,0].copy()

# draw Hough lines
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(dmy, (x1, y1), (x2, y2), (255, 0, 0), 3)
# plot frame
plt.figure(figsize=(10,10))
plt.imshow(dmy, cmap= "gray")
plt.show()