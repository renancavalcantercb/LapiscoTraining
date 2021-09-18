import cv2

img = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

median_img = cv2.medianBlur(grayscale_img, ksize=5)
blur_img = cv2.blur(grayscale_img, ksize=(5, 5))

cv2.imshow('Input grayscale img', grayscale_img)

cv2.imshow('Median filter result', median_img)
cv2.imshow('Blur filter result', blur_img)
cv2.waitKey(0)

cv2.imwrite('median_filter_result.jpg', median_img)
cv2.imwrite('blur_filter_result.jpg', blur_img)