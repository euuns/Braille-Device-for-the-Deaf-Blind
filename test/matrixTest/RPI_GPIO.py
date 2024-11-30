import RPi.GPIO as GPIO
import time

# 핀 정의
row_1 = 9
row_2 = 14
row_3 = 8
row_4 = 12
row_5 = 1
row_6 = 7
row_7 = 2
row_8 = 5
col_1 = 13
col_2 = 3
col_3 = 4
col_4 = 10
col_5 = 6
col_6 = 11
col_7 = 15
col_8 = 16

rows = (row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8)
cols = (col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8)


# 핀 초기화
def allOff():
    for row in rows:
        GPIO.output(row, 0)
    for col in cols:
        GPIO.output(col, 1)

def allOn():
    for row in rows:
        GPIO.output(row, 1)
    for col in cols:
        GPIO.output(col, 0)

# 도트 매트릭스 테스트 함수
def test():
    while True:
        for x in range(8):
            allOff()  # 모든 LED 끄기
            GPIO.output(rows[x], 1)  # 현재 행에 신호 출력

            # 여기에 열을 하나씩 켜는 코드를 추가해야 합니다.
            for y in range(8):
                GPIO.output(cols[y], 0)  # 각 열을 차례로 켬
                time.sleep(0.01)  # 짧은 시간 동안 대기
                GPIO.output(cols[y], 1)  # 각 열을 끔



# 프로그램 시작
if __name__ == "__main__":

    # GPIO 초기화
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)  # BCM 핀 번호 사용
    GPIO.setwarnings(False)  # 경고 메시지 비활성화

    # 핀 설정
    for row in rows:
        GPIO.setup(row, GPIO.OUT)
        GPIO.output(row, 0)

    for col in cols:
        GPIO.setup(col, GPIO.OUT)
        GPIO.output(col, 0)

    try:
        allOff()
        test()

    except KeyboardInterrupt:
        GPIO.cleanup()  # GPIO 핀 정리

    finally:
        allOff()  # 프로그램 종료 시 모든 LED 끔
        GPIO.cleanup()  # GPIO 리소스 해제

