#2023-05-18-Week6-과제
#10026_적록색약

'''
입력 :
1. 입력 크기 1 ≤ N ≤ 100
2. 그리드 입력 (N*N)

출력 : 
적록색약 아닌 사람의 구역, 적록색약인 사람의 구역
'''




#런타임 에러 발생

from collections import deque
import sys
import string

sys.setrecursionlimit(100000) #재귀
input=sys.stdin.readline()

N = int(input())
matrix = [list(input().rstrip()) for i in range(N)]

visited = [[0]*N  for i in range(N)] #방문 안 한 상태로 설정


def dfs(x,y) : 

    move_x = [-1,1,0,0]
    move_y = [0,0,-1,1]

    color = matrix[x][y]  #R, G, B
    visited[x][y] = True  #방문

    for i in range(4) : #상하좌우 
        new_x = x + move_x[i]
        new_y = y + move_y[i]
        if {(0 <= new_x <= N - 1) 
            and (0 <= new_y <= N - 1) 
            and (visited[new_x][new_y] == False)}:
            if color == matrix[new_x][new_y] :
                dfs(new_x,new_y)

#정상
normal = 0

for x in range(N) :
    for y in range(N) :
        if visited[x][y] == False : 
            dfs(x,y)
            normal += 1

#적록색약
noRG = 0
for x in range(N) : #적록색약 기준으로 색 변경
    for y in range(N) :
        if matrix[x][y] == 'R' or matrix[x][y] == 'G' :
            matrix[x][y] == 'g'

visited = [[0]*N  for i in range(N)] #방문횟수 초기화
for x in range(N) :
    for y in range(N) :
        if visited[x][y] == False : 
            dfs(x,y)
            noRG += 1

#출력
print(normal, noRG)






