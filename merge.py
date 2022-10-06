import cv2
import numpy as np

#resmi içe aktar 
img = cv2.imread("OIP.jpg")
#cv2.imshow("orijinal", img)

#yan yana birleştir.
hor = np.hstack((img,img))
#cv2.imshow("horizontal",hor)

#alt alta birleştir
ver = np.vstack((img,img))
cv2.imshow("dikey",ver)


cv2.waitKey(0)           #...
cv2.destroyAllWindows()  #...