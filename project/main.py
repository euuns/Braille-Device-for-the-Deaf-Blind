import cv2

from objectRec.objectRecognition import capture_camera
from nearObjectDetection import get_closest_object_with_distance

from objectRec.eng2korMapping import eng2kor
from getBraille import word2Braille

from sensor.distanceMeasurement import measure_distance



def main():
    # 카메라 캡처 초기화
    cap = capture_camera()
    
    # 이전 프레임에서의 크기 및 거리 초기화
    prev_size = 0  # 초기화
    prev_distance = 0  # 초기화
    ultrasonic_threshold = 30.0  # 초음파 감지 임계값 (단위: cm)


    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 프레임 크기 가져오기
            height, width, _ = frame.shape
            
            # 초음파 센서 데이터 읽기
            ultrasonic_distance = measure_distance()


            if ultrasonic_distance < ultrasonic_threshold:  # 초음파 거리 임계값 이내

                # 영상 데이터에서 물체 탐지
                closest_object, current_size, size_change_rate, current_distance, distance_change_rate = \
                    get_closest_object_with_distance(frame, width, height, ultrasonic_distance, prev_size, prev_distance)


                # 물체가 가까워지는 조건 확인
                if distance_change_rate > 0 and size_change_rate > 0:  # 거리 감소 및 크기 증가
                    # 물체 이름을 점자로 변환
                    if closest_object:
                        print(f"점자로 변환 중: {closest_object}")
                        word2Braille(eng2kor(closest_object))  # 점자 출력


                # 이전 크기와 거리 값 업데이트
                prev_size = current_size
                prev_distance = ultrasonic_distance


            # 프레임 출력 (선택사항: 디버깅용)
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
                break


    except KeyboardInterrupt:
        print("프로그램 종료")
    finally:
        cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
