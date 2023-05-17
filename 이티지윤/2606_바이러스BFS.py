import sys
from collections import deque

N = int(sys.stdin.readline())
C = int(sys.stdin.readline())

graph = [[] for i in range(N+1)]

for i in range(C):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []
def bfs(x):
    q = deque([x])
    visited.append(x)
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if i not in visited:
                q.append(i)
                visited.append(i)
                
bfs(1)
print(len(visited) -1) # 1번 컴퓨터는 제외
