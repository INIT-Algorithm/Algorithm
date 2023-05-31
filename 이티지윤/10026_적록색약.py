#10026_적록색약
#적록색약이 아닌 사람 : 유기농 배추랑 똑같음
#적록색약인 사람 : 
import sys
sys.setrecursionlimit(10000)

read=sys.stdin.readline
#MAX= 100+10
#print(MAX)
n = int(read())

#인덱스0부터 3까지 차례대로 합치면 오른쪽, 왼쪽, 위, 아래 
dirX = [1, -1, 0, 0]
dirY = [0, 0, 1, -1]

#graph
graph = [list(input().rstrip()) for _ in range(n)]

#visited
visited=[[False]*(n) for _ in range(n)]

count1 = 0
count2 = 0


def dfs(x,y):
    global graph, visited
    visited[x][y] = True

    for i in range(4):
        newX = x + dirX[i]
        newY = y + dirY[i]
        if (n > newX >= 0) and (n > newY >= 0):
            if not visited[newX][newY]:
                if graph[newX][newY] == graph[x][y]:#위 조건 만족하면서 탐색중인 색상과 같은 색이면    
                        dfs(newX, newY)  #dfs로 탐색

# 적녹색약이 아닌 사람 
for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] and not visited[i][j]:
            dfs(i, j)
            count1 += 1

# 적녹색약인 사람
# 초록색->빨간색으로 변경
for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
# 방문정보 초기화
visited = [[False]*(n) for _ in range(n)] 
for i  in range(0, n):
    for j in range(0, n):
        if graph[i][j] and not visited[i][j]:
            dfs(i, j)
            count2 += 1

print(count1, count2)



