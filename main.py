from figure_detection import *
from intelligent_placer import slide_obj_over_fig

if __name__ == '__main__':
    im = load_images()
    gr = set_grayscale(im)
    cont = find_figure_contour(im)
    a = create_mask_figure(im)
    fill_mask = fill_mask_figure(a)
    bbox, _ = create_bbox(fill_mask)
    tr = truncate_mask(fill_mask, bbox)

    b = find_figure_contour(im)
    mask_without_fig = create_mask_without_figure(b)
    masks_for_objects, object_areas = create_masks_for_objects(mask_without_fig)
    masks_for_objects = reverse_object_masks(masks_for_objects)
    #show_obj(masks_for_objects)

    object_loc = []
    answer = []
    i = 1

    for main_fig, obj, obj_area in zip(tr, masks_for_objects, object_areas):
        for ob, area in zip(obj, obj_area):
            (y, x), result = slide_obj_over_fig(main_fig, ob, area)
            object_loc.append([y, x])

            if x == -1:
                print(i, "No")
                break

        plt.imshow(result, cmap='gray')
        plt.show()
        print(i, "Yes")
        answer.append(result)
        i += 1

