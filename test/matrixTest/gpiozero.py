from gpiozero import LED
import time

# 행(row), 열(column) 도트매트릭스 LED pico에 연
# -1,-2는 행열을 1부터 시작하기 위해 더미(dummy)핀으로 넣음
rows = [-1, LED(9), LED(14), LED(8), LED(12), LED(1), LED(7), LED(2), LED(5)]
cols = [-2, LED(13), LED(3), LED(4), LED(10), LED(6), LED(11), LED(15), LED(16)]

# 사용자 정의함수 clear 선언
def clear():
    for i in range(1, 9):
        cols[i].on()  # 열을 끄기 (LED off)
        rows[i].off()  # 행을 끄기 (LED off)

def test():
    clear()  # 사용자 정의함수 clear 호출, led 초기화
    rows[2].on()  # 2행 led 켜기
    cols[2].off()
    cols[3].off()
    cols[6].off()
    cols[7].off()
    time.sleep(1)

    clear()
    rows[3].on()  # 3행 led 켜기
    cols[1].off()
    cols[4].off()
    cols[5].off()
    cols[8].off()
    time.sleep(1)

    clear()
    rows[4].on()  # 4행 led 켜기
    cols[1].off()
    cols[8].off()
    time.sleep(1)

    clear()
    rows[5].on()  # 5행 led 켜기
    cols[1].off()
    cols[8].off()
    time.sleep(1)

    clear()
    rows[6].on()  # 6행 led 켜기
    cols[2].off()
    cols[7].off()
    # time.sleep(1)

    clear()
    rows[7].on()  # 7행 led 켜기
    cols[3].off()
    cols[6].off()
    # time.sleep(1)

    clear()
    rows[8].on()  # 8행 led 켜기
    cols[4].off()
    cols[5].off()
    # time.sleep(1)

while True:
    # clear()  # 사용자 정의함수 clear 호출, led 초기화

    for i in range(1, 9):
        rows[i].on()
        cols[i].off()
