import cv2
img = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
laplace = cv2.Laplacian(grayscale_img, ddepth=cv2.CV_64F, ksize=3)

laplace = cv2.convertScaleAbs(laplace)

equalized_laplacian = cv2.equalizeHist(laplace)

cv2.imshow('Input grayscale img', grayscale_img)
cv2.imshow('Laplacian filter result', laplace)
cv2.imshow('Equalized Laplacian', equalized_laplacian)

cv2.waitKey(0)