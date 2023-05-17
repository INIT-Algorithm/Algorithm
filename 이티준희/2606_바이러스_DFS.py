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

#dfs 
import sys

vertex = int(sys.stdin.readline())  # 컴퓨터 개수
edge = int(sys.stdin.readline())  # 연결선 개수

graph = [[] for _ in range(vertex + 1)]  # 그래프
visited = [0] * (vertex + 1)  # 1번 인덱스부터 사용

for i in range(edge):  # 그래프 생성
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # a 에 b 연결
    graph[b].append(a)  # b 에 a 연결


def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i)


dfs(1)  # 1번 컴퓨터부터 시작
print(sum(visited) - 1)
