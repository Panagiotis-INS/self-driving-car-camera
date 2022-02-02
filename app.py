import os
import re
#from tkinter import Frame
import cv2
import numpy as np
from tqdm import *
import matplotlib.pyplot as plt
from time import sleep
import json
import requests
####
def send_to_server(found,go):
    print(found,go)
    #http://middleware:8351
    data={'found':found,'go':go}
    url = 'http://20.0.0.202:8351/api/camera/'
    requests.post(url, data = data)
#
def main():
    vc=cv2.VideoCapture(0)#'/dev/video2')
    ######
    while(1):
        return_value, image = vc.read()
        # create a zero array
        stencil =np.zeros_like(image[:,:,0])
        # specify coordinates of the polygon
        polygon = np.array([[50,270], [220,160], [360,160], [480,270]])
        # fill polygon with ones
        cv2.fillConvexPoly(stencil, polygon, 1)
        img = cv2.bitwise_and(image[:,:,0], image[:,:,0], mask=stencil)
        ret, thresh = cv2.threshold(img, 130, 145, cv2.THRESH_BINARY)
        # plot image
        lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)

        # create a copy of the original image
        dmy =image[:,:,0].copy()
        # draw Hough lines
        try:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                print(x1,x2,y1,y2)
                cv2.line(dmy, (x1, y1), (x2, y2), (255, 0, 0), 3)
                direction=''
                if(x1+x2>dmy[1].size):
                    #print(1) # go right
                    direction='r'
                else:
                    direction='l'
                    #print(0) # go left
            #print("YES")
            
            send_to_server(1,direction)
        except:
            send_to_server(0,0)
            #print("No")
        # plot image
        #plt.figure(figsize=(10,10))
        #plt.imshow(dmy, cmap= "gray")
        #plt.show()

if __name__=='__main__':
    main()
