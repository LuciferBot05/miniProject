import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("ewaste_classifier.h5")

labels = ["battery","circuit_board","mobile","cable"]

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    img = cv2.resize(frame,(224,224))
    img = np.reshape(img,[1,224,224,3])

    prediction = model.predict(img)

    label = labels[np.argmax(prediction)]

    cv2.putText(frame,label,(20,50),
    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("E-Waste Detection",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
