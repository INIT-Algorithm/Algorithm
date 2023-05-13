import itertools

n, m = map(int, input().split())
numlist = list(range(1, n+1))
num = list(itertools.combinations(numlist ,m))
for i in num:
    for j in i:
        print(j, end= ' ')
    print()