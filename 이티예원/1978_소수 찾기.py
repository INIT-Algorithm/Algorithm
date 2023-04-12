import sys

n = int(input())
print(n)
m = [*map(int,sys.stdin.readline().split())]
print(m)
count = 0

for i in m:
    if i != 1 and i != 2:
        for a in range(i):
            if a != 0 and a != 1:
                if i % a == 0:
                    break
                elif a == i-1:
                    count += 1
                    break
        else:
            count += 1
    elif i == 2:
        count += 1

print(count)
