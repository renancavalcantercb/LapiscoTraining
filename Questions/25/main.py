import cv2
import numpy as np
from numba import njit

img = cv2.imread('image.png')
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
segmented = np.zeros_like(grayscale_img)
seed = (0, 0)
event_count = 0


@njit
def region_growing(image, image_marked, seed=None):
    rows, cols = image.shape[:2]
    current_found = 0
    previous_points = 1

    while previous_points != current_found:

        previous_points = current_found
        current_found = 0
        for row in range(rows):
            for col in range(cols):
                if image_marked[row, col] == 1:
                    if image[row - 1, col - 1] < 230:
                        image_marked[row - 1, col - 1] = 1
                        current_found += 1
                    if image[row - 1, col] < 230:
                        image_marked[row - 1, col] = 1
                        current_found += 1
                    if image[row - 1, col + 1] < 230:
                        image_marked[row - 1, col + 1] = 1
                        current_found += 1
                    if image[row, col - 1] < 230:
                        image_marked[row, col - 1] = 1
                        current_found += 1
                    if image[row, col + 1] < 230:
                        image_marked[row, col + 1] = 1
                        current_found += 1
                    if image[row + 1, col - 1] < 230:
                        image_marked[row + 1, col - 1] = 1
                        current_found += 1
                    if image[row + 1, col] < 230:
                        image_marked[row + 1, col] = 1
                        current_found += 1
                    if image[row + 1, col + 1] < 230:
                        image_marked[row + 1, col + 1] = 1
                        current_found += 1

                if image_marked[row, col] == 2:
                    if image[row - 1, col - 1] < 230:
                        image_marked[row - 1, col - 1] = 2
                        current_found += 1
                    if image[row - 1, col] < 230:
                        image_marked[row - 1, col] = 2
                        current_found += 1
                    if image[row - 1, col + 1] < 230:
                        image_marked[row - 1, col + 1] = 2
                        current_found += 1
                    if image[row, col - 1] < 230:
                        image_marked[row, col - 1] = 2
                        current_found += 1
                    if image[row, col + 1] < 230:
                        image_marked[row, col + 1] = 2
                        current_found += 1
                    if image[row + 1, col - 1] < 230:
                        image_marked[row + 1, col - 1] = 2
                        current_found += 1
                    if image[row + 1, col] < 230:
                        image_marked[row + 1, col] = 2
                        current_found += 1
                    if image[row + 1, col + 1] < 230:
                        image_marked[row + 1, col + 1] = 2
                        current_found += 1

                if image_marked[row, col] == 3:
                    if image[row - 1, col - 1] < 230:
                        image_marked[row - 1, col - 1] = 3
                        current_found += 1
                    if image[row - 1, col] < 230:
                        image_marked[row - 1, col] = 3
                        current_found += 1
                    if image[row - 1, col + 1] < 230:
                        image_marked[row - 1, col + 1] = 3
                        current_found += 1
                    if image[row, col - 1] < 230:
                        image_marked[row, col - 1] = 3
                        current_found += 1
                    if image[row, col + 1] < 230:
                        image_marked[row, col + 1] = 3
                        current_found += 1
                    if image[row + 1, col - 1] < 230:
                        image_marked[row + 1, col - 1] = 3
                        current_found += 1
                    if image[row + 1, col] < 230:
                        image_marked[row + 1, col] = 3
                        current_found += 1
                    if image[row + 1, col + 1] < 230:
                        image_marked[row + 1, col + 1] = 3
                        current_found += 1

    return image_marked


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global seed
        global event_count
        global segmented

        event_count += 1

        segmented[y, x] = event_count


if __name__ == '__main__':
    cv2.namedWindow('Mark object 1', 1)
    cv2.imshow('Mark object 1', grayscale_img)
    cv2.setMouseCallback('Mark object 1', mouse_event)

    cv2.waitKey(0)

    segmented_img = region_growing(grayscale_img, segmented)
    rows, cols = segmented_img.shape[:2]
    new_img = np.zeros([rows, cols, 3], np.uint8)
    new_img[np.where(segmented_img == 1)] = [0, 0, 255]
    new_img[np.where(segmented_img == 2)] = [255, 0, 0]
    new_img[np.where(segmented_img == 3)] = [0, 255, 0]

    cv2.imshow('Segmented img', new_img)
    cv2.waitKey(0)