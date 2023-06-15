import sys
input = sys.stdin.readline

c = [list(map(int, input().split())) for _ in range(5)] # 한줄씩 5개 매핑
mc = []
for _ in range(5):
    mc += list(map(int, input().split())) # 1차원 배열로

# count 함수
# 문자열 안에서 찾고 싶은 문자의 개수 x.count(0) -> 0이 몇개인지
def check():
    bingo = 0
    # 가로 확인
    for x in c: 
        if x.count(0) == 5:
            bingo += 1
    # 세로 확인
    for i in range(5): 
        y = 0
        for j in range(5):
            if c[j][i] == 0:
                y += 1

        if y == 5:
            bingo += 1
    # 왼쪽위부터 시작하는 대각선 확인 \
    d1 = 0
    for i in range(5):
        if c[i][i] == 0:
            d1 += 1

    if d1 == 5:
        bingo += 1
    # 오른쪽위부터 시작하는 대각선 확인 /
    d2 = 0
    for i in range(5):
        if c[i][4-i] == 0:
            d2 += 1

    if d2 == 5:
        bingo += 1
    return bingo 

cnt = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if mc[i] == c[x][y]:
                c[x][y] = 0 # mc와 c가 같으면 0으로 
                cnt += 1
    if cnt >= 12:  # 12개가 이상이면 3빙고일 확률 존재
        result = check()
        if result >= 3: # 3빙고 시
            print(i+1)
            break
