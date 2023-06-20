#DFS

computer=int(input())
v=int(input())

graph = [[] for i in range(computer+1)]
visited=[0]*(computer+1)

for i in range(v): 
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)
            
dfs(1)
print(sum(visited)-1)
