import sys

n=int(sys.stdin.readline()) 
m=int(sys.stdin.readline()) 
graph = [[] for i in range(n+1)] 
visited=[0]*(n+1) 

for i in range(m): 
    a,b=map(int,input().split())
    graph[a]+=[b] 
    graph[b]+=[a] 

def dfs(m):
    visited[m]=1
    for i in graph[m]:
        if visited[i]==0:
            dfs(i)
dfs(1)
print(sum(visited)-1)
