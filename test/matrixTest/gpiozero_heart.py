from gpiozero import LED
from time import sleep

# 핀 정의
row_1 = LED(9)
row_2 = LED(14)
row_3 = LED(8)
row_4 = LED(12)
row_5 = LED(1)
row_6 = LED(7)
row_7 = LED(2)
row_8 = LED(5)
col_1 = LED(13)
col_2 = LED(3)
col_3 = LED(4)
col_4 = LED(10)
col_5 = LED(6)
col_6 = LED(11)
col_7 = LED(15)
col_8 = LED(16)

rows = (row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8)
cols = (col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8)

# Heart 모양 데이터 정의
Heart_col_0 = (1, 1, 1, 1, 1, 1, 1, 1)
Heart_col_1 = (1, 0, 0, 1, 1, 0, 0, 1)
Heart_col_2 = (0, 0, 0, 0, 0, 0, 0, 0)
Heart_col_3 = (0, 0, 0, 0, 0, 0, 0, 0)
Heart_col_4 = (1, 0, 0, 0, 0, 0, 0, 1)
Heart_col_5 = (1, 1, 0, 0, 0, 0, 1, 1)
Heart_col_6 = (1, 1, 1, 0, 0, 1, 1, 1)
Heart_col_7 = (1, 1, 1, 1, 1, 1, 1, 1)

# 전체 LED 끄기
def allOff():
    for row in rows:
        row.off()
    for col in cols:
        col.on()

# 전체 LED 켜기
def allOn():
    for row in rows:
        row.on()
    for col in cols:
        col.off()

def colTest():
    while True:
        for x in range(8):
            allOff()  # 모든 LED 끄기
            rows[x].off()  # 현재 행에 신호 출력

            # 여기에 열을 하나씩 켜는 코드를 추가해야 합니다.
            for y in range(8):
                cols[y].on()  # 각 열을 차례로 켬
                print(y, cols[y])
                sleep(2)  # 짧은 시간 동안 대기
                cols[y].off()  # 각 열을 끔

def rowTest():
    while True:
        for x in range(8):
            allOff()
            cols[x].off()

            for y in range(8):
                rows[y].on()
                print(y, rows[y])
                sleep(2)
                rows[y].off()

# 실행

colTest()
sleep(0.1)  # 잠시 대기 후 다시 반복
