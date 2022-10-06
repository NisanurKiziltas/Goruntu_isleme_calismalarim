import cv2
import numpy as np
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img_vis)

print(img.shape)

img_hist = cv2.calcHist([img],channels = [0], mask = None, histSize = [256], ranges = [0,256])
print(img_hist.shape)
plt.figure(), plt.plot(img_hist)

color = ("b","g","r")
plt.figure()
for i,c in enumerate(color):
    hist = cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256] )
    plt.plot(hist,color = c)






plt.show()