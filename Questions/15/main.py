import cv2
cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(grayscale_image, 30, 100)
    cv2.imshow('Video', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break