import cv2

# create classifiers
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

# read image, convert to grayscale, run classifier
image = cv2.imread('example.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face = face_classifier.detectMultiScale(image_gray, 1.1, 4)

# rectangles
for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
    roi_gray = image_gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)

# show final image
cv2.imshow('img', image)
cv2.waitKey()