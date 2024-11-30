import RPi.GPIO as GPIO
import time

# 행(row), 열(column) 도트매트릭스 LED 핀 연결
rows = [-1, 10, 11, 12, 13, 14, 15, 16, 17]
cols = [-2, 2, 3, 4, 5, 6, 7, 8, 9]

# GPIO 핀 설정
GPIO.setmode(GPIO.BCM)

# 행과 열 핀을 출력으로 설정
for i in range(1, 9):
    GPIO.setup(rows[i], GPIO.OUT)
    GPIO.setup(cols[i], GPIO.OUT)

# 사용자 정의함수 clear 선언
def clear():
    for i in range(1, 9):
        GPIO.output(cols[i], GPIO.HIGH)  # 열 핀에 HIGH 신호 (LED 끄기)
        GPIO.output(rows[i], GPIO.LOW)   # 행 핀에 LOW 신호 (LED 끄기)

try:
    while True:
        clear()  # 사용자 정의함수 clear 호출, LED 초기화
        GPIO.output(rows[2], GPIO.HIGH)  # 2행 LED on
        GPIO.output(cols[2], GPIO.LOW)
        GPIO.output(cols[3], GPIO.LOW)
        GPIO.output(cols[6], GPIO.LOW)
        GPIO.output(cols[7], GPIO.LOW)
        # time.sleep(1)

        clear()
        GPIO.output(rows[3], GPIO.HIGH)  # 3행 LED on
        GPIO.output(cols[1], GPIO.LOW)
        GPIO.output(cols[4], GPIO.LOW)
        GPIO.output(cols[5], GPIO.LOW)
        GPIO.output(cols[8], GPIO.LOW)
        # time.sleep(1)

        clear()
        GPIO.output(rows[4], GPIO.HIGH)  # 4행 LED on
        GPIO.output(cols[1], GPIO.LOW)
        GPIO.output(cols[8], GPIO.LOW)
        # time.sleep(1)

        clear()
        GPIO.output(rows[5], GPIO.HIGH)  # 5행 LED on
        GPIO.output(cols[1], GPIO.LOW)
        GPIO.output(cols[8], GPIO.LOW)
        # time.sleep(1)

        clear()
        GPIO.output(rows[6], GPIO.HIGH)  # 6행 LED on
        GPIO.output(cols[2], GPIO.LOW)
        GPIO.output(cols[7], GPIO.LOW)
        # time.sleep(1)

        clear()
        GPIO.output(rows[7], GPIO.HIGH)  # 7행 LED on
        GPIO.output(cols[3], GPIO.LOW)
        GPIO.output(cols[6], GPIO.LOW)
        # time.sleep(1)

        clear()
        GPIO.output(rows[8], GPIO.HIGH)  # 8행 LED on
        GPIO.output(cols[4], GPIO.LOW)
        GPIO.output(cols[5], GPIO.LOW)
        # time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()  # 프로그램 종료 시 GPIO 리소스 해제
