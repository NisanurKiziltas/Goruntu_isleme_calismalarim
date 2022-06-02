"""
import cv2
img = cv2.imread("resim.jpg",0)
cv2.imshow("resim",img)
k=cv2.waitKey(0)
if k==27:
    # 27 = esc tuşu demek
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("gri.png", img) 
    #oluşturulan dosyayı kaydediyor
    cv2.destroyAllWindows()
    """
    
    #çizgi
    """
    import cv2
import numpy as np
img = np.zeros((720,1280,3), np.uint8)
img=cv2.line(img, (0,0), (500,500), (255,0,0),5)
cv2.imshow("resim",img)

k=cv2.waitKey(0)
if k==27:
    # 27 = esc tuşu demek
    cv2.destroyAllWindows()
    """
    
    #kare 
    """
    import cv2
import numpy as np
img = np.zeros((720,1280,3), np.uint8)
#img=cv2.line(img, (0,0), (500,500), (255,0,0),5)
img=cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.imshow("resim",img)

k=cv2.waitKey(0)
if k==27:
    # 27 = esc tuşu demek
    cv2.destroyAllWindows()

    """
    
    #çember 
    """
    import cv2
import numpy as np
img = np.zeros((720,1280,3), np.uint8)
#img=cv2.line(img, (0,0), (500,500), (255,0,0),5)
#img=cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
img = cv2.circle(img, (447,337), 63, (0,0,255),-1)

cv2.imshow("resim",img)

k=cv2.waitKey(0)
if k==27:
    # 27 = esc tuşu demek
    cv2.destroyAllWindows()
"""

#elips
"""
import cv2
import numpy as np
img = np.zeros((720,1280,3), np.uint8)
#img=cv2.line(img, (0,0), (500,500), (255,0,0),5)
#img=cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#img = cv2.circle(img, (447,337), 63, (0,0,255),-1)
img = cv2.ellipse(img, (700,256), (100,50), 0,0, 255, -1)

cv2.imshow("resim",img)

k=cv2.waitKey(0)
if k==27:
    # 27 = esc tuşu demek
    cv2.destroyAllWindows()
    
    """
    
    
#gri ressim kaydetme
"""
import cv2
#resmi tanıt
img = cv2.imread("resim.jpg",0)
# görselleştir
cv2.imshow("ilk resim",img)

k = cv2.waitKey(0) & 0xFF
if k == 27 :
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("doga_gray.png", img)
    cv2.destroyAllWindows()
    


"""

#video içe aktarma 
"""
import cv2
import time
#video ismini al 
video_name = "video.mp4"

#video içe aktar : capture ,cap
cap = cv2.VideoCapture(video_name)

print("genişlik : ", cap.get(3))
print("yükseklik :",cap.get(4))

if cap.isOpened() == False:
    print("hata")

while True :
    ret,frame = cap.read()
    if ret ==True:
        time.sleep(0.01)#kullanmazsak hızlı devam eder
        cv2.imshow("video", frame)
    else : break
    if cv2.waitKey(1) & 0xFF ==ord("q"):
      break  

cap.release() #stop capture
cv2.destroyAllWindows()

"""


#kamera input alma
"""
import cv2
cap = cv2.VideoCapture(0)
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

#video kaydet
#writer = cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fource("MJPG"),20,(width,height))
#writer=cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fourcc('m','p','4','v'),20,(width,height))

writer = cv2.VideoWriter("video_kaydı2.mp4",cv2.VideoWriter_fourcc(*'mp4v'),20,(width,height))

while True:
    ret,frame =cap.read()
    cv2.imshow("video", frame)
    #save
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap .release()
writer.release()
cv2.destroyAllWindows()

"""


























    
