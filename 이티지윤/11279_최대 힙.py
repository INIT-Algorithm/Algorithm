# for문 안의 num = int(input()) # 이 방법 시간초과=> 반복문으로 여러 줄 받을 때 input()은 시간초과 발생

import heapq, sys

heap = []
n = int(input())

for i in range(n):
    num = int(sys.stdin.readline()) # 한 줄 입력 받아 정수형으로 형변환
    if num == 0: # 0 입력되면
        if heap:  # 힙에 요소 있을 때 가장 큰 값 첫번째 루트 노드 삭제
            print(heapq.heappop(heap)[1]) 
        else:# 비어있을 때 0 출력
            print(0)
    else: # 자연수 입력되면
        heapq.heappush(heap, (-num, num)) # (우선순위, 값)

