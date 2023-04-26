#2023-04-15-Week2-과제
#11279_최대 힙

'''
배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 
주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
x가 0이라면 배열에서 가장 큰 값을 출력하고 
그 값을 배열에서 제거하는 경우이다. 
입력되는 자연수는 231보다 작다.

입력에서 0이 주어진 회수만큼 답을 출력한다.
만약 배열이 비어 있는 경우인데 
가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.
'''


'''
import heapq
heap = []
num = int(input())

for i in range(num) :
    a = int(input())
    if a==0:
        if heap :
            print(heapq.heappop(heap)[1])
        else :
            print(0)
    elif a>0 :
        heapq.heappush(heap, (-a,a))
'''

#채점 결과 시간 초과 
#input() -> sys.stdin.readline()

import heapq
import sys
heap = []
num = int(sys.stdin.readline())

for i in range(num) :
    a = int(sys.stdin.readline())
    if a==0: #a가 0이라면
        if heap : 
            print(heapq.heappop(heap)[1]) # 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
        else : #
            print(0)
    elif a>0 : #a가 자연수라면
        heapq.heappush(heap, (-a,a)) #a라는 값을 넣는 연산
        