import sys

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억

N = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"

n = len(alphabet) #26

graph = [[INF] * n for _ in range(n)] # INF로 초기화

for _ in range(N): 
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    graph[a][b] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

M = int(input())
for _ in range(M):
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    if graph[a][b] == INF:
        print("F")
    else:
        print("T")
