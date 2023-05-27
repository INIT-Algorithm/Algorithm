parent=[]

def find(parent,x):
    if(parent[x]==x):
        return x
    return find(parent,parent[x])
    
def union(parent,a,b):
    rootA=find(parent,a)
    rootB=find(parent,b)
    if(rootA<rootB):
        parent[rootB]=rootA
    else:
        parent[rootA]=rootB

def solution(n, costs):
    global parent
    result=0
    parent=[i for i in range(n+1)]
    costs.sort(key=lambda x:x[2]) # [1, 2, 5] : 노드 1과 2가 가중치 5의 값을 갖는 간선으로 연결되어있음
    for c in costs:
        a,b,cost= c
        if find(parent,a)!=find(parent,b):
            union(parent,a,b)
            result+=cost
    return result