#2023-05-11-Week5-과제
#2606_바이러스

'''
입력

7 총 컴퓨터 수
6 컴퓨터 간 연결된 선 개수
1 2 1번컴퓨터와 2번컴퓨터 연결
2 3
...
4 7
'''

#bfs 너비 우선 탐색
import sys
from collections import deque
vertex = int(sys.stdin.readline()) # 컴퓨터 개수
edge = int(sys.stdin.readline()) # 연결선 개수

graph = [[NULL] for i in range(vertex+1)] #그래프
visited = [0]*(vertex+1) #1번 인덱스부터 사용

for i in range(edge): # 그래프 생성
    a,b = map(int,stdin.split())
    graph[a]+=[b] # a 에 b 연결
    graph[b]+=[a] # b 에 a 연결
    
visited[1] = 1 # 1번 컴퓨터부터 시작이니 방문 표시
queue = deque([1])
while queue :
    result = queue.popleft()
    for i in graph[result]:
        if visited[i]==0:
            queue.append(i)
            visited[i]=1
print(sum(visited)-1)   
