import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
end = max(lan)

def lan_length(n):
    count = 0
    for item in lan:
        count += item // n
    return count

def program(start, end, N):
    if start > end:
        return end
    
    mid = (start + end) // 2
    length = lan_length(mid)
    if length >= N:
        return program(mid+1, end, N)
    else:
        return program(start, mid-1, N)

print(program(1, end, N))
