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

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) # a 인덱스에 b 넣기
    graph[b].append(a) # b 인덱스에 a 넣기

visited = [0] * (N + 1)  # false 대신 0 넣기 -> 더해야돼서!

def bfs(V):
    q = deque([V])  
    visited[V] = 1  
    while q:
        V = q.popleft()
        for i in graph[V]:  
            if visited[i] == 0: 
                q.append(i)
                visited[i] = visited[V] + 1
bfs(1)
result = 0
for i in range(2,N+1):
    # 본인이거나 친구거나, 친구의 친구거나 경우의 수가 최대 3개
    if 0 < visited[i] <=3:
        result += 1
print(result)
