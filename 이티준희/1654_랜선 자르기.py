#2023-05-25-Week7-과제
#1654_랜선 자르기

'''
가지고 있는 K개의 랜선을 잘라서
N개의 같은 길이 랜선으로 만들기
-> K=300일 때 N의 길이가 140이면 N=2, 20은 버려짐

기존 K개의 랜선으로 N개를 만들 수는 없음
자를 때는 정수 단위로만 자름

N개보다 많이 만드는 것도 N개를 만드는 것에 포함


입력 1 : 이미 가지고 있는 K개, 필요한 랜선 N개
(1<=K<=10000  1<=N<=1000000   K<=N)
입력 2 : 이미 가지고 있는 K개의 랜선 각 길이 

랜선의 길이는 자연수<=2^31 -1

출력 : N개를 만들 수 있는 랜선의 최대 길이
'''


import sys
K, N = map(int, sys.stdin.readline().split())

array = []

for i in range(K):
    array.append(int(sys.stdin.readline()))

start = 1 # 최소 1
end = max(array) # 최대

while (start <= end): # 이분탐색 
    # --> start와 end가 동일하면 탈출 = 최대 랜선 길이 발견
    mid = (start + end) // 2 # 중간 지점 값
    cnt = 0 # 랜선 개수 0
    for i in range(K) : 
        cnt += array[i] // mid  # 랜선을 중간 값으로 나누어 개수 파악 
    if cnt >= N : # 랜선 개수가 목표 이상 = 중간 기준으로 오른쪽 탐색
        start = mid + 1
    else :  # 랜선 개수가 목표 미만 = 중간 기준으로 왼쪽 탐색
        end = mid - 1

print(end)


