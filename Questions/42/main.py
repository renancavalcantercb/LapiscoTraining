import cv2

img = cv2.imread('image.jpg')
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny_img = cv2.Canny(grayscale_img, 80, 180)
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 20
params.maxArea = 40000
params.filterByCircularity = False
params.minCircularity = 0.1
params.filterByConvexity = False
params.minConvexity = 0.87
params.filterByInertia = False
params.minInertiaRatio = 0.8
params.minDistBetweenBlobs = 20

detector = cv2.SimpleBlobDetector_create(params)
blobs = detector.detect(canny_img)

print(len(blobs))

cv2.imshow('Input grayscale img', grayscale_img)
cv2.waitKey(0)