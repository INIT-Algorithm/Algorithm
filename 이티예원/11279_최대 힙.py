import heapq
import sys

heap = []

#연산의 개수 N을 입력받는다
n = int(input())

for i in range(n):

    #연산에 대한 정보를 나타내는 정수 x가 주어진다
    x = int(sys.stdin.readline())

    #x가 0이라면
    if x == 0:
        #배열의 요소가 있는 경우, 
        #배열에서 가장 큰 갑을 출력
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        #파이썬에서 힙은 최소힙을 따르므로, 최대힙을 구현하기 위해서 *(-1)
        heapq.heappush(heap, (-1)*x)
