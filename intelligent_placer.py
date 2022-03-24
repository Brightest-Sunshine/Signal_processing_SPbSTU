import cv2
import numpy as np


def slide_obj_over_fig(main_figure, obj, object_area):
    fig_y, fig_x = main_figure.shape
    obj_y, obj_x = obj.shape
    for pos_y in range(0, fig_y - obj_y, 20):
        for pos_x in range(0, fig_x - obj_x, 20):
            roi = main_figure[pos_y:pos_y + obj_y, pos_x:pos_x + obj_x].astype(int)
            intersect = cv2.bitwise_xor(roi, obj.astype(int))
            if np.sum(intersect) == object_area:
                main_figure[pos_y:pos_y + obj_y, pos_x:pos_x + obj_x] = obj.astype(bool)
                return (pos_y, pos_x), main_figure

    return (-1, -1), main_figure