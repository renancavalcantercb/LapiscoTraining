import cv2
import numpy as np
from numba import njit
seed = (0, 0)

# @njit
def region_growing(image, seed=None):
    rows, cols = image.shape[:2]
    xc, yc = seed
    ref_color = image[xc, yc]
    segmented = np.zeros_like(image)
    segmented[xc, yc] = ref_color
    current_found = 0
    previous_points = 1

    while previous_points != current_found:

        previous_points = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                if np.array_equal(segmented[row, col], ref_color):
                    if np.array_equal(image[row - 1, col - 1], ref_color):
                        segmented[row - 1, col - 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row - 1, col], ref_color):
                        segmented[row - 1, col] = ref_color
                        current_found += 1
                    if np.array_equal(image[row - 1, col + 1], ref_color):
                        segmented[row - 1, col + 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row, col - 1], ref_color):
                        segmented[row, col - 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row, col + 1], ref_color):
                        segmented[row, col + 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row + 1, col - 1], ref_color):
                        segmented[row + 1, col - 1] = ref_color
                        current_found += 1
                    if np.array_equal(image[row + 1, col], ref_color):
                        segmented[row + 1, col] = ref_color
                        current_found += 1
                    if np.array_equal(image[row + 1, col + 1], ref_color):
                        segmented[row + 1, col + 1] = ref_color
                        current_found += 1

        cv2.imshow('Segmentation', segmented)
        cv2.waitKey(1)

    return segmented


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
        seed = (y, x)


if __name__ == '__main__':
    img = cv2.imread('image.jpg')
    img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)
    cv2.namedWindow('Original img', 1)
    cv2.imshow('Original img', img)
    cv2.setMouseCallback('Original img', mouse_event)
    cv2.waitKey(0)
    segmented_img = region_growing(img, seed)

    cv2.imshow('Segmented img', segmented_img)
    cv2.waitKey(0)