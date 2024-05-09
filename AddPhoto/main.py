import cv2
import numpy as np

ataturk = cv2.imread("Ataturk.jpg")
sinem = cv2.imread("Sinem_Baskan.jpg")

if ataturk.shape != sinem.shape:
    # Eğer boyutlar farklıysa, 'sinem' görüntüsünü 'ataturk' görüntüsünün boyutlarına getir
    sinem = cv2.resize(sinem, (ataturk.shape[1], ataturk.shape[0]))

weightedSum = cv2.addWeighted(ataturk,0.5,sinem,0.4,0)

cv2.imshow("Eklenmiş Resim",weightedSum)

if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()