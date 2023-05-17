import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]  
visited = [False]*(n+1)


for i in range(m):
    a, b = map(int, input().split())
   
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, v):
    cnt = 0
    queue = deque([v])  

    while queue:  
        pop = queue.popleft()  
        visited[pop] = True

        for i in graph[pop]:
            if visited[i]==False:
                visited[i] = True
                queue.append(i)  
                cnt += 1  
    print(cnt)

bfs(graph, 1)