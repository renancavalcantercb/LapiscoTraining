import cv2
import numpy as np
from numba import njit
seed = (0, 0)

@njit
def region_growing(image, seed=None):
    rows, cols = image.shape[:2]
    xc, yc = seed
    segmented = np.zeros_like(image)
    segmented[xc, yc] = 255
    current_found = 0
    previous_points = 1

    while previous_points != current_found:

        previous_points = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                if segmented[row, col] == 255:
                    if image[row - 1, col - 1] < 127:
                        segmented[row - 1, col - 1] = 255
                        current_found += 1
                    if image[row - 1, col] < 127:
                        segmented[row - 1, col] = 255
                        current_found += 1
                    if image[row - 1, col + 1] < 127:
                        segmented[row - 1, col + 1] = 255
                        current_found += 1
                    if image[row, col - 1] < 127:
                        segmented[row, col - 1] = 255
                        current_found += 1
                    if image[row, col + 1] < 127:
                        segmented[row, col + 1] = 255
                        current_found += 1
                    if image[row + 1, col - 1] < 127:
                        segmented[row + 1, col - 1] = 255
                        current_found += 1
                    if image[row + 1, col] < 127:
                        segmented[row + 1, col] = 255
                        current_found += 1
                    if image[row + 1, col + 1] < 127:
                        segmented[row + 1, col + 1] = 255
                        current_found += 1

    return segmented

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed

        # Update the seed point
        seed = (y, x)


def get_centroid(image):
    xc, yc = 0, 0

    rows, cols = image.shape[:2]
    count = 0
    for row in range(rows):
        for col in range(cols):
            if image[row, col] == 255:
                xc += row
                yc += col
                count += 1

    xc = int(xc / count)
    yc = int(yc / count)

    return xc, yc


if __name__ == '__main__':
    img = cv2.imread('image.jpg')
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('Original Image', 1)
    cv2.imshow('Original Image', grayscale_img)
    cv2.setMouseCallback('Original Image', mouse_event)
    cv2.waitKey(0)
    segmented_img = region_growing(grayscale_img, seed)
    xc, yc = get_centroid(segmented_img)
    rows, cols = segmented_img.shape[:2]
    new_img = np.zeros([rows, cols, 3], np.uint8)
    new_img[np.where(segmented_img == 255)] = [255, 0, 0]
    cv2.circle(new_img, (yc, xc), 5, (0, 255, 0), -1)
    cv2.imshow('Segmented image', new_img)
    cv2.waitKey(0)