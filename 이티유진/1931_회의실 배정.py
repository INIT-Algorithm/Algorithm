import sys
N = int(sys.stdin.readline())

meetings = []

for _ in range(N):
    start, end = map(int, input().split(" "))
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

time = 0
cnt = 0
for i in meetings:
    if time <= i[0]:
        time = i[1]
        cnt += 1

print(cnt)