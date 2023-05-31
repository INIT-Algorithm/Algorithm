import sys

K, N = map(int, input().split())

lan = [int(sys.stdin.readline()) for _ in range(K)]

def binary_search(start, end, N):
    start = 1 
    end = max(lan)
    
    while start <= end: 
        mid = (start + end) // 2 

    lines = [(i//mid) for i in lan]
   
        
    if lines == N:
        return mid
    elif lines <  N: 
        start = mid + 1
    else:
        end = mid - 1

    print(end)

binary_search(lan, N)