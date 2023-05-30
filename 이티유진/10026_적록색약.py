import sys
from collections import deque

n = int(sys.stdin.readline())
visited = [[False] * n for _ in range(n)]
grid = [list(map(str, input())) for _ in range(n)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
                queue.append([nx, ny])
                visited[nx][ny] = True

count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
print(count, end=' ')

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
print(count)