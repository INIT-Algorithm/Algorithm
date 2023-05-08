import sys
import heapq

n = int(sys.stdin.readline())
heap = []

# -1을 곱해 최소 힙으로 최대 힙 구현
for i in range (n):
    x = int(sys.stdin.readline())
    if x == 0:                                  # x가 0일 때
        if heap:                                    # 배열에서 가장 큰 값 출력하고 그 값을 배열에서 삭제
            print((-1)*heapq.heappop(heap))         
        else:                                       # 배열이 비어있을 경우 0 출력 
            print(0)                            
    elif x > 0:                                 # x가 자연수일 때
        heapq.heappush(heap,(-1)*x)                 # 배열에 x라는 값 추가
