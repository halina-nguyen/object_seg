import os
import shutil
import random


PATH = "object_segmentation/data/apples2/images"
RATIO = 0.8


# split dataset images into train and val sets
def split_images(img_path, ratio):

    # image directories
    train_img_dir = os.path.join(img_path, 'train')
    val_img_dir = os.path.join(img_path, 'val')

    # label directories
    lbl_dir = os.path.join(img_path, '..', 'labels')
    train_lbl_dir = os.path.join(lbl_dir, 'train')
    val_lbl_dir = os.path.join(lbl_dir, 'val')

    # delete previous distribution
    if os.path.exists(train_img_dir):
        shutil.rmtree(train_img_dir)

    if os.path.exists(val_img_dir):
        shutil.rmtree(val_img_dir)

    if os.path.exists(train_lbl_dir):
        shutil.rmtree(train_lbl_dir)

    if os.path.exists(val_lbl_dir):
        shutil.rmtree(val_lbl_dir)

    # create output directories
    os.makedirs(train_img_dir)
    os.makedirs(val_img_dir)
    os.makedirs(train_lbl_dir)
    os.makedirs(val_lbl_dir)

    # shuffle images
    img = [f for f in os.listdir(img_path) if os.path.isfile(os.path.join(img_path, f))]
    random.shuffle(img)

    # split images
    split_idx = int(len(img) * ratio)
    train_img = img[:split_idx]
    val_img = img[split_idx:]

    # move images and label files to directories
    for f in train_img:
        shutil.copy(os.path.join(img_path, f), os.path.join(train_img_dir, f))
        shutil.copy(os.path.join(lbl_dir, os.path.splitext(f)[0] + '.txt'), os.path.join(train_lbl_dir, f + '.txt'))

    for f in val_img:
        shutil.copy(os.path.join(img_path, f), os.path.join(val_img_dir, f))
        shutil.copy(os.path.join(lbl_dir, os.path.splitext(f)[0] + '.txt'), os.path.join(val_lbl_dir, f + '.txt'))


if __name__ == "__main__":
    split_images(PATH, RATIO)