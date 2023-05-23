import sys

n = int(sys.stdin.readline())  # 컴퓨터의 개수
m = int(sys.stdin.readline())  # 쌍의 개수

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
visited = [0] * (n + 1)


def dfs(start):
    global result
    visited[start] = 1
    for j in graph[start]:
        if visited[j] == 0:
            result += 1
            dfs(j)


dfs(1)
print(result)