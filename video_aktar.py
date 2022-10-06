from pickle import TRUE
import cv2
import time

#video ismi 
video_name = "omer.mp4"

#video içe aktar(capture)
cap = cv2.VideoCapture(video_name)

print("video genişliği",cap.get(3))
print("video yüksekliği",cap.get(4))

if cap.isOpened() == False:
    print ("hata")

while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01)
        cv2.imshow("video",frame)
    else:
        break
    if cv2.waitKey(1) &0xFF == ("q"):
        break
cap.release()
cv2.destroyAllWindows()

