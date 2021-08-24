import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while True:
    status, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    facedetection = face_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in facedetection:
        """ cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) """
        hh = int(h/2)
        ww = int(w/2)
        roi_gray = gray[y:y+hh, x:x+ww]
        
        eyedetection = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (x1, y1, w1, h1) in eyedetection:
            """ cv2.rectangle(roi_gray, (x, y), (x+w, y+h), (255, 0, 0), 2) """
            eye = roi_gray[y1:y1+h1, x1:x1+w1]

            _, thresh = cv2.threshold(eye, 10, 255, cv2.THRESH_BINARY_INV)
            contornos, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contornos = sorted(contornos, key=cv2.contourArea, reverse=True)

            for cnt in contornos :
                """ cv2.drawContours(eye, [cnt], -1, (255,0,0), 2) """
                (x2, y2, w2, h2) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x+x1+x2, y+y1+y2), (x+x1+x2+w2, y+y1+y2+h2), (255,255,0), 2)
                break
            cv2.imshow("eye GRAY",eye)

    cv2.imshow("CAMARA", frame)

    if cv2.waitKey(1) == 27 :
        cap.release()
        cv2.destroyAllWindows()
        break