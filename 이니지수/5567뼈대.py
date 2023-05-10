# 5567 결혼식

# 입력 값

# 6
# 5
# 1 2
# 1 3
# 3 4
# 2 3
# 4 5

import sys
from collections import deque

# N 과 M 입력 받는 방법 다름
N = 
M = 

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    #그래프 초기 세팅 다름

visited = [0] * (N + 1)  # false 대신 0

def bfs(V):
    q = deque([V])  
    visited[V] = 1 # 숫자 덧셈에 필요
    while q:
        V = q.popleft()
        for i in range(1, N + 1):  #for문 범위 수정
            if not visited[i] and graph[V][i]: # visited[i] 관련 조건 다름
                q.append(i)
                visited[i] =  # visited[i] 구하는 방법 다름
bfs(1)
# 추가 코드
