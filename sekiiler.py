from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import cv2
import numpy as np

#resim oluştur
img = np.zeros((512,512,3),np.uint8)#siyah resim
print(img.shape)
#cv2.imshow("siyah",img)

#çizgi
#(resim,başlangıç noktası,bitiş noktası,renk)   
#renk (blue,green,red) = (0,0,255)=red
cv2.line(img,(0,90),(512,512),(0,255,200)) 
#cv2.imshow("cizgi",img)

#dikdörtgen
cv2.rectangle(img,(200,34),(256,256),(0,7,234),cv2.FILLED)
#cv2.imshow("REcTANGLE",img)

#daire
#(resim,merkez,yarı çap,renkm)
cv2.circle(img, (300,300),45,(55,20,234),cv2.FILLED)
#cv2.imshow("cember",img)

#metin
# (resim,başlangıç,font,kalınlık,renk)
cv2.putText(img,"resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(55,20,234))
cv2.imshow("cember",img)
cv2.waitKey(0)           #...
cv2.destroyAllWindows()  #...


