import numpy as np 
import cv2 
import matplotlib.pyplot as plt 

# read original image 
image = cv2.imread("image1.jpg") 
cimg = image
# finds the circles in the grayscale image using the Hough transform
circles = cv2.HoughCircles(image=cimg, method=cv2.HOUGH_GRADIENT, dp=0.9,minDist=80, param1=110, param2=39, maxRadius=70)
for co, i in enumerate(circles[0, :], start=1):
    # draw the outer circle in green
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle in red
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
# print the number of circles detected
print("Number of circles detected:", co)
# save the image, convert to BGR to save with proper colors
# cv2.imwrite("coins_circles_detected.png", cimg)
# show the image
plt.imshow(cimg)
plt.show()
