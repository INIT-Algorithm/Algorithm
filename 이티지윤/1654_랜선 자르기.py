import sys

input = sys.stdin.readline

# k : 이미 가지고 있는 랜선의 개수, n : 필요한 랜선의 개수
k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

answer = 0  # 랜선의 최대 길이

start, end = 1, max(lan)
while start <= end:
    mid = (start + end) // 2
    temp_sum = 0
    for i in lan:  # mid 길이만큼 랜선 케이블들을 조각냄
        temp_sum += i // mid

    if temp_sum >= n:  # 랜선의 개수가 n이상이면
        start = mid + 1
        answer = mid
    else:  # 랜선의 개수가 n미만이면
        end = mid - 1

print(answer)