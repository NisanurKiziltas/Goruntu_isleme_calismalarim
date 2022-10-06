import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar 
img = cv2.imread("datai_team.jpg")
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.title("orijinal")

# erozyon //sınırları küçültür
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 2)
plt.figure(), plt.imshow(result, cmap ="gray"), plt.axis("off"),plt.title("erozyon")

#genişleme 
result2 = cv2.dilate(img,kernel,iterations = 1)
plt.figure(),plt.imshow(result2, cmap = "gray"),plt.axis("off"),plt.title("genişleme")




plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()