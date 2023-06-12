import sys

K, N = map(int, input().split())

lan = [int(sys.stdin.readline()) for _ in range(K)]

def binary_search(start, end, N):
    result = 0  
    while start <= end:
        mid = (start + end) // 2
        lines = sum([(i // mid) for i in lan]) 

        if lines >= N: 
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

answer = binary_search(1, max(lan), N)
print(answer)