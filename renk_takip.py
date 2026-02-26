import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Orjinal Goruntu', frame)
   
    cv2.imshow('Sadece Maviler', res) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
