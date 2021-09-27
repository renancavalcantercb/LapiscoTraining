import cv2
import numpy as np
import random
from numba import njit

@njit
def region_growing(image):
    rows, cols = image.shape[:2]
    segmented = np.zeros_like(image)
    num_objects = 0

    for ext_row in range(rows):
        for ext_col in range(cols):
            if segmented[ext_row, ext_col] == 0 and image[ext_row, ext_col] < 230:
                num_objects += 1
                segmented[ext_row, ext_col] = num_objects
                current_found = 0
                previous_points = 1

                while previous_points != current_found:
                    previous_points = current_found
                    current_found = 0

                    for row in range(rows):
                        for col in range(cols):
                            if segmented[row, col] == num_objects:
                                if image[row - 1, col - 1] < 230:
                                    segmented[row - 1, col - 1] = num_objects
                                    current_found += 1
                                if image[row - 1, col] < 230:
                                    segmented[row - 1, col] = num_objects
                                    current_found += 1
                                if image[row - 1, col + 1] < 230:
                                    segmented[row - 1, col + 1] = num_objects
                                    current_found += 1
                                if image[row, col - 1] < 230:
                                    segmented[row, col - 1] = num_objects
                                    current_found += 1
                                if image[row, col + 1] < 230:
                                    segmented[row, col + 1] = num_objects
                                    current_found += 1
                                if image[row + 1, col - 1] < 230:
                                    segmented[row + 1, col - 1] = num_objects
                                    current_found += 1
                                if image[row + 1, col] < 230:
                                    segmented[row + 1, col] = num_objects
                                    current_found += 1
                                if image[row + 1, col + 1] < 230:
                                    segmented[row + 1, col + 1] = num_objects
                                    current_found += 1

    return segmented, num_objects

if __name__ == '__main__':
    img = cv2.imread('image.jpg')
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original', grayscale_img)

    segmented_img, n_objects = region_growing(grayscale_img)
    rows, cols = segmented_img.shape[:2]
    new_img = np.zeros([rows, cols, 3], np.uint8)

    for n in range(n_objects):
        color = lambda: random.randint(0, 255)
        new_img[np.where(segmented_img == n + 1)] = [color(), color(), color()]


    cv2.imshow('Segmented img', new_img)
    cv2.waitKey(0)

