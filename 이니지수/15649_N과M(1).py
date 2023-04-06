from itertools import permutations
n, m = map(int, input().split())
arr = list(range(1, n+1))
num = list(permutations(arr, m))
for i in num:
    print(' '.join(map(str,i)))