#2023-05-11-Week5-수업
#5567_결혼식

'''
입력 값
6
5
1 2
1 3
3 4
2 3
4 5
'''

#bfs 

import sys
from collections import deque

'''
이렇게 작성했더니 런타임에러
input = sys.stdin.readline()
N = int(input())
M = int(input())
'''

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[False] * (N + 1) for i in range(N + 1)]  #False 대신 0 가능 #1번 인덱스부터 사용

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) # a 인덱스에 b 넣기
    graph[b].append(a) # b 인덱스에 a 넣기
    
    #1번 인덱스 -> 본인 -> 본인의 친구

visited = [0] * (N + 1)  # false 대신 0 이어야 함 -> 덧셈 연산 수행을 위해 int형

def bfs(vertex):
    queue = deque([vertex])  
    visited[vertex] = 1  
    while queue: #queue==1일 때 반복
        vertex = queue.popleft()  #deque의 popleft()은 list의 pop(0)와 같지만 O(1)임
        for i in graph[vertex]:  
            if visited[i] == 0: 
                queue.append(i)
                visited[i] = visited[vertex] + 1
bfs(1)
result = 0 #초대하는 동기의 수 
for i in range(2,N+1):
    if (visited[i] != 0) and (visited[i] < 4) :  # 본인/친구/친구의 친구 -> visited 수 범위 1~3
    #if 0 < visited[i] <=3 :  이게 더 간결함
        result += 1   #visited 범위에 해당하면 누적합 계산                                                                                                                                                              
print(result)
