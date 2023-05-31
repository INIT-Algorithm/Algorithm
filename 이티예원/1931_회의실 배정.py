N = int(input())
time = []


for i in range(N):
    start, end = map(int, input().split())
    time.append([start, end])


time = sorted(time, key = lambda a : a[0])  
time = sorted(time, key = lambda a : a[1])

finish = 0
cnt = 0

for start, end in time:
    if start >= finish:
        cnt += 1
        finish = end

print(cnt)
