import cv2
cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', grayscale_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break