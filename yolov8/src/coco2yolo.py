import json
import os
import shutil


PATH = "object_segmentation/data/apples/annotations/instances_default.json"


# convert COCO json file to YOLO format
def coco_to_yolo(ann_path):
    try:
        with open(ann_path, 'r') as f:
            ann = json.load(f)

        # map each image to id, width and height
        imgs = {}
        width = {}
        height = {}
        for img in ann['images']:
            if img['id'] not in imgs:
                imgs[img['id']] = img['file_name']
                width[img['id']] = img['width']
                height[img['id']] = img['height']

        # create output directory
        label_dir = os.path.join(os.path.dirname(ann_path), '..', 'labels')
        if os.path.exists(label_dir):
            shutil.rmtree(label_dir)
        os.makedirs(label_dir)

        # create text file for each image
        for a in ann['annotations']:
            output_dir = os.path.join(label_dir, os.path.splitext(imgs[a['image_id']])[0] + '.txt')

            if os.path.exists(output_dir):
                open(output_dir, "w+").close()

        # write text file for each image
        for obj in ann['annotations']:
            xs_ys = a['segmentation'][0]

            if len(xs_ys) >= 6 and not len(xs_ys) % 2 and obj['image_id'] in imgs and obj['image_id'] in width and obj['image_id'] in height:

                # open text file
                output_dir = os.path.join(label_dir, os.path.splitext(imgs[obj['image_id']])[0] + '.txt')
                ann_output = open(output_dir, "a")

                # print class index
                class_index = a['category_id']
                ann_output.write(f"{class_index} ")

                # print bounding coordinates of segmentation mask
                for x_y in xs_ys:
                    if xs_ys.index(x_y) % 2:
                        y = x_y / height[obj['image_id']]
                        ann_output.write(f"{y} ")
                    else:
                        x = x_y / width[obj['image_id']]
                        ann_output.write(f"{x} ")

                # add new row for next object
                idx = ann['annotations'].index(obj)
                if idx+1 < len(ann['annotations']) and obj['image_id'] == ann['annotations'][idx+1]['image_id']:
                    ann_output.write("\n")
                else:
                    ann_output.close()

    except FileNotFoundError:
        print(f"Error: File '{ann_path}' not found.")


if __name__ == "__main__":
    coco_to_yolo(PATH)