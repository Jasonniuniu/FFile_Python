# -*- coding: utf-8 -*-
import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']  #手动添加中文字体

# Root directory of the project
ROOT_DIR = os.path.abspath("../")

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))  # To find local version
import coco

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")
# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

# Directory of images to run detection on
IMAGE_DIR = os.path.join(ROOT_DIR, "images01")
print(IMAGE_DIR)  #输出F:\File_Python\Python_example\Mask_RCNN-master\images01



class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

config = InferenceConfig()
config.display()

#Create Model and Load Trained Weights
# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True)

# COCO Class names
# Index of the class in the list is its ID. For example, to get ID of
# the teddy bear class, use: class_names.index('teddy bear')
# class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
#                'bus', 'train', 'truck', 'boat', 'traffic light',
#                'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
#                'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
#                'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
#                'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
#                'kite', 'baseball bat', 'baseball glove', 'skateboard',
#                'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
#                'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
#                'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
#                'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
#                'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
#                'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
#                'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
#                'teddy bear', 'hair drier', 'toothbrush']

class_names = ['BG', '人类', '自行车', '汽车', '摩托车', '飞机',
               '公共汽车','火车','卡车','小船','红绿灯',
               '消火栓','停车标志','停车计时器','板凳','小鸟',
               '猫','狗','马','羊','牛','象','熊',
               '斑马','长颈鹿','背包','伞','手提包','领带',
               '手提箱','飞盘','滑雪板','滑雪板','运动球',
               '风筝','棒球棒','棒球手套','滑板',
               '冲浪板','网球拍','酒瓶','酒杯','杯子',
               '叉子','刀子','勺子','碗','香蕉','苹果',
               '三明治','橘子','花椰菜','胡萝卜','热狗','披萨',
               '甜甜圈','蛋糕','椅子','沙发','盆栽','床',
               '餐桌','厕所','电视','笔记本电脑','鼠标','遥控器',
               '键盘','手机','微波炉','烤箱','烤面包机',
               '沉','冰箱','书','钟','花瓶','剪刀',
               '泰迪熊','吹风机','牙刷']


#Run Object Detection
# Load a random image from the images folder
file_names = next(os.walk(IMAGE_DIR))[2]
print(file_names) #输出列表，['2018 World Cup (1).png', '2018 World Cup (2).png', '2018 World Cup (3).png', '2018 World Cup (4).png', '2018 World Cup (5).png', '2018.jpg']
image = skimage.io.imread(os.path.join(IMAGE_DIR, random.choice(file_names)))
#IMAGE_DIR='F:\File_Python\Python_example\Mask_RCNN-master\images01\2018.jpg'
print(image)

# Run detection
results = model.detect([image], verbose=1)

# Visualize results
r = results[0]
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                            class_names, r['scores'])





