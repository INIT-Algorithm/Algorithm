# 2839_설탕 배달
# -> 정답

N = int(input())
count = 0

while N >= 0:
    if N % 5 == 0 : # 전체 무게의 합을 5로 나누었을 때 나누어 떨어지면
        count += N // 5  # 그 몫 만큼 봉지 추가
        print (count)   # 총 봉지 수 출력
        break
    N -= 3   # 전체 무게의 합에서 3 빼기
    count += 1  # 3kg 봉지 한 개 추가

    if N < 0 : # 봉지를 만들 수 없는 음수
        print(-1)  # -1 출력