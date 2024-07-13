import os
from ray import tune
from ray.tune.schedulers import ASHAScheduler
from ray.tune.search.hyperopt import HyperOptSearch
from ultralytics import YOLO


def train(config):
    model = YOLO("yolo_segmentation/yolov8m-seg.pt")

    model.train(
        data='coco.yaml',
        epochs=50,
        imgsz=640,
        batch=16,
    )

    results = model.val()
    return results


if __name__ == "__main__":
    train()