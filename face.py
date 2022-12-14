# Importing OpenCV package
import cv2

# Loading the required haar-cascade xml classifier file
face_ = cv2.CascadeClassifier('/Users/raghadbaeshen/PycharmProjects/OpencvPython/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/Users/raghadbaeshen/PycharmProjects/OpencvPython/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while cap.isOpened():

    ret, img = cap.read()
    print(ret)
    # Converting image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_.detectMultiScale(gray, 1.3, 5)
    
# Iterating through rectangles of detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
