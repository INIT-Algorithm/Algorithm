#2023-05-25-Week7-과제
#1931_회의실 배정

'''
한 개의 회의실을 사용하려는 N개의 회의에 대한 사용표
시작시간, 종료시간 고정
시간이 겹치지 않게 회의실 사용하는 최대 회의 개수

* 중간 중단 x
* 종료 동시에 다음 회의 시작 o
* 회의 시작하자마자 종료 o
* 시작시간 종료시간 0<=자연수<=2^31 -1

입력 1 : 회의 개수 1<=N<=100000
입력 2 : 회의 정보 -> 시작 공백 종료

출력 : 회의 최대 개수
'''

'''
1. 시작시간이 빠른 순서 -> 시작시간이 같은 경우 = 종료시간이 빠른 순서
                        (2,3) (2,7) :: (2,3) -> (2,7)
2. 종료시간이 빠른 순서 -> 종료시간이 같은 경우 = 시작시간이 빠른 순서
                        (7,7) (2,7) :: (2,7) -> (7,7)

(2,7) (3,5) (6,7) 입력시
by 1번 :: (2,7) 회의 1개
by 2번 :: (3,5) (6,7) 회의 2개

--> 종료 시간이 빠른 순서, 
    같은 경우에는 시작 시간이 빠른 순서
'''


### 런타임 에러

import sys
N = int(sys.stdin.readline)

time = [] 
# 시간 저장하는 리스트 
# -> 처음부터 공간을 할당 받고 시작? 입력 받은 만큼 append?

cnt = 0 # 출력할 회의 개수

for _ in range(N):
  start, end = map(int, sys.stdin.readline().split())
  time.append([start, end])

time = sorted(time, key = lambda time: time[0]) # 시작 시간 sort
time = sorted(time, key = lambda time: time[1]) # 종료 시간 sort

final = 0 # 마지막 회의 시간

for i, j in time:
  if i >= final: # 시작 >= 마지막 회의 
    cnt += 1 
    final = j # 갱신

print(cnt)

