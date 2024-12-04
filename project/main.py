# test.py
import cv2
from objectRec.objectRecognition import capture_camera, get_closest_object
from objectRec.eng2korMapping import eng2kor
from getBraille import word2Braille
import time


def run_camera():

    cap = capture_camera()

    if not cap.isOpened():
        print("Error: 카메라를 열 수 없습니다.")
        return


    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: 프레임을 읽을 수 없습니다.")
            break

        height, width = frame.shape[:2]


        # ★ 물체 인식 조건
        closest_object = get_closest_object(frame, width, height)


        if closest_object:
            korean_label = eng2kor(closest_object)
            braille_result = word2Braille(korean_label)

            print(braille_result)
            time.sleep(3)  # 3초 대기


        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



# 메인 함수 실행
if __name__ == "__main__":
    run_camera()
