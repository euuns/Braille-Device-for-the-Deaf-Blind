import brailleMapping as bm

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ',
                'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ',
                 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ',
                 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


# 단어를 각 글자별로 초성,중성,종성 나누기
def spilltWord(korean_word):
    r = []
    x = []
    for w in list(korean_word.strip()):
        cho = (ord(w) - ord('가')) // 588
        jung = ((ord(w) - ord('가')) - (588 * cho)) // 28
        jong = (ord(w) - ord('가')) - (588 * cho) - (28 * jung)
        
        r.append(CHOSUNG_LIST[cho])
        r.append(JUNGSUNG_LIST[jung])
        r.append(JONGSUNG_LIST[jong])

        x.append(list(r))
        r = []

    return x


# 자모음을 점자 형태로 변환
def word2Braille(hangul):
    consonant = spilltWord(hangul)
    cho = []
    jung = []
    jong = []

    for x in consonant:
        for y in range(len(x)):
            if y == 0:
                cho = bm.CHO[x[y]]
            elif y == 1:
                jung = bm.JUNG[x[y]]
            else:
                if x[y] != " ":
                    jong = bm.JONG[x[y]]

        if jong:
            printBrailleResult(cho, jung, jong)
            jong.clear()
        else:
            printBrailleResult(cho, jung)
        


def printBrailleResult(cho, jung, jong=0):
    # 초성, 중성, 종성 처리 함수

    # 초성 출력
    for i in range(3):
        if len(cho) > i:  # 리스트 길이를 체크하여 오류를 방지
            print(f"{cho[i][0]} {cho[i][3]}")
            print(f"{cho[i][1]} {cho[i][4]}")
            print(f"{cho[i][2]} {cho[i][5]}")

    # 중성 출력
    for i in range(3):  # 3행
        if len(jung) > i:  # 리스트 길이를 체크하여 오류를 방지
            print(f"{jung[i][0]} {jung[i][3]}")
            print(f"{jung[i][1]} {jung[i][4]}")
            print(f"{jung[i][2]} {jung[i][5]}")

    # 종성 출력
    if jong != 0:
        for i in range(3):  # 3행
            if len(jong) > i:  # 리스트 길이를 체크하여 오류를 방지
                print(f"{jong[i][0]} {jong[i][3]}")
                print(f"{jong[i][1]} {jong[i][4]}")
                print(f"{jong[i][2]} {jong[i][5]}")

