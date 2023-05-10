import sys
input = sys.stdin.readline

n,k = map(int, input().split())

array = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    array[i][i] = 1
    array[i][0] = 1

for i in range(2,n+1):
    for j in range(1,n+1):
        if array[i][j] != 1:
            array[i][j] = array[i-1][j-1] + array[i-1][j]

print(array[n][k])