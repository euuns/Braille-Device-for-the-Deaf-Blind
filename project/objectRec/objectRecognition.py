import cv2
import numpy as np
import os
import time

from objectRec.eng2korMapping import eng2kor


# YOLO 모델 경로 설정
config_path = os.getcwd() + '\objectRec\yolov3.cfg'
weights_path = os.getcwd() + '\objectRec\yolov3.weights'
coco_names_path = os.getcwd() + '\objectRec\coco.names'


# COCO 데이터셋 클래스 이름 로드
with open(coco_names_path, 'r', encoding='utf-8') as f:
    classes = f.read().strip().split('\n')


# YOLO 모델 로드
net = cv2.dnn.readNet(weights_path, config_path)


# GPU 사용 설정
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)



def capture_camera():
    return cv2.VideoCapture(0)


# 앞에 있는 객체 확인
def get_closest_object(frame, width, height):

    # YOLO 입력 반환
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]
    detections = net.forward(output_layers)

    best_score = float('-inf')
    closest_object = None


    for output in detections:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # 목표 객체 확인
            if confidence > 0.5 and class_id in [1, 2, 3, 5, 7, 9, 11]:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # 크기 점수와 위치 점수 계산
                size_score = w * h
                position_score = ((center_x - width // 2) ** 2 + (center_y - height // 2) ** 2) ** 0.5
                score = size_score - position_score

                if score > best_score:
                    best_score = score
                    closest_object = classes[class_id]

    return closest_object
