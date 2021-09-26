import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg')

grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
original_hist = np.zeros([256], np.uint8)
equalized_hist = np.zeros([256], np.uint8)

img_flat = grayscale_img.flatten()

for pixel in img_flat:
    original_hist[pixel] += 1


cdf = [sum(original_hist[:i + 1]) for i in range(len(original_hist))]
cdf = np.array(cdf)

normal_cdf = ((cdf - cdf.min())*255)/(cdf.max() - cdf.min())
normal_cdf = normal_cdf.astype('uint8')


equalized_img = normal_cdf[img_flat]

equalized_img = np.reshape(equalized_img, grayscale_img.shape)

plt.figure(1)
plt.subplot(221)
plt.imshow(grayscale_img, cmap='gray')
plt.subplot(222)
plt.hist(grayscale_img.ravel(), 256, [0, 256])
plt.subplot(223)
plt.imshow(equalized_img, cmap='gray')
plt.subplot(224)
plt.hist(equalized_img.ravel(), 256, [0, 256])
plt.show()
