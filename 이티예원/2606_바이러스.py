from collections import deque

computer = int(input())
v = int(input())
graph = [[] for i in range(computer+1)]
visited = [0]*(computer+1)

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


visited[1] = 1
Q = deque([1])

while Q:
    c = Q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            Q.append(nx)
            visited[nx]=1

print(sum(visited)-1)
