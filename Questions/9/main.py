import cv2

img = cv2.imread('image.jpg')
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Input grayscale img', grayscale_img)
cv2.waitKey(0)


rows, cols = grayscale_img.shape[:2]

with open('result.txt', 'w') as outfile:
    for row in range(rows):
        for col in range(cols):
            outfile.write(str(grayscale_img[row, col]) + ' ')
        outfile.write('\n')
