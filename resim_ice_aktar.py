import cv2

#içe aktarma
img = cv2.imread("OIP.jpg",0)#0 olması giri olması demek

#görselleştirme 
cv2.imshow("ilk resim",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("mess_gray.png",img)
    cv2.destroyAllWindows()