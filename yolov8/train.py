from ultralytics import YOLO
from src.split_images import split_images
from src.coco2yolo import coco_to_yolo


IMG_PATH = "object_segmentation/data/apples/images"
ANN_PATH = "object_segmentation/data/apples/annotations/instances_default.json"
RATIO = 0.8

MODEL_PATH = "object_segmentation/yolov8m-seg.pt"
DATA_PATH = "object_segmentation/coco.yaml"


def train(config):
    model = YOLO(MODEL_PATH)

    model.train(
        data=DATA_PATH,
        epochs=50,
        imgsz=640,
        batch=16,
    )


if __name__ == "__main__":

    # prepare YOLO training
    split_images(IMG_PATH, RATIO)
    coco_to_yolo(ANN_PATH)

    # train model
    train()