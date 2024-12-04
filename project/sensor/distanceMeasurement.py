import RPi.GPIO as GPIO # type: ignore
import time

# 초음파 센서 핀 설정
TRIG_PIN = 23
ECHO_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)


# 초음파 센서로 거리 측정
def measure_distance():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)  # 트리거 신호를 10μs 동안 출력
    GPIO.output(TRIG_PIN, False)

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # 초음파의 속도(34300cm/s)를 반영
    return round(distance, 2)
