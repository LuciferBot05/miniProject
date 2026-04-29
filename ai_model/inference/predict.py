import serial
import time
import requests
arduino = serial.Serial('COM5',9600)
time.sleep(2)
import cv2
import numpy as np
from tensorflow.keras.models import load_model # pyright: ignore[reportMissingModuleSource]
model = load_model("../model/ewaste_classifier.h5")

labels = ["battery","cable","circuit_board","mobile"]

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    ret, frame = cap.read()

    img = cv2.resize(frame,(224,224))
    img = np.reshape(img,[1,224,224,3])

    prediction = model.predict(img)
    confidence = np.max(prediction)
    label = labels[np.argmax(prediction)]

    
    if confidence < 0.7:
     label = "No Object"

    if label != "No Object":

     requests.get(f"http://127.0.0.1:5000/update/{label}")

    if label == "battery":
        arduino.write(b'1')
    elif label == "cable":
        arduino.write(b'2')
    elif label == "mobile":
        arduino.write(b'3')
    elif label == "circuit_board":
        arduino.write(b'4') 

    

    
    if label == "battery":
        arduino.write(b'1')

    elif label == "cable":
        arduino.write(b'2')

    elif label == "mobile":
        arduino.write(b'3')

    elif label == "circuit_board":
        arduino.write(b'4')

    cv2.putText(frame,label,(20,50),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("E-Waste Detection",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
