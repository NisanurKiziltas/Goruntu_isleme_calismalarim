import cv2
#içe aktarma
img = cv2.imread("OIP.jpg")
print("resim boyutu: ",img.shape)
cv2.imshow("Orijinal",img)
cv2.waitKey(0)
#cv2.destroyAllWindows()

#yeniden boyutlandır
imgResized = cv2.resize(img,(820,420))
print("Resized Img Shape:",imgResized.shape)
cv2.imshow("Img Resized",imgResized)
cv2.waitKey(0)
#cv2.destroyAllWindows()

#kırp
imgCropped = img[:200,:300]
cv2.imshow("kırpık resim",imgCropped)
cv2.waitKey(0)
cv2.destroyAllWindows()