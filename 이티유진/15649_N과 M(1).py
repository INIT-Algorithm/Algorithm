import itertools
#from itertools import permutations

n,m = map(int, input().split())

a = []
for i in range(1,n+1):
    a.append(i)

pe = itertools.permutations(a,m)

#print("hello",end='')
#print(*list(pe))

for i in pe:
    for j in i:
        print(j,end = ' ')
    print()