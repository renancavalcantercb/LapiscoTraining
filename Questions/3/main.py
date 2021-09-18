import cv2

image = cv2.imread('image.jpg')

blue_channel, green_channel, red_channel = cv2.split(image)

cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)
cv2.waitKey(0)

cv2.imwrite('blue_channel.jpg', blue_channel)
cv2.imwrite('green_channel.jpg', green_channel)
cv2.imwrite('red_channel.jpg', red_channel)