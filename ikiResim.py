import cv2
import matplotlib.pyplot as plt

#karıştırma 
img1 = cv2.imread("deniz.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("agac.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
"""
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)
"""

print(img1.shape) # boyut için
print(img2.shape)

img1 = cv2.resize(img1,(150,150))
print(img1.shape)

img2 = cv2.resize(img2,(150,150))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#karıştırılmış resim = alpha*img1 + beta* img2
blended = cv2.addWeighted(src1 = img1, alpha=0.6,src2 = img2 ,beta= 0.9, gamma = 0.9)
plt.figure()
plt.imshow(blended)


plt.show()              #..
cv2.waitKey(0)          #..
cv2.destroyAllWindows() #..