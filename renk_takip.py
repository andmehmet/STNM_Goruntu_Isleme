import cv2
import numpy as np

# Kamerayı başlat (0 varsayılan kameradır)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı.")
        break

    # Görüntüyü HSV formatına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi renk için alt ve üst sınır değerleri
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    # Maskeyi oluştur (Mavi yerler beyaz, gerisi siyah)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Orijinal renkleri korumak için maskeyi orijinal görüntüye uygula
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Pencereleri göster
    cv2.imshow('Orjinal Goruntu', frame)
    # Maske penceresini kapattık, yerine orijinal renkli sonucu ekledik
    cv2.imshow('Sadece Maviler', res) 

    # 'q' tuşuna basınca döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()