import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

from imageio import imread, imsave
from skimage.morphology import binary_opening
from skimage.measure import regionprops
from skimage.measure import label as sk_measure_label
from scipy.ndimage import binary_fill_holes


def load_images():
    images = []
    directory = 'test_cases'
    files = os.listdir(directory)
    for file in files:
        image = imread(os.path.join(directory, file))
        images.append(image)

    return images


def get_opencv_images(images):
    opencv_images = []
    for image in images:
        opencv_images.append(np.array(image))

    return opencv_images


def set_grayscale(images):
    grayscale_images = []
    opencv_images = get_opencv_images(images)

    for i in range(len(images)):
        open_cv_image = opencv_images[i]
        gray_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        grayscale_images.append(gray_image)

    return grayscale_images


def find_figure_contour(images):
    opencv_images = get_opencv_images(images)
    grayscale_images = set_grayscale(images)

    for counter, grayscale_image in enumerate(grayscale_images):
        _, bw = cv2.threshold(~grayscale_image, 0, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        contours = list(contours)
        contours.sort(key=cv2.contourArea, reverse=True)

        if len(contours[0]) > 0:
            contour = contours[0]
            epsilon = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.003 * epsilon, True)
            cv2.drawContours(opencv_images[counter], [approx], -1, (0, 255, 255, 255), 30)

    return opencv_images


def create_mask_without_figure(open_cv_images):
    mask_without_figures = []
    grayscale_images = set_grayscale(open_cv_images)

    for grayscale_image in grayscale_images:
        _, bw = cv2.threshold(grayscale_image, 0, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        _, _ = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        tmp = binary_opening(bw, footprint=np.ones((20, 20)))
        mask_without_figures.append(~tmp)

    return mask_without_figures


def create_mask(images):
    masks = []
    grayscale_images = set_grayscale(images)

    for grayscale_image in grayscale_images:
        _, bw = cv2.threshold(grayscale_image, 0, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        _, _ = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        res_otsu_enclosed = binary_opening(bw, footprint=np.ones((20, 20)))
        masks.append(~res_otsu_enclosed)

    return masks


def create_mask_figure(images):
    mask_figures = []
    res_otsu_enclosed = create_mask(images)
    opencv_images = find_figure_contour(images)
    mask_without_figures = create_mask_without_figure(opencv_images)

    for i in range(len(images)):
        mask_figures.append(mask_without_figures[i] ^ res_otsu_enclosed[i])

    return mask_figures


def get_largest_component(mask):
    labels = sk_measure_label(mask)
    props = regionprops(labels)
    areas = [prop.area for prop in props]

    largest_comp_id = np.array(areas).argmax()
    return labels == (largest_comp_id + 1)


def fill_mask_figure(masks):
    fill_masks = []
    for mask in masks:
        tmp = get_largest_component(mask)
        fill_masks.append(binary_fill_holes(tmp))
    return fill_masks


def create_bbox(masks):
    bboxes, object_area = [], []
    # для фигуры на вход должна приходить фил маск
    for mask in masks:
        label = sk_measure_label(mask)
        prop = regionprops(label)[0]
        bboxes.append(prop.bbox)
        object_area.append(prop.area)
    return bboxes, object_area


def truncate_mask(masks, bboxes):
    truncate_masks = []

    for mask, bbox in zip(masks, bboxes):
        truncate_masks.append(mask[bbox[0]:bbox[2], bbox[1]:bbox[3]])

    return truncate_masks


def sh(im):
    for i in im:
        plt.imshow(i)
        plt.gray()
        plt.show()

def show_obj(im):
    for i in im:
        for j in i:
            plt.imshow(j)
            plt.gray()
            plt.show()
##################################################################################################### для фигур


def find_objects(mask):
    labels = sk_measure_label(mask)
    props = regionprops(labels)
    areas = [prop.area for prop in props]
    object_masks = []
    for i in range(len(areas)):
        if areas[i] != 1:
            largest_comp_id = i
            object_masks.append(labels == (largest_comp_id + 1))

    return object_masks


def create_masks_for_objects(mask_without_figure):
    masks_for_objects = []
    object_areas = []
    for mask in mask_without_figure:
        object_mask = find_objects(mask)
        objects_bbox, object_area = create_bbox(object_mask)
        masks_for_objects.append(truncate_mask(object_mask, objects_bbox))
        object_areas.append(object_area)

    return masks_for_objects, object_areas


def reverse_object_masks(masks_for_objects):
    for i in range(len(masks_for_objects)):
        for j in range(len(masks_for_objects[i])):
            masks_for_objects[i][j] = ~masks_for_objects[i][j]

    return masks_for_objects
