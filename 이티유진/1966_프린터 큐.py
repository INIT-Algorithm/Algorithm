import sys
from collections import deque

t = int(sys.stdin.readline())                           #테스트 케이스 수 t

for i in range(t):
    n, m = map(int,input().split())
    queue = deque(list(map(int,input().split())))       #문서 중요도 queue
    index_queue = deque(list(range(n)))                 #인덱스 idx_queue
    cnt = 0                                             #인쇄 순서 cnt
    while queue:
        if queue[0] == max(queue):                      #queue의 첫번째 원소가 최댓값인 경우(가장 앞에 있는 문서의 중요도가 가장 클 경우) pop
            cnt += 1                                    #pop할 때마다 cnt 1씩 증가
            queue.popleft()
            if index_queue.popleft() == m:              #pop한 문서의 인덱스가 m과 같다면 cnt 출력
                print(cnt)
        else:
            queue.append(queue.popleft())               #queue의 첫번째 원소가 최댓값 아닌 경우 맨 뒤로 재배치
            index_queue.append(index_queue.popleft())