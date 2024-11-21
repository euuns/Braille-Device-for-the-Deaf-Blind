# -*- coding: utf-8 -*-
import cv2
import numpy as np

# YOLOv3 모델 설정 파일과 가중치 파일 경로
config_path = 'yolov3.cfg'
weights_path = 'yolov3.weights'
coco_names_path = 'coco.names'

# COCO 데이터셋 클래스 이름 로드
with open(coco_names_path, 'r', encoding='utf-8') as f:
    classes = f.read().strip().split('\n')

# YOLO 모델 로드
net = cv2.dnn.readNet(weights_path, config_path)

# GPU 사용 설정
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# 카메라 캡처 시작
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 입력 이미지 크기
    height, width = frame.shape[:2]

    # YOLOv3 네트워크로 이미지를 변환
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    
    # YOLO 네트워크 계층 이름 로드
    layer_names = net.getLayerNames()

    # UnconnectedOutLayers를 통해 출력 계층 가져오기
    try:
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]
    except AttributeError:
        # OpenCV 버전에 따라 달라질 수 있으므로 예외 처리
        output_layers = [layer_names[int(i) - 1] for i in net.getUnconnectedOutLayers()]

    detections = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    for output in detections:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # 인식할 객체 확인
            # 1(자전거) 2(자동차) 3(오토바이) 5(버스) 7(트럭) 9(신호등) 11(표지판)
            if confidence > 0.5 and class_id in [1, 2, 3, 5, 7, 9, 11]:
                # 경계 상자 계산
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # 경계 상자 그리기
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)
    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = (0, 255, 0)  # 초록색 경계 상자

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # 결과 출력
    cv2.imshow("Real-time Object Detection", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라 및 윈도우 종료
cap.release()
cv2.destroyAllWindows()
