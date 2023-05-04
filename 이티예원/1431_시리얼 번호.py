import sys

n = int(sys.stdin.readline())

guitar = []

for _ in range(n):
    guitar.append(sys.stdin.readline().strip())
    
def serialSum(str):
    sum = 0
    for i in str:
        if i.isdigit():
            sum += int(i)
    return sum

guitar.sort(key = lambda x : (len(x), serialSum(x), x))

for a in guitar:
    print(a)
