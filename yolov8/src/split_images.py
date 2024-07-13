import os
import shutil
import random


PATH = 'object_segmentation/data/apples/images'
RATIO = 0.8


# split dataset images into train and val sets
def split_images(img_path, ratio):
    train_dir = os.path.join(img_path, 'train')
    val_dir = os.path.join(img_path, 'val')

    # delete previous distribution
    if os.path.exists(train_dir):
        shutil.rmtree(train_dir)

    if os.path.exists(val_dir):
        shutil.rmtree(val_dir)

    # create output directories
    os.makedirs(train_dir)
    os.makedirs(val_dir)

    # shuffle images
    img = [f for f in os.listdir(img_path) if os.path.isfile(os.path.join(img_path, f))]
    random.shuffle(img)

    # split images
    split_idx = int(len(img) * ratio)
    train_files = img[:split_idx]
    val_files = img[split_idx:]

    # move images to directories
    for f in train_files:
        shutil.copy(os.path.join(img_path, f), os.path.join(train_dir, f))

    for f in val_files:
        shutil.copy(os.path.join(img_path, f), os.path.join(val_dir, f))


if __name__ == "__main__":
    split_images(PATH, RATIO)