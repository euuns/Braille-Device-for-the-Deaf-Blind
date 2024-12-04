# 영어-한글 라벨 매핑
label_map = {
    "bicycle": "자전거",
    "car": "자동차",
    "motorbike": "오토바이",
    "bus": "버스",
    "truck": "트럭",
    "traffic light": "신호등",
    "stop sign": "표지판"
}

def eng2kor(eng):
    return label_map.get(eng, "알 수 없는 라벨")  # 매핑되지 않은 경우 기본값
