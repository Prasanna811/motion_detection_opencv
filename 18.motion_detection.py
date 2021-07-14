import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

while cap.isOpened():
    # absdiff calculates diff between two arrays
    diff = cv2.absdiff(frame1, frame2)
    # Convert to grayscale since Contours work well in grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Blurs an image using a Gaussian filter.
    # The function convolves the source image with the specified Gaussian kernel.
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Thresholding
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, 'Status: movement', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    cv2.imshow('feed', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
