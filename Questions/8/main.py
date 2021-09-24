import cv2
img = cv2.imread('image.jpg')


grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Input grayscale img', grayscale_img)


rows, cols = grayscale_img.shape[:2]
double_sized_img = cv2.resize(grayscale_img, (2 * rows, 2 * cols))
half_sized_img = cv2.resize(grayscale_img, (int(rows/2), int(cols/2)))


cv2.imshow('Double sized img', double_sized_img)
cv2.imshow('Half sized img', half_sized_img)

cv2.waitKey(0)

cv2.imwrite('double_sized_img.jpg', double_sized_img)
cv2.imwrite('half_sized_img.jpg', half_sized_img)